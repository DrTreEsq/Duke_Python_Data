import os
from collections import defaultdict
from pathlib import Path

import click
from termcolor import cprint

from kaze import Envs
from kaze.curl_utils import download
from kaze.file_utils import load_yml, write_yml, get_md5, decompress, is_archive
from kaze.utils import omit, NamedList


class KazeConfig:
    datasets = None

    def load(self):
        config = load_yml(".kaze.yml") or defaultdict(list)
        config_lock = load_yml(".kaze-lock.yml") or defaultdict(list)

        self.datasets = NamedList()
        for entry in [*config['datasets'], *config_lock['datasets']]:
            self.datasets.add(**entry)

        self.config = omit(config, "datasets")

    def save(self):
        write_yml(dict(datasets=self.datasets.omit("archive_path", "hash"), **self.config),
                  ".kaze.yml")
        write_yml({'datasets': self.datasets.pick("name", "source", "path", "archive_path", "hash")},
                  ".kaze-lock.yml")


@click.group(invoke_without_command=True)
@click.pass_context
def kaze(ctx):
    if ctx.invoked_subcommand is None:
        kaze_config = KazeConfig()
        kaze_config.load()

        n = len(kaze_config.datasets)
        if n:
            print(f"Found {n} dataset{'s' if n > 1 else ''}.")
        else:
            print("No datasets found")

        # todo: read from .kaze.yml instead
        # todo: add new entries to .kaze.yml

        for entry in kaze_config.datasets.to_list():

            path = entry['path']
            raw_path = os.path.expandvars(path)

            if not os.path.exists(raw_path):
                cprint(f"{entry['name']} is missing", "red")

                source = entry['source']

                if 'archive_path' in entry:
                    archive_path = entry['archive_path']
                else:
                    # this is inconsistent
                    archive_path = path + Path(source).suffix
                    entry['archive_path'] = archive_path

                raw_archive_path = os.path.expandvars(archive_path)
                download(source, raw_archive_path)
                if is_archive(raw_archive_path):
                    decompress(raw_archive_path, raw_path)
                    os.remove(raw_archive_path)

                kaze_config.save()


@kaze.command()
@click.argument("source", default="")
@click.option("--name", '-n', default=None)
@click.option("--path", '-o', default=None, help="target location for the dataset")
@click.option("--images", '-i', default=None, help="image path")
@click.option("--labels", default=None, help="label path")
@click.option("--voice", default=None, help="voice path")
@click.option("--video", default=None, help="video path")
@click.option("--quiet", "-q", is_flag=True, help="Verbose mode")
@click.option("--unzip", "-z", is_flag=True, help="Decompress the dataset")
# @click.option("--remove_archive", "-z", is_flag=True, help="Decompress the dataset")
@click.option("--verbose", "-v", is_flag=True, help="Verbose mode")
def add(source, name, path, images, labels, voice, video, quiet, unzip, verbose, **kwargs):
    kaze_config = KazeConfig()
    kaze_config.load()

    if name is None:
        name = Path(source).stem
        print(f"Using the name {name}")

    if path is None:
        path = Envs.DATASETS_ROOT + "/" + name

    raw_path = os.path.expandvars(path)

    # todo: ask to overwrite/download again if the dataset already exists
    if name in kaze_config.datasets:
        answer = input(f"{name} has already been added. Update? [Y/n]") or "Y"
        if answer.lower() == "n":
            print('Exiting...')
            return

    cprint(f"adding {name} from {source}. Download to {path}", "blue")

    archive_path = raw_path + Path(source).suffix
    raw_archive_path = os.path.expandvars(archive_path)

    if os.path.exists(archive_path):
        cprint(f"{name} already exists", "red")
        answer = input(f"Remove {path} and download again? [Y/n]") or "Y"
        if answer.lower() == "y":
            os.remove(archive_path)
            print(f"Downloading {name} to {path}") or "Y"
            download(source, raw_archive_path)
    elif quiet:
        print(f"Downloading {name} to {path}") or "Y"
        download(source, raw_archive_path)
    else:
        answer = input(f"Download the file to {path}? [Y/n]") or "Y"
        if answer.lower() == "y":
            download(source, raw_archive_path)

    # load again since the config files might have changed.
    kaze_config.load()
    kaze_config.datasets.add(name=name, source=source, archive_path=archive_path,
                             hash=get_md5(archive_path), path=path,
                             images=images, labels=labels, voice=voice, video=video)

    if unzip or is_archive(raw_archive_path):
        decompress(raw_archive_path, raw_path)
        # if remove_archive:
        os.remove(raw_archive_path)

    kaze_config.save()


@kaze.command(name="list")
def list_command():
    kaze_config = KazeConfig()
    kaze_config.load()

    for entry in kaze_config.datasets.values():
        print(f"{entry['name']} at {entry['path']}")

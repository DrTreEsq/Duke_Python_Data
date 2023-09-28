import gzip
import os
import re
import shutil

import yaml


def load_yml(filename):
    try:
        with open(filename, "r") as f:
            return yaml.load(f, Loader=yaml.FullLoader)
    except FileNotFoundError:
        return None


def write_yml(data, filename):
    with open(filename, "w") as f:
        yaml.dump(data, f, sort_keys=False)


def get_md5(filename):
    import hashlib

    with open(filename, "rb") as f:
        h = f.read()
        return hashlib.md5(h).hexdigest()


def is_zip(filename):
    return "."


def gunzip_something(gzipped_file_name, work_dir):
    """gunzip the given gzipped file"""

    # see warning about filename
    filename = os.path.split(gzipped_file_name)[-1]
    filename = re.sub(r"\.gz$", "", filename, flags=re.IGNORECASE)

    with gzip.open(gzipped_file_name, 'rb') as f_in:  # <<========== extraction happens here
        with open(os.path.join(work_dir, filename), 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


shutil.register_unpack_format('gz', ['.gz', ], gunzip_something)


def is_archive(filename):
    return shutil._find_unpack_format(filename)


def decompress(source, dest, recursive=False):
    import shutil
    import os

    shutil.unpack_archive(source, dest)

    if recursive:
        for child in os.listdir(dest):
            if is_archive(child) is not None:
                decompress(dest + "/" + child, dest, recursive=False)


def cwd_ancestors():
    """generator returning the the current directory and ancestors one after another"""
    import os
    _ = os.path.abspath(os.getcwd())
    while True:
        yield _
        parent = os.path.dirname(_)
        if parent == _:
            break
        else:
            _ = parent

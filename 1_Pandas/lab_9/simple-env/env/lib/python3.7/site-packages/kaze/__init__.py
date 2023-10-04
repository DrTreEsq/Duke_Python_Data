import glob
import os.path
from collections import defaultdict
from pathlib import Path

from params_proto.neo_proto import ParamsProto, Proto

from kaze.file_utils import load_yml, cwd_ancestors
from kaze.utils import NamedList


class Envs(ParamsProto, cli=False):
    KAZE_DATASETS_ROOT = Proto(env='KAZE_DATASETS_ROOT', default='$HOME/datasets')
    DATASETS_ROOT = Proto(env='DATASETS', default=KAZE_DATASETS_ROOT.value)


class Datasets(NamedList):
    def __init__(self, config_path=None):
        # todo: need to traverse parents
        if config_path is None:
            for d in cwd_ancestors():
                try:
                    config_path, = glob.glob(d + "/.kaze.yml")
                    break
                except Exception:
                    pass

        super().__init__()

        if config_path is None:
            return

        config = load_yml(config_path) or defaultdict(list)
        # config_lock = load_yml(".kaze-lock.yml") or defaultdict(list)

        for entry in config['datasets']:
            # resolve path
            raw_path = os.path.expandvars(entry['path'])
            self.add(**entry, raw_path=Path(raw_path))


datasets = Datasets()

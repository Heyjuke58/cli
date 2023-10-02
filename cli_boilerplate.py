import argparse
import shutil
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dir", type=str, help="Directory where to paste the boilerplate code.")

    args = parser.parse_args()

    return args


def main(dir: str):
    target_path_parser = Path(dir + "/argument_parser.py")
    assert not target_path_parser.is_file(), "There already exists a argument_parser.py in the target directory. Remove it first."
    shutil.copy(Path("argument_parser.py"), target_path_parser)

    target_path_main = Path(dir + "/main.py")
    assert not target_path_main.is_file(), "There already exists a main.py in the target directory. Remove it first."
    shutil.copy(Path("main.py"), target_path_main)


if __name__ == "__main__":
    args = parse_args()
    main(args.dir)

import argparse
import shutil
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dir", type=str, help="Directory where to paste the boilerplate code.")

    args = parser.parse_args()

    return args


def main(dir: str):
    target_path = Path(dir + "/parse_arguments2.py")
    assert not target_path.is_file(), "There already exists a argument_parser.py in the target directory. Remove it first."

    shutil.copy(Path("argument_parser.py"), target_path)


if __name__ == "__main__":
    args = parse_args()
    main(args.dir)

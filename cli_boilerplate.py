import argparse
import shutil
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", dest="dir", type=str, help="Directory where to paste the boilerplate code.")
    parser.add_argument("-h", dest="home_dir", type=str, help="Home directory where to paste the boilerplate code.")

    args = parser.parse_args()

    return args


def main(dir: str, home_dir: str):
    target_path_parser = Path(dir + "/argument_parser.py")
    assert not target_path_parser.is_file(), "There already exists a argument_parser.py in the target directory. Remove it first."
    shutil.copy(Path(home_dir + "/bin/argument_parser.py"), target_path_parser)

    target_path_main = Path(dir + "/main.py")
    assert not target_path_main.is_file(), "There already exists a main.py in the target directory. Remove it first."
    shutil.copy(Path(home_dir + "/bin/main.py"), target_path_main)


if __name__ == "__main__":
    args = parse_args()
    main(args.dir)

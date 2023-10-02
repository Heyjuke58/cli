import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
    )
    parser.add_argument(
        "-f",
        "--flag",
        dest="flag",
        action="store_true",
        help="Some flag that is true when set.",
    )
    parser.add_argument(
        "-s",
        "--string",
        dest="string",
        type=str,
        default="default",
        help="Some string with a default.",
    )
    parser.add_argument(
        "-c",
        "--choices",
        dest="custom",
        type=int,
        default=0,
        choices=range(0, 2),
        help="Some int with choices.",
    )

    args = parser.parse_args()

    return args

from argument_parser import parse_args


def main(**kwargs):
    print(kwargs)
    pass


if __name__ == "__main__":
    args = parse_args()
    args = vars(args)
    main(**args)

from resotolib.args import ArgumentParser


def add_args(arg_parser: ArgumentParser) -> None:
    arg_parser.add_argument(
        "--path",
        "-p",
        help="Path to App bundle",
        dest="app_path",
        required=True,
        type=str,
    )

__VERSION__ = "0.0.0"

from lists import *
import argparse


def parse_args():  # pragma: no cover
    parser = argparse.ArgumentParser(
        description=""
    )
    subparsers = parser.add_subparsers(dest="action")

    get_lists = subparsers.add_parser(
        "get_lists", help="Get Lists"
    )

    add_item = subparsers.add_parser(
        "add_item", help="Add Item To List"
    )
    add_item.add_argument(
        "-i",
        "--item",
        help="The item you are adding to the list",
        action="store",
        type=str,
        required=True,
    )

    create_list = subparsers.add_parser(
        "create_list",
        help="Create New List",
    )

    delete_list = subparsers.add_parser(
        "create_list",
        help="Create New List",
    )

    return parser.parse_args()


def main():  # pragma: no cover
    args = parse_args()

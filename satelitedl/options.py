# coding: utf-8
import argparse


def parse_args() -> dict:
    """parse_args.
    set datetime ex:19901010
    Args:

    Returns:
        dict:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date",
                        help="set datetime ex 19910101", type=str)
    p = parser.parse_args()
    args = {"date": p.date}
    return args

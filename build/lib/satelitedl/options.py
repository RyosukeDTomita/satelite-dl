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
    parser.add_argument("-o", "--outdir",
                        help="set output dir path", type=str)
    p = parser.parse_args()
    args = {"date": p.date, "outdir": p.outdir}
    return args

# coding: utf-8
"""
Usage: python3 -m satelitedl --date 19900101
Authore: Ryosuke Tomita
Date: 2021/11/02
"""
from datetime import datetime
from .options import parse_args
from .scrapeimg import ScrapingImg

def create_url(date: str) -> str:
    """create_url.

    Args:
        date (str): date

    Returns:
        str:
    """
    base_url = "http://weather.is.kochi-u.ac.jp/sat/ALL/"
    date_str = datetime.strptime(date, "%Y%m%d")
    url_data_part = date_str.strftime("%Y/%d/%m/")
    return (base_url + url_data_part)


def main():
    """main
    1. get argument.
    2. scrape satelite picture from
    "http://weather.is.kochi-u.ac.jp/sat/ALL/"
    """

    args = parse_args()
    date = args["date"]
    if date is None:
        raise Exception('No argument about date.')

    url = create_url(date)

    scrape_img = ScrapingImg(url)
    scrape_img.fetch_img_url()
    scrape_img.download_file()


__all__ = ["main", "create_url"]

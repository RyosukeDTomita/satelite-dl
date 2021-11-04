# coding: utf-8
"""
Usage: python3 -m satelitedl --date 19900101
Authore: Ryosuke Tomita
Date: 2021/11/02
"""
from datetime import datetime
from typing import Union
from .options import parse_args
from .scrapeimg import ScrapingImg


def judge_date_type(date: str) -> str:
    """judge_date_type.
    Using "date"(str) length, judge date type.
    Args:
        date (str): date

    Returns:
        str:
    """
    if len(date) == 8:
        date_type = "day"
    elif len(date) == 6:
        date_type = "month"
    elif len(date) == 4:
        date_type = "year"
    else:
        raise Exception (f'{date} is not valid value.')

    return date_type


def create_url(date: str) -> Union[str, None]:
    """create_url.

    Args:
        date (str): date

    Returns:
        Union[str, None]:
    """
    try:
        date_str = datetime.strptime(date, "%Y%m%d")
    except ValueError:
        return None
    url_data_part = date_str.strftime("%Y/%m/%d/")
    base_url = "http://weather.is.kochi-u.ac.jp/sat/ALL/"
    return base_url + url_data_part


def use_scrapeimg(date: str, date_type: str):
    """use_scrapeimg.
    use module "scrapeimg".
    Args:
        date (str): date
        date_type (str): date_type
    """

    def run_scrape_img(_date: str):
        """run_scrape_img.

        Args:
            _date (str): _date
        """
        url = create_url(_date)
        if url is None:
            return
        scrape_img = ScrapingImg(url)
        scrape_img.fetch_img_url()
        scrape_img.download_file()

    month_list = tuple([f'{m+1:02}' for m in range(12)])
    day_list = tuple([f'{y+1:02}' for y in range(31)])
    if   date_type == "year":
        for month in month_list:
            for day in day_list:
                date_day = (date + month + day)
                run_scrape_img(date_day)
    elif date_type == "month":
        for day in day_list:
            date_day = (date + day)
            run_scrape_img(date_day)
    elif date_type == "day":
        date_day = date
        run_scrape_img(date_day)


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

    date_type = judge_date_type(date)

    use_scrapeimg(date, date_type)


__all__ = ["main", "create_url", "judge_date_type", "use_scrapeimg"]

# config: utf-8
from setuptools import setup
from setuptools import find_packages


def main():
    setup(
        name="satelite-dl",
        version="0.0.1",
        description='download satelite data from http://weather.is.kochi-u.ac.jp/sat/ALL/',
        author="Ryosuke Tomita",
        packages=find_packages(),
        install_requires=[
            'argparse',
            'bs4',
            'datetime',
            'typing',
        ],

        entry_points={
            'console_scripts': [
                'satelite-dl = satelitedl:main',
            ],
        }
    )


if __name__ == "__main__":
    main()

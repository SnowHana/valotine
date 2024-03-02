import sys


# print(sys.path)
from opgg.opgg import OPGG

from opgg.summoner import Summoner


def main():
    opgg = OPGG()

    summoner: Summoner
    for summoner in opgg.search(["JUGKING"]):
        print(summoner)


if __name__ == "__main__":
    main()

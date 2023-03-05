import sys
import re
import matplotlib.pyplot as plt


def add_date(dist: dict, year: str):
    if year in dist:
        dist[year] += 1
    else:
        dist[year] = 1


def main():
    text = sys.stdin.readlines()
    pattern = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')
    dist = {}

    for line in text:
        date = pattern.search(line)
        if date is not None:
            add_date(dist, date.group('year'))

    plt.xlabel('Year')
    plt.ylabel('Nª of processes')

    plt.bar(list(dist.keys()), list(dist.values()))

    plt.show()


if __name__ == "__main__":
    main()

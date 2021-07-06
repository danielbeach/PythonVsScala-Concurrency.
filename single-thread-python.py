import csv
from glob import glob
from datetime import datetime


def main():
    files = gather_files()
    for file in files:
        rows = read_file(file)
        for row in rows:
            filter_row(row)


def gather_files(loc: str = 'trips/*.csv') -> iter:
    files = glob(loc)
    for file in files:
        yield file


def read_file(file_location: str) -> iter:
    with open(file_location, 'r') as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            yield row


def filter_row(row: object) -> None:
    if row[12] == 'member':
        print('member ride found')


if __name__ == '__main__':
    t1 = datetime.now()
    main()
    t2 = datetime.now()
    x = t2-t1
    print(f'It took {x} to process files')

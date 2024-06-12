from collections import Counter
from functools import lru_cache
import argparse
from pathlib import Path


@lru_cache
def count_single_char(sequence: str) -> int:
    if not isinstance(sequence, str):
        raise TypeError("Only str type is allowed")
    return sum(item for item in Counter(sequence).values() if item == 1)


def read_data_from_file(filepath: Path | str) -> str:
    filepath = Path(filepath)
    with open(filepath, 'r') as file:
        return file.read().strip()


def main():
    parser = argparse.ArgumentParser(
        description='Count single char in sequence')
    parser.add_argument(
        '--string',
        type=str,
        help='The string to be processed')
    parser.add_argument(
        '--file',
        type=str,
        help='The path to the file containing the string to be processed')
    args = parser.parse_args()
    if not args.string and not args.file:
        parser.error("One of --string or --file must be present")

    text = read_data_from_file(args.file) if args.file else args.string
    print(count_single_char(text))


if __name__ == '__main__':
    main()

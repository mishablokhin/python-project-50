import argparse
from gendiff import generate_diff


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help='path to first file')
    parser.add_argument('second_file', help='path to second file')
    parser.add_argument('-f', '--format', choices=['stylish', 'plain', 'json'],
                        default='stylish', help='set format of output')
    return parser.parse_args()


def main():
    args = parse_arguments()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()

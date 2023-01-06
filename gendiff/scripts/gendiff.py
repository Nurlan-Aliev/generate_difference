import argparse
from gendiff.generate import generate_diff
from gendiff.formarter.stylish import stylish
from gendiff.formarter.plain import plain


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)

parser.add_argument('-f', '--format', metavar='',
                    default=stylish, help='output format (default: "stylish")')


args = parser.parse_args()


def main():
    if args.format == 'plain':
        print(generate_diff(args.first_file, args.second_file, plain))
    else:
        print(generate_diff(args.first_file, args.second_file, stylish))


if __name__ == '__main__':
    main()

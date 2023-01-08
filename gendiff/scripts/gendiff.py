#!/usr/bin/env python3
import argparse
from gendiff.gendiff import generate_diff
from gendiff.formarter.stylish import stylish
from gendiff.formarter.plain import plain
from gendiff.formarter.json_formater import json_ as json


parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)

parser.add_argument('-f', '--format', metavar='',
                    choices=['stylish', 'plain', 'json'], default=stylish,
                    help='output format (default: "stylish")')


def main():
    args = parser.parse_args()
    if args.format == 'plain':
        print(generate_diff(args.first_file, args.second_file, plain))
    elif args.format == 'json':
        print(generate_diff(args.first_file, args.second_file, json))
    elif args.format == 'stylish' or args.format == stylish:
        print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()

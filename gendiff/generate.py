from gendiff.opening import open_file
import itertools


ADD = '  + '
RM = '  - '
NOT_CHANGE = '    '
LVL = 1
DEPTH_LINE = '    '


def generate_diff(first_file, second_file):
    open_first = open_file(first_file)
    open_second = open_file(second_file)
    return stylish(difference(open_first, open_second))


def value_to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


def check(value, value2=None):
    if value2 is None:
        value2 = value
    if isinstance(value, dict):
        return difference(value, value2)
    else:
        return value_to_str(value)


def difference(dict_1, dict_2) -> list:

    list_keys = list(dict_1.keys() | dict_2.keys())
    list_keys.sort()
    result = []
    for key in list_keys:
        value_1 = dict_1.get(key)
        value_2 = dict_2.get(key)

        if key not in dict_1:
            result.append((key, ADD, check(value_2)))

        elif key not in dict_2:
            result.append((key, RM, check(value_1)))

        else:
            if value_1 == value_2 or \
                    isinstance(value_1, dict) and isinstance(value_2, dict):
                result.append((key, NOT_CHANGE, check(value_1, value_2)))

            else:
                result.append((key, RM, check(value_1)))
                result.append((key, ADD, check(value_2)))

    return result


def stylish(tree) -> str:
    def inner_(node, depth):
        deep_indent_size = DEPTH_LINE * depth
        lists = []
        for index in node:
            name, status, value = index
            if isinstance(value, list):
                lists.append(f'{deep_indent_size}{status}{name}:'
                             f' {inner_(value, depth + LVL)}')
            else:
                lists.append(f'{deep_indent_size}{status}{name}:'
                             f' {value_to_str(value)}')
        result = itertools.chain('{', lists, [deep_indent_size + '}'])
        return '\n'.join(result)

    return inner_(tree, 0)

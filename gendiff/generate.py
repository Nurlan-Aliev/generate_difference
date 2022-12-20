import json


def gen_diff(first_file, second_file):
    open_first = json.load(open(first_file))
    open_second = json.load(open(second_file))
    all_keys = open_first.keys() | open_second.keys()
    list_keys = list(all_keys)
    list_keys.sort()
    result = '{\n'
    for key in list_keys:
        if key not in open_first.keys():
            result += f'  + {key}: {bool_to_str(open_second[key])}\n'
        elif key not in open_second:
            result += f'  - {key}: {bool_to_str(open_first[key])}\n'
        elif open_first[key] != open_second[key]:
            result += f'  - {key}: {bool_to_str(open_first[key])}\n' \
                      f'  + {key}: {bool_to_str(open_second[key])}\n'
        else:
            result += f'    {key}: {bool_to_str(open_first[key])}\n'
    result += '}'
    return result


def bool_to_str(value) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    return value


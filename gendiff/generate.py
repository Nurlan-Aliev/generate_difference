from gendiff.opening import open_file


def generate_diff(first_file, second_file):
    open_first = open_file(first_file)
    open_second = open_file(second_file)
    list_keys = list(open_first.keys() | open_second.keys())
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

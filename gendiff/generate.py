from gendiff.opening import open_file


ADD = 'added'
RM = 'removed'
NOT_CHANGE = 'not_change'
UPDATE = 'updated'


def generate_diff(first_file, second_file, style):
    open_first = open_file(first_file)
    open_second = open_file(second_file)
    diff = difference(open_first, open_second)
    result = style(diff)
    return result


# Перевод None в null, bool в str
def value_to_str(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


# Расскрытие словарей
def check(value, value2=None):
    if value2 is None:
        value2 = value
    if isinstance(value, dict):
        return difference(value, value2)
    else:
        return value_to_str(value)


# Вычеслитель различий
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
                result.append((key, UPDATE, (check(value_1), check(value_2))))

    return result

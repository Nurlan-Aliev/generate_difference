from gendiff.opening import open_file
from gendiff.formarter.stylish import stylish
from gendiff.formarter.plain import plain
from gendiff.formarter.json_formater import json_

ADD = 'added'
RM = 'removed'
NOT_CHANGE = 'not_change'
UPDATE = 'updated'
STATUS = 'status'
VALUE = 'value'


def generate_diff(first_file, second_file, style='stylish'):
    open_first = open_file(first_file)
    open_second = open_file(second_file)
    diff = difference(open_first, open_second)
    if style == 'plain':
        return plain(diff)
    elif style == 'json':
        return json_(diff)
    elif style == 'stylish':
        return stylish(diff)


# Расскрытие словарей
def check(value, value2=None):

    if is_dict(value):
        if value2 is None:
            value2 = value
        return difference(value, value2)

    else:
        return value


def is_dict(items):
    return isinstance(items, dict)


# Вычеслитель различий
def difference(dict_1, dict_2) -> list:

    list_keys = list(dict_1.keys() | dict_2.keys())
    list_keys.sort()
    result = []

    for key in list_keys:

        value_1 = dict_1.get(key)
        value_2 = dict_2.get(key)

        if key not in dict_1:
            result.append({key: {STATUS: ADD, VALUE: check(value_2)}})

        elif key not in dict_2:
            result.append({key: {STATUS: RM, VALUE: check(value_1)}})

        elif value_1 == value_2 or is_dict(value_1) and is_dict(value_2):
            result.append({key: {STATUS: NOT_CHANGE,
                                 VALUE: check(value_1, value_2)}})

        else:
            result.append({key: {STATUS: UPDATE,
                                 VALUE: (check(value_1), check(value_2))}})

    return result

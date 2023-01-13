from gendiff.utils import open_file
from gendiff.formarter.stylish import stylish
from gendiff.formarter.plain import plain
from gendiff.formarter.json_formater import json_

ADD = 'added'
RM = 'removed'
NOT_CHANGE = 'not_changed'
UPDATE = 'updated'
STATUS = 'status'
VALUE = 'value'


def generate_diff(first_file, second_file, style='stylish'):
    open_first = open_file(first_file)
    open_second = open_file(second_file)
    diff = build_base(open_first, open_second)
    if style == 'plain':
        return plain(diff)
    elif style == 'json':
        return json_(diff)
    elif style == 'stylish':
        return stylish(diff)


def check(value_1, value_2=None):
    """Returns the difference function with the received value
    if the value1  is a dictionary. Otherwise returns a value.
    """
    if is_dict(value_1):
        if value_2 is None:
            value_2 = value_1
        return build_base(value_1, value_2)

    else:
        return value_1


def is_dict(items):
    """Сhecks if an element is a dictionary"""
    return isinstance(items, dict)


def build_base(dict_1: dict, dict_2) -> list:
    """Return a list of dictionaries with key, difference status and value"""
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

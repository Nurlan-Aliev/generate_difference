from gendiff.utils import parse_content, read_file
from gendiff.formarter.stylish import stylish
from gendiff.formarter.plain import plain
from gendiff.formarter.json_formater import json

ADD = 'added'
RM = 'removed'
NOT_CHANGE = 'not_changed'
UPDATE = 'updated'
STATUS = 'status'
VALUE = 'value'
PARENT = 'nested'


def generate_diff(first_file, second_file, style='stylish'):
    file_content_1, file_type_1 = read_file(first_file)
    file_content_2, file_type_2 = read_file(second_file)
    dict_1 = parse_content(file_content_1, file_type_1)
    dict_2 = parse_content(file_content_2, file_type_2)
    diff = build_base(dict_1, dict_2)

    if style == 'plain':
        return plain(diff)

    elif style == 'json':
        return json(diff)

    elif style == 'stylish':
        return stylish(diff)


def check(value_1, value_2=None):
    """
    Returns the difference function with the received value
    if the value1  is a dictionary. Otherwise returns a value.
    """
    if is_dict(value_1):
        if value_2 is None:
            value_2 = value_1
        return build_base(value_1, value_2)

    else:
        return value_1


def is_dict(items_1, items_2=None):
    """Сhecks if an element is a dictionary"""
    if items_2 is None:
        return isinstance(items_1, dict)
    return isinstance(items_1, dict) and isinstance(items_2, dict)


def build_base(dict_1: dict, dict_2: dict) -> list:
    """Return a list of dictionaries with key, difference status and value"""
    list_keys = sorted(list(dict_1.keys() | dict_2.keys()))
    result = []

    for key in list_keys:
        result.append(find_key(key, dict_1, dict_2))
    return result


def find_key(key, dict_1, dict_2):
    value_1 = dict_1.get(key)
    value_2 = dict_2.get(key)

    if key not in dict_1:
        return {key: {STATUS: ADD, VALUE: check(value_2)}}

    elif key not in dict_2:
        return {key: {STATUS: RM, VALUE: check(value_1)}}

    elif value_1 == value_2:
        return {key: {STATUS: NOT_CHANGE, VALUE: check(value_1, value_2)}}

    elif is_dict(value_1, value_2):
        return {key: {STATUS: PARENT, VALUE: check(value_1, value_2)}}

    else:
        return {key: {STATUS: UPDATE, VALUE: (check(value_1), check(value_2))}}

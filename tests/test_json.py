from gendiff.formarter.json_formater import json_
from gendiff.gendiff import generate_diff


first_json = 'tests/fixtures/filepath1.json'
second_json = 'tests/fixtures/filepath2.json'


def test_json_():
    file_for_test = open('tests/fixtures/file_to_test_json.json', 'r')

    assert generate_diff(first_json, second_json, json_) == file_for_test.read()
    file_for_test.close()

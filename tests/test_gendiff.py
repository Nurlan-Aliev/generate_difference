from gendiff.gendiff import generate_diff
import pytest


def result_stylish():
    with open('tests/fixtures/result_stylish.txt', 'r') as file_for_test:
        return file_for_test.read()


def result_plain():
    with open('tests/fixtures/result_plain.txt', 'r') as file_for_test:
        return file_for_test.read()


def result_json():
    with open('tests/fixtures/result_json.json', 'r') as file_for_test:
        return file_for_test.read()


STYLISH = ('stylish', result_stylish)
PLAIN = ('plain', result_plain)
JSON = ('json', result_json)
PATH_1 = ('tests/fixtures/filepath1.json', 'tests/fixtures/yaml_file1.yml')
PATH_2 = ('tests/fixtures/filepath2.json', 'tests/fixtures/yaml_file2.yaml')


@pytest.mark.parametrize('first', PATH_1)
@pytest.mark.parametrize('second', PATH_2)
@pytest.mark.parametrize('formate,result', [STYLISH, PLAIN, JSON])
def test_case(first, second, formate, result):
    assert generate_diff(first, second, formate) == result()

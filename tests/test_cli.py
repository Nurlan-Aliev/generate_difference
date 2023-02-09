from gendiff.cli import cli
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


first = 'tests/fixtures/filepath1.json'
second = 'tests/fixtures/filepath2.json'
STYLISH = ('stylish', result_stylish)
PLAIN = ('plain', result_plain)
JSON = ('json', result_json)


@pytest.mark.parametrize('formate,result', [STYLISH, PLAIN, JSON])
def test_cli(formate, result):
    assert cli([first, second, '-f', formate]) == result()


if __name__ == '__main__':
    test_cli()

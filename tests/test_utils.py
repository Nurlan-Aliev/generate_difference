from gendiff.utils import parse_content, read_file
import pytest


def free():
    return {}


def coll():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False}


JSON = 'tests/fixtures/file1.json', coll
YAML = 'tests/fixtures/first_file.yaml', coll
FREE_FILE = 'tests/fixtures/free.json', free


@pytest.mark.parametrize('file_path,result', [JSON, YAML, FREE_FILE])
def test_parse_content(file_path, result):
    content, type_file = read_file(file_path)
    assert parse_content(content, type_file) == result()


if __name__ == '__main__':
    test_parse_content()

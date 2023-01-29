from gendiff.utils import parse_content, read_file
import pytest


@pytest.fixture
def coll():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False}


def test_parse_content(coll):
    content_json, type_file_json = read_file('tests/fixtures/file1.json')
    assert parse_content(content_json, type_file_json) == coll
    content_yaml, type_file_yaml = read_file('tests/fixtures/first_file.yaml')
    assert parse_content(content_yaml, type_file_yaml) == coll
    content_free, type_file_free = read_file('tests/fixtures/free.json')
    assert parse_content(content_free, type_file_free) == {}


if __name__ == '__main__':
    test_parse_content()

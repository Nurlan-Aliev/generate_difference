from gendiff.utils import parse_content, read_file
import pytest


JSON = 'tests/fixtures/file1.json'
YAML = 'tests/fixtures/first_file.yaml'
# FREE_FILE = 'tests/fixtures/free.json'


@pytest.fixture
def free():
    return {}


@pytest.fixture
def coll():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False}


@pytest.mark.parametrize('file_path', [JSON, YAML])
def test_parse_content(file_path, coll):
    content_json, type_file_json = read_file(file_path)
    assert parse_content(content_json, type_file_json) == coll


if __name__ == '__main__':
    test_parse_content()

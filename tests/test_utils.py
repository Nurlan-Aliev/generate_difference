from gendiff.utils import parse_content
import pytest


@pytest.fixture
def coll():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False}


def test_parse_content(coll):
    assert parse_content('tests/fixtures/file1.json') == coll

    assert parse_content('tests/fixtures/first_file.yaml') == coll

    assert parse_content('tests/fixtures/free.json') == {}


if __name__ == '__main__':
    test_parse_content()

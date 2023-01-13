from gendiff.utils import open_file
import pytest


@pytest.fixture
def coll():
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False}


def test_open_file(coll):
    assert open_file('tests/fixtures/file1.json') == coll

    assert open_file('tests/fixtures/first_file.yaml') == coll

    assert open_file('tests/fixtures/free.json') == {}


if __name__ == '__main__':
    test_open_file()

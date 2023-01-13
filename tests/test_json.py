from gendiff.gendiff import generate_diff
import pytest


@pytest.fixture
def file_read():
    with open('tests/fixtures/file_to_test_json.json', 'r') as file_for_test:
        return file_for_test.read()


def test_json_(file_read):
    first_json = 'tests/fixtures/filepath1.json'
    second_json = 'tests/fixtures/filepath2.json'
    first_yaml = 'tests/fixtures/yaml_file1.yaml'
    second_yaml = 'tests/fixtures/yaml_file2.yaml'
    assert generate_diff(first_json, second_json, 'json') == file_read
    assert generate_diff(first_yaml, second_yaml, 'json') == file_read

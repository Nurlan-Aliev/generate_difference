from gendiff.gendiff import generate_diff
import pytest


@pytest.fixture
def file_read():
    with open('tests/fixtures/file_to_test_json.json', 'r') as file_for_test:
        return file_for_test.read()


json = ('tests/fixtures/filepath1.json', 'tests/fixtures/filepath2.json')
yaml = ('tests/fixtures/yaml_file1.yml', 'tests/fixtures/yaml_file2.yaml')


@pytest.mark.parametrize('first,second', [json, yaml])
def test_json_(first, second, file_read):
    assert generate_diff(first, second, 'json') == file_read

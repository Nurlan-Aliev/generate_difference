from gendiff.gendiff import generate_diff
import pytest


@pytest.fixture
def result_tree():
    with open('tests/fixtures/result_plain.txt', 'r') as file_for_test:
        return file_for_test.read()


json = ('tests/fixtures/filepath1.json', 'tests/fixtures/filepath2.json')
yaml = ('tests/fixtures/yaml_file1.yml', 'tests/fixtures/yaml_file2.yaml')


@pytest.mark.parametrize('first,second', [json, yaml])
def test_plain(first, second, result_tree):
    assert generate_diff(first, second, 'plain') == result_tree


if __name__ == '__main__':
    test_plain()

from gendiff.gendiff import generate_diff
import pytest


@pytest.fixture
def result_stylish():
    with open('tests/fixtures/result_stylish.txt', 'r') as file_for_test:
        return file_for_test.read()


@pytest.fixture
def result_plain():
    with open('tests/fixtures/result_plain.txt', 'r') as file_for_test:
        return file_for_test.read()


@pytest.fixture
def result_json():
    with open('tests/fixtures/result_json.json', 'r') as file_for_test:
        return file_for_test.read()


json = ('tests/fixtures/filepath1.json', 'tests/fixtures/filepath2.json')
yaml = ('tests/fixtures/yaml_file1.yml', 'tests/fixtures/yaml_file2.yaml')
json_yaml = ('tests/fixtures/filepath1.json', 'tests/fixtures/yaml_file2.yaml')


@pytest.mark.parametrize('first,second', [json, yaml, json_yaml])
def test_stylish(first, second, result_stylish):
    assert generate_diff(first, second, 'stylish') == result_stylish


@pytest.mark.parametrize('first,second', [json, yaml, json_yaml])
def test_plain(first, second, result_plain):
    assert generate_diff(first, second, 'plain') == result_plain


@pytest.mark.parametrize('first,second', [json, yaml, json_yaml])
def test_json_(first, second, result_json):
    assert generate_diff(first, second, 'json') == result_json


if __name__ == '__main__':
    test_stylish()
    test_plain()
    test_json_()

from gendiff.gendiff import generate_diff


first_json = 'tests/fixtures/filepath1.json'
second_json = 'tests/fixtures/filepath2.json'
first_yaml = 'tests/fixtures/yaml_file1.yaml'
second_yaml = 'tests/fixtures/yaml_file2.yaml'


def test_json_():
    file_for_test = open('tests/fixtures/file_to_test_json.json', 'r')

    assert generate_diff(first_json, second_json, 'json') == file_for_test.read()
    file_for_test.close()

    file_for_test = open('tests/fixtures/file_to_test_json.json', 'r')
    assert generate_diff(first_yaml, second_yaml, 'json') == file_for_test.read()
    file_for_test.close()

from gendiff.gendiff import generate_diff


first_json = 'tests/fixtures/file1.json'
second_json = 'tests/fixtures/file2.json'
first_yaml = 'tests/fixtures/first_file.yaml'
second_yaml = 'tests/fixtures/second_file.yaml'
free_json = 'tests/fixtures/free.json'
result = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

first_tree_json = 'tests/fixtures/filepath1.json'
second_tree_json = 'tests/fixtures/filepath2.json'
first_tree_yaml = 'tests/fixtures/yaml_file1.yaml'
second_tree_yaml = 'tests/fixtures/yaml_file2.yaml'
file_for_test = open('tests/fixtures/result.txt', 'r')
result_tree = file_for_test.read()


def test_generate_diff():
    assert generate_diff(first_json, second_json, 'stylish') == result
    assert generate_diff(first_yaml, second_yaml, 'stylish') == result
    assert generate_diff(first_json, second_yaml, 'stylish') == result
    assert generate_diff(free_json, second_json, 'stylish') == '''{
  + host: hexlet.io
  + timeout: 20
  + verbose: true
}'''

    assert generate_diff(first_json, free_json, 'stylish') == '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''
    assert generate_diff(first_tree_json, second_tree_json) == result_tree
    assert generate_diff(first_tree_yaml, second_tree_yaml) == result_tree
    assert generate_diff(first_tree_json, second_tree_yaml) == result_tree


if __name__ == '__main__':
    test_generate_diff()

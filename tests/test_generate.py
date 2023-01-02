from gendiff.generate import generate_diff


first_json = 'tests/fixtures/file1.json'
second_json = 'tests/fixtures/file2.json'
first_yaml = 'tests/fixtures/first_file.yaml'
second_yaml = 'tests/fixtures/second_file.yaml'
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
result_tree = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


def test_generate_diff():
    assert generate_diff(first_json, second_json) == result
    assert generate_diff(first_yaml, second_yaml) == result
    assert generate_diff(first_json, second_yaml) == result
    assert generate_diff('tests/fixtures/free.json', second_json) == '''{
  + host: hexlet.io
  + timeout: 20
  + verbose: true
}'''

    assert generate_diff(first_json, 'tests/fixtures/free.json') == '''{
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

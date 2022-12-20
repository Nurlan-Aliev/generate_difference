from gendiff.generate import generate_diff


def test_generate_diff():
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


if __name__ == '__main__':
    test_generate_diff()

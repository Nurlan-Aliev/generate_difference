from gendiff.generate import generate_diff


def test_generate_diff():
    assert generate_diff(
    'tests/fixtures/file1.json', 'tests/fixtures/file2.json') == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert generate_diff(
            'tests/fixtures/free.json', 'tests/fixtures/file2.json') == '''{
  + host: hexlet.io
  + timeout: 20
  + verbose: true
}'''
    assert generate_diff(
    'tests/fixtures/file1.json', 'tests/fixtures/free.json') == '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''


if __name__ == '__main__':
    test_generate_diff()

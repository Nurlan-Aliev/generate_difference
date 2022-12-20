from gendiff.opening import open_file


def test_open_file():
    assert open_file('tests/fixtures/file1.json') == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False}

    assert open_file('tests/fixtures/first_file.yaml') == {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False}

    assert open_file('tests/fixtures/free.json') == {}


if __name__ == '__main__':
    test_open_file()

from gendiff.gendiff import generate_diff


first_json = 'tests/fixtures/filepath1.json'
second_json = 'tests/fixtures/filepath2.json'
first_yaml = 'tests/fixtures/yaml_file1.yaml'
second_yaml = 'tests/fixtures/yaml_file2.yaml'

result_tree = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''


def test_plain():
    assert generate_diff(first_json, second_json, 'plain') == result_tree
    assert generate_diff(first_yaml, second_yaml, 'plain') == result_tree


if __name__ == '__main__':
    test_plain()

import itertools


DEPTH_LINE = '    '
LVL = 1
RM = '  - '
ADD = '  + '


# Стиль
def stylish(tree, depth=0) -> str:

    if not isinstance(tree, list):
        return tree

    deep_indent_size = DEPTH_LINE * depth
    lists = []

    for index in tree:
        for name in index:
            value = index[name]['VALUE']
            status = index[name]['STATUS']

            if status == 'updated':

                lists.append(f'{deep_indent_size}{RM}{name}:'
                             f' {stylish(to_str(value[0]), depth + LVL)}')
                lists.append(f'{deep_indent_size}{ADD}{name}:'
                             f' {stylish(to_str(value[1]), depth + LVL)}')

            else:
                lists.append(f'{deep_indent_size}{refactor(status)}{name}:'
                             f' {stylish(to_str(value), depth + LVL)}')

    result = itertools.chain('{', lists, [deep_indent_size + '}'])
    return '\n'.join(result)


def refactor(status):
    if status == 'added':
        return '  + '
    if status == 'removed':
        return '  - '
    if status == 'not_change':
        return '    '


# Перевод None в null, bool в str
def to_str(value):

    if isinstance(value, bool):
        return str(value).lower()

    elif value is None:
        return 'null'

    return value

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
        name, status, value = index

        if status == 'updated':

            lists.append(f'{deep_indent_size}{RM}{name}:'
                         f' {stylish(value[0], depth + LVL)}')
            lists.append(f'{deep_indent_size}{ADD}{name}:'
                         f' {stylish(value[1], depth + LVL)}')

        else:
            lists.append(f'{deep_indent_size}{refactor(status)}{name}:'
                         f' {stylish(value, depth + LVL)}')

    result = itertools.chain('{', lists, [deep_indent_size + '}'])
    return '\n'.join(result)


def refactor(status):
    if status == 'added':
        return '  + '
    if status == 'removed':
        return '  - '
    if status == 'not_change':
        return '    '

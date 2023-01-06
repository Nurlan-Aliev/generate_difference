import itertools


DEPTH_LINE = '    '
LVL = 1


# Стиль
def stylish(tree) -> str:

    def inner_(node, depth):

        if not isinstance(node, list):
            return node

        deep_indent_size = DEPTH_LINE * depth
        lists = []

        for index in node:
            name, status, value = index

            if isinstance(value, tuple):
                lists.append(f'{deep_indent_size}  - {name}:'
                             f' {inner_(value[0], depth + LVL)}')
                lists.append(f'{deep_indent_size}  + {name}:'
                             f' {inner_(value[1], depth + LVL)}')

            else:
                lists.append(f'{deep_indent_size}{refactor(status)}{name}:'
                             f' {inner_(value, depth + LVL)}')

        result = itertools.chain('{', lists, [deep_indent_size + '}'])
        return '\n'.join(result)

    return inner_(tree, 0)


def refactor(status):
    if status == 'added':
        return '  + '
    if status == 'removed':
        return '  - '
    if status == 'not_change':
        return '    '

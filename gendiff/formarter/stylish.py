import itertools


DEPTH_LINE = '    '
LVL = 1
RM = '  - '
ADD = '  + '


# Стиль
def stylish(tree, depth=0) -> str:

    if not isinstance(tree, list):
        return tree

    deep_size = DEPTH_LINE * depth
    lst = []

    for index in tree:
        for name in index:
            value = index[name]['value']
            status = index[name]['status']

            if status == 'updated':
                lst.append(f'{deep_size}{RM}{name}:'
                           f' {stylish(to_str(value[0]), depth + LVL)}')
                lst.append(f'{deep_size}{ADD}{name}:'
                           f' {stylish(to_str(value[1]), depth + LVL)}')

            else:
                lst.append(f'{deep_size}{refactor(status)}{name}:'
                           f' {stylish(to_str(value), depth + LVL)}')

    result = itertools.chain('{', lst, [deep_size + '}'])
    return '\n'.join(result)


def refactor(status):
    if status == 'added':
        return ADD
    if status == 'removed':
        return RM
    if status == 'not_change':
        return DEPTH_LINE


# Перевод None в null, bool в str
def to_str(value):

    if isinstance(value, bool):
        return str(value).lower()

    elif value is None:
        return 'null'

    return value

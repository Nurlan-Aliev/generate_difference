import itertools


DEPTH_LINE = '    '
LVL = 1
RM = '  - '
ADD = '  + '


def stylish(tree: list) -> str:

    def inner(node, depth=0):
        if not isinstance(node, list):
            return node

        deep_size = DEPTH_LINE * depth
        result = []

        for index in node:
            for name in index:
                value = index[name]['value']
                status = index[name]['status']

                if status == 'updated':
                    result.append(f'{deep_size}{RM}{name}:'
                                  f' {inner(make_str(value[0]), depth + LVL)}')
                    result.append(f'{deep_size}{ADD}{name}:'
                                  f' {inner(make_str(value[1]), depth + LVL)}')

                else:
                    result.append(f'{deep_size}{refactor(status)}{name}:'
                                  f' {inner(make_str(value), depth + LVL)}')

        return '\n'.join(itertools.chain('{', result, [deep_size + '}']))

    return inner(tree)


def refactor(status):
    if status == 'added':
        return ADD
    if status == 'removed':
        return RM
    if status == 'not_changed':
        return DEPTH_LINE


def make_str(value):
    """Casts None to null, bool to str"""
    if isinstance(value, bool):
        return str(value).lower()

    elif value is None:
        return 'null'

    return value

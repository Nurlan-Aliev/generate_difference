def plain(tree):
    result = build_way(tree, [])

    lst = []
    for i in result:
        name, status, value = i

        if status == 'added':
            lst.append(f"Property '{name}' "
                       f"was added with value: {list_to_complex(value)}")

        if status == 'removed':
            lst.append(f"Property '{name}' was removed")

        if status == 'updated':
            rm, add = value
            lst.append(f"Property '{name}' was updated. "
                       f"From {list_to_complex(rm)} to {list_to_complex(add)}")

    return '\n'.join(lst)


def list_to_complex(value):
    if isinstance(value, list):
        return '[complex value]'
    if value == 'true' or value == 'null' or value == 'false':
        return value
    return f"'{value}'"


def build_way(tree, list_way):
    lst = []

    for i in tree:
        name, status, value = i
        list_way.append(name)

        if status == 'not_change' and isinstance(value, list):
            lst.append(build_way(value, list_way))
            list_way.pop(-1)

        else:
            str_way = '.'.join(list_way)
            list_way.pop(-1)
            lst.append((str_way, status, value))

    return flatten(lst)


def normalize(item):
    return flatten(item) if isinstance(item, list) else [item]


def flatten(tree):
    return sum(map(normalize, tree), [])

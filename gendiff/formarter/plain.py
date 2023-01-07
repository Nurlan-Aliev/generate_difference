from gendiff.formarter.stylish import to_str


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
    if is_list(value):
        return '[complex value]'
    if isinstance(value, bool) or value is None:
        return to_str(value)
    return f"'{value}'"


def build_way(tree, list_way):
    lst = []

    for index in tree:
        for name in index:
            list_way.append(name)
            value = index[name]['VALUE']
            status = index[name]['STATUS']

            if status == 'not_change' and is_list(value):
                lst.append(build_way(value, list_way))
                list_way.pop(-1)

            else:
                str_way = '.'.join(list_way)
                list_way.pop(-1)
                lst.append((str_way, status, value))

    return flatten(lst)


def normalize(item):
    return flatten(item) if is_list(item) else [item]


def flatten(tree):
    return sum(map(normalize, tree), [])


def is_list(value):
    return isinstance(value, list)

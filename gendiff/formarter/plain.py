from gendiff.formarter.stylish import make_str


def plain(tree: list) -> str:
    result = build_way(tree, [])

    lst = []
    for i in result:
        name, status, value = i

        if status == 'added':
            lst.append(f"Property '{name}' "
                       f"was added with value: {check_type(value)}")

        if status == 'removed':
            lst.append(f"Property '{name}' was removed")

        if status == 'updated':
            rm, add = value
            lst.append(f"Property '{name}' was updated. "
                       f'From {check_type(rm)} to {check_type(add)}')

    return '\n'.join(lst)


def check_type(value):
    if is_list(value):
        return '[complex value]'

    if isinstance(value, (bool, int)) or value is None:
        return make_str(value)

    return f"'{value}'"


def build_way(tree, list_path):
    lst = []

    for index in tree:
        name = list(index.keys())[0]
        list_path.append(name)
        value = index[name]['value']
        status = index[name]['status']

        if status == 'not_changed' and is_list(value):
            lst.append(build_way(value, list_path))
            list_path.pop(-1)

        else:
            str_way = '.'.join(list_path)
            list_path.pop(-1)
            lst.append((str_way, status, value))

    return flatten(lst)


def normalize(item):
    return flatten(item) if is_list(item) else [item]


def flatten(tree):
    return sum(map(normalize, tree), [])


def is_list(value):
    return isinstance(value, list)

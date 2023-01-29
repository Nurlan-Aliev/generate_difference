from gendiff.formarter.stylish import make_str


def plain(tree: list) -> str:
    path = build_path(tree, [])

    result = []
    for element in path:
        name, status, value = element

        if status == 'added':
            result.append(f"Property '{name}' "
                          f"was added with value: {check_type(value)}")

        if status == 'removed':
            result.append(f"Property '{name}' was removed")

        if status == 'updated':
            rm, add = value
            result.append(f"Property '{name}' was updated. "
                          f"From {check_type(rm)} to {check_type(add)}")

    return '\n'.join(result)


def check_type(value):
    if is_list(value):
        return '[complex value]'

    if isinstance(value, (bool, int)) or value is None:
        return make_str(value)

    return f"'{value}'"


def build_path(tree, list_path):
    result = []

    for index in tree:
        name = list(index.keys())[0]
        list_path.append(name)
        value = index[name]['value']
        status = index[name]['status']

        if status == 'nested':
            result.append(build_path(value, list_path))
            list_path.pop(-1)

        else:
            str_way = '.'.join(list_path)
            list_path.pop(-1)
            result.append((str_way, status, value))

    return flatten(result)


def normalize(item):
    return flatten(item) if is_list(item) else [item]


def flatten(tree):
    return sum(map(normalize, tree), [])


def is_list(value):
    return isinstance(value, list)

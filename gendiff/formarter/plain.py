from gendiff.make_str import make_str


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
    if isinstance(value, list):
        return '[complex value]'

    if isinstance(value, (bool, int)) or value is None:
        return make_str(value)

    return f"'{value}'"


def build_path(tree, paths):
    result = []

    for index in tree:
        name = list(index.keys())[0]
        paths.append(name)
        value = index[name]['value']
        status = index[name]['status']

        if status == 'nested':
            result.append(build_path(value, paths))
            paths.pop(-1)

        else:
            str_path = '.'.join(paths)
            paths.pop(-1)
            result.append((str_path, status, value))

    return flatten(result)


def normalize(item):
    return flatten(item) if isinstance(item, list) else [item]


def flatten(tree):
    return sum(map(normalize, tree), [])

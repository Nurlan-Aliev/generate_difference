import json


def make_json(tree) -> json:
    return json.dumps(tree, indent=2)

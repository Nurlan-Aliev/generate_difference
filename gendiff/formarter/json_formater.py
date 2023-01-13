import json


def json_(tree) -> json:
    return json.dumps(tree, indent=2)

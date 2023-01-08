import json


def json_(lst) -> json:
    return json.dumps(lst, indent=2)

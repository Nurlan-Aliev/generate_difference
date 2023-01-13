import yaml
import json


def open_file(file1):
    if file1.endswith('.json'):
        with open(file1, "r") as input_file:
            return json.load(input_file)

    if file1.endswith('.yaml') or file1.endswith('.yml'):
        return yaml.safe_load(open(file1))

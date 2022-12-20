import yaml
import json


def open_file(file1):
    if file1.endswith('.json'):
        return json.load(open(file1))
    if file1.endswith('.yaml') or file1.endswith('.yml'):
        return yaml.safe_load(open(file1))

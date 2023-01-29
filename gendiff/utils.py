import yaml
import json
import os


def read_file(file_path):
    _, file_type = os.path.splitext(file_path)

    with open(file_path, "r") as output_file:
        content = output_file.read()
    return content, file_type


def parse_content(content, file_type):

    if file_type == '.json':
        return json.loads(content)

    if file_type == '.yaml' or '.yml':
        return yaml.safe_load(content)

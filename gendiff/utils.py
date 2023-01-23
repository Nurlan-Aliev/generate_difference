import yaml
import json
import os


def read_file(file_path):
    with open(file_path, "r") as output_file:
        return output_file.read()


def parse_content(content):
    content = read_file(content)
    format = os.path.splitext(content)[1]
    if format == '.json':
        return json.load(content)

    if format == '.yaml' or '.yml':
        return yaml.safe_load(content)

import yaml
import json
import os


def read_file(file_path):
    with open(file_path, "r") as output_file:
        content = output_file.read()
    return content


def get_format(file_path):
    _, formate_file = os.path.splitext(file_path)
    return formate_file


def parse_content(content, file_type):

    if file_type == '.json':
        return json.loads(content)

    if file_type == '.yaml' or '.yml':
        return yaml.safe_load(content)


def open_file(file_path):
    file_content = read_file(file_path)
    file_format = get_format(file_path)
    content = parse_content(file_content, file_format)
    return content

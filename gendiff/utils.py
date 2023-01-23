import yaml
import json
import os


def read_file(file_path):
    return open(file_path, "r")


def parse_content(path):
    format = os.path.splitext(path)[1]
    contend = read_file(path)
    if format == '.json':
        return json.load(contend)

    if format == '.yaml' or '.yml':
        return yaml.safe_load(contend)

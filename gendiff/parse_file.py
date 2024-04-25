import json
import yaml
import os


def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def parse_content(content, format_name):
    if format_name in ['yaml', 'yml']:
        return yaml.safe_load(content)
    elif format_name == 'json':
        return json.loads(content)
    else:
        raise ValueError(f"Unsupported format: {format_name}")


def get_content(file_path):
    content = read_file_content(file_path)
    format_name = os.path.splitext(file_path)[1][1:]
    return parse_content(content, format_name)

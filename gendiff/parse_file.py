import json
import yaml


def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def parse_content(content, file_path):
    if file_path.endswith(('.yaml', '.yml')):
        return yaml.safe_load(content)
    elif file_path.endswith('.json'):
        return json.loads(content)


def read_data_file(file_path):
    content = read_file_content(file_path)
    return parse_content(content, file_path)

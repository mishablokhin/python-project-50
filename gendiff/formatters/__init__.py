from . import plain, json, stylish


def get_formatter(format_name):
    if format_name == 'plain':
        return plain.plain
    elif format_name == 'json':
        return json.json_format
    return stylish.stylish

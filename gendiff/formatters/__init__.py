from .stylish import stylish
from .plain import plain
from .json import json_format


def format_diff(diff, format_name='stylish'):
    if format_name == 'plain':
        return plain(diff)
    elif format_name == 'json':
        return json_format(diff)
    return stylish(diff)

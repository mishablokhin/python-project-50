from .stylish import stylish
from .plain import plain


def get_formatter(format_name):
    if format_name == 'plain':
        return plain
    return stylish

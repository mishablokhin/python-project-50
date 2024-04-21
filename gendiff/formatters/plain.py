def plain(diff, path=''):
    lines = []
    for key, node in sorted(diff.items()):
        full_key = f"{path}.{key}" if path else key
        if node['type'] == 'nested':
            lines.append(plain(node['children'], full_key))
        elif node['type'] == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{full_key}' was added with value: {value}")
        elif node['type'] == 'removed':
            lines.append(f"Property '{full_key}' was removed")
        elif node['type'] == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            update_message = (f"Property '{full_key}' was updated. From "
                              f"{old_value} to {new_value}")
            lines.append(update_message)
    return '\n'.join(filter(None, lines))


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)

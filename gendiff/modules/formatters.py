def stylish(diff, depth=0):
    indent = '    ' * depth
    lines = ['{']
    for key, node in sorted(diff.items()):
        formatted = format_node(node, key, depth, indent)
        lines.extend(formatted)
    lines.append(indent + '}')
    return '\n'.join(lines)


def format_node(node, key, depth, indent):
    line = []
    key_indent = f"{indent}    {key}: "
    if node['type'] == 'nested':
        nested_formatted = stylish(node['children'], depth + 1)
        line.append(f"{key_indent}{nested_formatted}")
    elif node['type'] == 'unchanged':
        line.append(f"{key_indent}{format_value(node['value'], depth + 1)}")
    else:
        line.extend(format_change(node, key, depth, indent))
    return line


def format_change(node, key, depth, indent):
    lines = []
    if node['type'] in ['added', 'removed']:
        sign = '+' if node['type'] == 'added' else '-'
        value_formatted = format_value(node['value'], depth + 1)
        lines.append(f"{indent}  {sign} {key}: {value_formatted}")
    elif node['type'] == 'changed':
        old_value_formatted = format_value(node['old_value'], depth + 1)
        new_value_formatted = format_value(node['new_value'], depth + 1)
        lines.append(f"{indent}  - {key}: {old_value_formatted}")
        lines.append(f"{indent}  + {key}: {new_value_formatted}")
    return lines


def format_nested_dict(value, depth):
    indent = '    ' * depth
    deeper_indent = '    ' * (depth + 1)
    lines = ['{']
    for key, val in sorted(value.items()):
        formatted_value = format_value(val, depth + 1)
        lines.append(f"{deeper_indent}{key}: {formatted_value}")
    lines.append(indent + '}')
    return '\n'.join(lines)


def format_value(value, depth):
    if isinstance(value, dict):
        return format_nested_dict(value, depth)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)

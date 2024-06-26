INDENT = '    '


def stylish(diff, depth=0):
    indent = INDENT * depth
    lines = ['{']
    for key, node in sorted(diff.items()):
        formatted = format_node(node, key, depth, indent)
        lines.extend(formatted)
    lines.append(indent + '}')
    return '\n'.join(lines)


def format_node(node, key, depth, indent):
    lines = []
    key_indent = indent + INDENT + f"{key}: "
    if node['type'] == 'nested':
        nested_formatted = stylish(node['children'], depth + 1)
        lines.append(f"{key_indent}{nested_formatted}")
    elif node['type'] == 'unchanged':
        lines.append(f"{key_indent}{format_value(node['value'], depth + 1)}")
    else:
        lines.extend(format_change(node, key, depth, indent))
    return lines


def format_change(node, key, depth, indent):
    lines = []
    type_signs = {'added': '+', 'removed': '-'}
    if node['type'] in ['added', 'removed']:
        sign = type_signs[node['type']]
        value_formatted = format_value(node['value'], depth + 1)
        lines.append(f"{indent}  {sign} {key}: {value_formatted}")
    elif node['type'] == 'changed':
        old_value_formatted = format_value(node['old_value'], depth + 1)
        new_value_formatted = format_value(node['new_value'], depth + 1)
        line_old = f"{indent}  - {key}: {old_value_formatted}"
        line_new = f"{indent}  + {key}: {new_value_formatted}"
        lines.extend([line_old, line_new])
    return lines


def format_value(value, depth):
    if isinstance(value, dict):
        indent = INDENT * depth
        deeper_indent = indent + INDENT
        lines = ['{']
        for key, val in sorted(value.items()):
            formatted_value = format_value(val, depth + 1)
            lines.append(f"{deeper_indent}{key}: {formatted_value}")
        lines.append(indent + '}')
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    else:
        return str(value)

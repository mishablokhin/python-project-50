import json


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def generate_diff(file_path1, file_path2):
    dict1 = read_json_file(file_path1)
    dict2 = read_json_file(file_path2)

    all_dict_keys = sorted(set(dict1) | set(dict2))
    diffs = []
    for key in all_dict_keys:
        if key in dict1 and key not in dict2:
            diffs.append(f"  - {key}: {format_value(dict1[key])}")
        elif key not in dict1 and key in dict2:
            diffs.append(f"  + {key}: {format_value(dict2[key])}")
        elif dict1[key] != dict2[key]:
            diffs.append(f"  - {key}: {format_value(dict1[key])}")
            diffs.append(f"  + {key}: {format_value(dict2[key])}")
        else:
            diffs.append(f"    {key}: {format_value(dict1[key])}")

    return '{\n' + '\n'.join(diffs) + '\n}'

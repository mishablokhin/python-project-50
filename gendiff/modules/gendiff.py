import json


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(file_path1, file_path2):
    with open(file_path1, 'r') as file1, open(file_path2, 'r') as file2:
        dict1 = json.load(file1)
        dict2 = json.load(file2)

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

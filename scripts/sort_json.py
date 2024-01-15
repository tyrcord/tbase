import json
import os


def sort_json_keys(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Sort keys in dictionary
    sorted_data = {k: v for k, v in sorted(data.items())}

    with open(file_path, 'w') as f:
        json.dump(sorted_data, f, indent=2)

        # Add an empty line at the end of the file
        f.write('\n')


def check_json_files(directory):
    for entry in os.scandir(directory):
        if entry.is_file() and entry.name.endswith('.json'):
            file_path = entry.path
            sort_json_keys(file_path)
            print(f"Sorted keys in {file_path}")
        elif entry.is_dir():
            check_json_files(entry.path)


check_json_files('./')

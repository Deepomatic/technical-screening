# #!/usr/bin/env python3
import json


# -------------------------------------------------------------------------------------------------------------------- #


def open_json_from_file(json_path):
    """
    Loads a json from a file path.

    :param json_path: path to the json file
    :return: the loaded json
    """
    try:
        with open(json_path) as json_file:
            json_data = json.load(json_file)
    except Exception as e:
        print(f"Could not open file {json_path} in json format. {e}")
        raise

    return json_data


def save_json_to_file(json_data, json_path):
    """
    Saves a json to a file.

    :param json_data: the actual json
    :param json_path: path to the json file
    :return:
    """
    try:
        with open(json_path, 'w') as json_file:
            json.dump(json_data, json_file)
    except Exception as e:
        print(f"Could not save file {json_path} in json format. {e}")
        raise

    return


def pretty_print(inline_json):
    """
    Prints a json in the command interface in easily-readable format.

    :param inline_json:
    :return:
    """
    print(json.dumps(inline_json, indent=4, sort_keys=True))
    return


# -------------------------------------------------------------------------------------------------------------------- #


def merge_axle_trees(annotation):
    """
    Take an annotation and return an updated annotation with axle tree areas.

    :param annotation: annotation json without merged axle
    :return: annotation json with axle tree areas
    """

    # TODO: Implement !
    merged_annotation = annotation

    return merged_annotation


if __name__ == '__main__':
    # Load annotations from json file
    json_data = open_json_from_file('annotations.json')

    # Merge
    json_data = merge_axle_trees(json_data)
    pretty_print(json_data)

    # Saves new annotations to json file
    save_json_to_file(json_data, 'new_annotations.json')
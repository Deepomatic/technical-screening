# #!/usr/bin/env python3
import json
import random
import os

# --------------------------------------------------------------------------- #


def open_json_from_file(json_path):
    """
    Loads a json from a file path.

    :param json_path: path to the json file
    :return: the loaded json
    """
    try:
        with open(json_path) as json_file:
            json_data = json.load(json_file)
    except:
        print(f"Could not open file {json_path} in json format.")
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
    except:
        print(f"Could not save file {json_path} in json format.")
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

# --------------------------------------------------------------------------- #
def nms(proposals, IoU_treshold=0.5):
    """
    Take a list of proposal predictions, the IoU treshold,
    and returns the list of predictions selected after nms.

    :param proposals: the json containing the proposals
    :param IoU_trehsold: the IoU threshold used to evaluate
    :return: the list of predictions
    """
    result_list = []

    # TODO: implement !

    return result_list


if __name__ == '__main__':
    # Load annotations from json file
    groundtruth = open_json_from_file('groundtruth.json')
    proposals = open_json_from_file('proposals.json')

    # NMS
    for img in proposals['images']:
        # TODO: Do some stuff and compute predictions
        print(f"Image '{img['location']}'\n\t- TP: \n\t- FN: \n\t- FP: ")

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


# -------------------------------------------------------------------------------------------------------------------- #


def evaluate_images(annotations, predictions, threshold, Jaccard_min=0.5):
    """
    Take a list of annotations and predictions, a threshold, and returns the number of true positives, false positives,
    and false negatives.

    :param annotations: the json containing the annotations
    :param predictions: the json containing the predictions
    :param threshold: the threshold used to select the boxes to evaluate
    :param Jaccard_min: the IoU threshold used to evaluate
    :return: (true_positives, false_negatives, false_positives)
    """
    true_positives = 0
    false_negatives = 0
    false_positives = 0

    # TODO: implement !

    # Tips: you can use Polygon to compute boxes intersections, unions, etc.
    # cf https://shapely.readthedocs.io/en/latest/manual.html#geometric-objects

    return true_positives, false_negatives, false_positives


if __name__ == '__main__':
    # Load annotations from json file
    groundtruth = open_json_from_file('groundtruth.json')
    predictions = open_json_from_file('predictions.json')

    # Evaluate
    for img in groundtruth['images']:
        # TODO: Do some stuff and evaluate image
        print(f"Image '{img['location']}'\n\t- TP: \n\t- FN: \n\t- FP: ")
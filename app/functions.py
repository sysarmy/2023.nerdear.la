import csv


def convert_key_values_to_lowercase(dictionary_list, key):
    for item in dictionary_list:
        if key in item:
            item[key] = item[key].lower()


def csv_to_list_of_dicts(csv_file):
    data = []
    with open(csv_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

import csv
import json

# FIXME:
# I think the try except should be done in routes.py to display error pages or error messages with flash()


def convert_key_values_to_lowercase(dictionary_list, key):
    """
    Convert the values of a specified key in a list of dictionaries to lowercase.

    Args:
        dictionary_list (list): A list of dictionaries.
        key (str): The key whose values need to be converted to lowercase.

    Raises:
        KeyError: If the specified key is not found in any dictionary.
        TypeError: If an invalid dictionary is encountered in the list, or if the value associated with the key is not a string.
        Exception: If any other unexpected error occurs.

    Returns:
        None
    """
    try:
        for item in dictionary_list:
            if not isinstance(item, dict):
                raise TypeError("Invalid dictionary encountered in the list.")

            if key not in item:
                raise KeyError(f"Key '{key}' not found in dictionary.")

            value = item[key]
            if not isinstance(value, str):
                print(f"Value for key '{key}' is not a string.")
                continue

            item[key] = value.lower()
    except KeyError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def csv_to_list_of_dicts(csv_file_path):
    """
    Read a CSV file and convert its contents into a list of dictionaries.

    Args:
        csv_file_path (str): The path to the CSV file.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        IsADirectoryError: If the specified path points to a directory instead of a file.
        PermissionError: If there is a permission issue accessing the file.
        json.JSONDecodeError: If there is an error parsing the CSV file.
        Exception: If any other unexpected error occurs.

    Returns:
        list: A list of dictionaries representing the CSV data. Each dictionary corresponds to a row in the CSV file,
              with column names as keys and cell values as values.
    """
    try:
        data = []
        with open(csv_file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print(f"File not found: {csv_file_path}")
    except IsADirectoryError:
        print(f"Expected a file, but got a directory: {csv_file_path}")
    except PermissionError:
        print(f"Permission denied to access file: {csv_file_path}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_json_file(json_file_path):
    """
    Read a JSON file and load its contents into a dictionary.

    Args:
        json_file_path (str): The path to the JSON file.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        IsADirectoryError: If the specified path points to a directory instead of a file.
        PermissionError: If there is a permission issue accessing the file.
        json.JSONDecodeError: If there is an error parsing the JSON file.
        Exception: If any other unexpected error occurs.

    Returns:
        dict: A dictionary representing the JSON data loaded from the file.
    """
    try:
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
    except IsADirectoryError:
        print(f"Expected a file, but got a directory: {json_file_path}")
    except PermissionError:
        print(f"Permission denied to access file: {json_file_path}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def remove_trailing_whitespace(dictionary_list):
    """
    Removes initial and final trailing whitespaces from keys and values of each dictionary in a list.

    Args:
        dictionary_list (list): List of dictionaries.

    Returns:
        list: List of dictionaries with updated keys and values.
    """
    processed_list = []

    try:
        for dictionary in dictionary_list:
            processed_dict = {}

            for key, value in dictionary.items():
                try:
                    processed_key = (
                        key.strip()
                    )  # Remove trailing whitespaces from the key
                    processed_dict[processed_key] = value.strip()
                except AttributeError:
                    # Handle exception if key is not a string
                    print(f"Warning: Invalid key type encountered: {key}")

            processed_list.append(processed_dict)

    except TypeError:
        # Handle exception if dictionary_list is not iterable
        print("Error: Invalid input. Expected a list of dictionaries.")

    return processed_list

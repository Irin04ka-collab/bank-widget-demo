import json

from operation import Operation

def load_file():
    with open("../data/operations.json", "r") as file:
        data = json.load(file)

    operations = [Operation(data_row) for data_row in data]

    return operations

def sort_by_date():
    pass
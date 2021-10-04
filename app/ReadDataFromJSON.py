"""
Author: Asad Ali
Date: 2021-10-04 14:54:43
Description: Reads in an input json file with field length information and converts the input json file to fixed length
csv file
"""

import json


class Spec:
    def __init__(self, ColumnNames, Offsets, FixedWidthEncoding, IncludeHeader, DelimitedEncoding):
        self.columnNames = ColumnNames
        self.offsets = Offsets
        self.fixedWidthEncoding = FixedWidthEncoding
        self.includeHeader = IncludeHeader
        self.delimitedEncoding = DelimitedEncoding

    @classmethod
    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)


def get_length(offset):
    return int(column_names_offset[offset])


def get_data_record(value):
    record = ''
    for offset in column_names_offset:
        record += value[offset].ljust(get_length(offset)) + delimiter
    return record


def get_header():
    header_str = ''
    for value in column_names_offset:
        header_str += value.ljust(get_length(value)) + delimiter
    return header_str


def populate_column_names_offset():
    for i in range(len(spec.columnNames)):
        column_names_offset[spec.columnNames[i]] = spec.offsets[i]


def load_input_json_data():
    with open('input_data.json', 'r') as json_data_file:
        json_data_str = json_data_file.read()
    json_data = json.loads(json_data_str)


def load_json_spec_file():
    global spec
    with open('spec.json', 'r') as json_file:
        json_offset_file = json_file.read()
        spec = Spec.from_json(json_offset_file)


def write_output_csv_file():
    with open("output.csv", "w") as output_file:
        if bool(spec.includeHeader):
            output_file.write(get_header())
            output_file.write("\n")

        for value in json_data:
            output_file.write(get_data_record(value))
            output_file.write("\n")


delimiter = ","
json_data = {}
column_names_offset = {}
load_json_spec_file()
populate_column_names_offset()
load_input_json_data()
write_output_csv_file()

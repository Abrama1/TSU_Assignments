import os
from pprint import pprint
from Task_1 import build_index


def read_first_n_strings(file_path, n=9):
    values = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            for token in line.split():  # split on any whitespace
                values.append(token)
                if len(values) >= n:
                    return values
    return values


def build_two_level(root_folder):

    # get the (lev1, lev2) -> [(lev3, file_path), ...] mapping from task1
    index_dict = build_index(root_folder)
    result = {}

    for outer_key, items in index_dict.items():
        inner = {}

        for lev3_name, file_path in items:
            file_name = os.path.basename(file_path)  # file_0.in
            file_stem = os.path.splitext(file_name)[0]  # file_0
            nine_values = read_first_n_strings(file_path, 9)  # list of up to 9 strings

            inner[(lev3_name, file_stem)] = nine_values

        result[outer_key] = inner

    return result


here = os.path.dirname(__file__)
root = os.path.normpath(os.path.join(here, "..", "data", "Root"))

two_level = build_two_level(root)
pprint(two_level)

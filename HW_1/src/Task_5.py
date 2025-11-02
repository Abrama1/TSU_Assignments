import os
from pprint import pprint
from Task_2 import build_two_level
from Task_4 import even_descending_check


def count_matches(values):
    ok = 0
    for token in values:
        if even_descending_check(token):
            ok += 1

    return ok


def find_pairs_with_max_matches(two_level_dict):
    max_count = -1
    winners = []

    for outer_key, inner_map in two_level_dict.items():
        for inner_key, values in inner_map.items():
            c = count_matches(values)
            if c > max_count:
                max_count = c
                winners = [(outer_key, inner_key)]
            elif c == max_count:
                winners.append((outer_key, inner_key))

    return max_count, winners


here = os.path.dirname(__file__)
root = os.path.normpath(os.path.join(here, "..", "data", "Root"))

d2 = build_two_level(root)
max_count, pairs = find_pairs_with_max_matches(d2)

print(f"Max passing values for single inner entry: {max_count}")
print(f"pair or pairs with that maximum (outer_key, inner_key): ")
for outer_key, inner_key in pairs:
    print("  ", outer_key, "->", inner_key)


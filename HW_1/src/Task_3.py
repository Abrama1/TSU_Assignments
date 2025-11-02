import os
from pprint import pprint
from Task_2 import build_two_level


def find_max_value_pairs(two_level_dict):

    max_len = -1
    winners = []

    for outer_key, inner_map in two_level_dict.items():
        for inner_key, values in inner_map.items():
            curr_len = len(values)
            if curr_len > max_len:
                max_len = curr_len
                winners = [(outer_key, inner_key)]
            elif curr_len == max_len:
                winners.append((outer_key, inner_key))

    return max_len, winners


here = os.path.dirname(__file__)
root = os.path.normpath(os.path.join(here, "..", "data", "Root"))

d2 = build_two_level(root)
max_len, pairs = find_max_value_pairs(d2)

print(f"Max number of values found in single inner entry: {max_len}\n")
print("Pair(or pairs) with that maximum (outer_key, inner_key):")
for outer_key, inner_key in pairs:
    print("  ", outer_key, "->", inner_key)

# If you also want to see one sample's values, uncomment:
# if pairs:
#     ok, ik = pairs[0]
#     print("\nSample values for the first max pair:")
#     pprint(d2[ok][ik])

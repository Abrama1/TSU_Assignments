def average_value(two_dim_dict, outer_key=None, inner_key=None, prop=None):

    # helper to compute average for one list
    def _avg_of_list(str_list, prop_func):
        total = 0
        count = 0
        for s in str_list:
            if not s.isdigit():
                # skip anything that isn't purely digits
                continue
            n = int(s)
            if prop_func is not None and not prop_func(n):
                # skip values that don't satisfy the property
                continue
            total += n
            count += 1
        if count == 0:
            return 0.0
        return total / count

    # Case A: outer_key not provided -> compute for ALL outer inner
    if outer_key is None:
        result = {}
        for ok, inner_map in two_dim_dict.items():
            for ik, lst in inner_map.items():
                result[(ok, ik)] = _avg_of_list(lst, prop)
        return result

    # Case B: specific outer_key provided
    if outer_key not in two_dim_dict:
        return 0.0

    inner_map = two_dim_dict[outer_key]

    if inner_key is None:
        default_ik = ('  ', 0)
        if default_ik not in inner_map:
            return 0.0
        return _avg_of_list(inner_map[default_ik], prop)

    # Specific inner_key
    if inner_key not in inner_map:
        return 0.0

    return _avg_of_list(inner_map[inner_key], prop)


def first_last_equal_and_sum_even(n):
    s = str(n)
    if not s:
        return False
    if s[0] != s[-1]:
        return False
    total = 0
    for ch in s:
        if '0' <= ch <= '9':
            total += ord(ch) - ord('0')
        else:
            return False
    return (total % 2) == 0


# demo data
demo_dict = {
    ("Root", "lev2_demo"): {
        ("  ", 0): ["111", "222", "333"],  # ('  ', 0) default inner key
        ("lev3_demo", "file_0"): ["121", "246", "808"],  # 121 ok (1==1, sum 4 even), 246 sum 12 even but first!=last, 808 ok
    },
    ("Root", "lev2_other"): {
        ("lev3_demo", "file_1"): ["99", "1234", "505", "7007"],  # 99 ok, 505 ok, 7007 ok
    },
}

# for quick prints (you can toggle it off)
RUN_DEMO = True

if RUN_DEMO:
    # 1) All averages (no property) across all keys
    all_avgs = average_value(demo_dict)
    print("All averages (no property):")
    for k, v in all_avgs.items():
        print(" ", k, "->", v)

    # 2) Average for a specific outer_key + default inner_key ('  ', 0)
    v_default = average_value(demo_dict, outer_key=("Root", "lev2_demo"))
    print("\nAverage at ('Root','lev2_demo') for inner ('  ', 0):", v_default)

    # 3) Average for a specific outer, inner with the bonus property
    v_prop = average_value(
        demo_dict,
        outer_key=("Root", "lev2_demo"),
        inner_key=("lev3_demo", "file_0"),
        prop=first_last_equal_and_sum_even
    )
    print("Average with property for ('lev3_demo','file_0'):", v_prop)

    # 4) Bonus: find outer, inner with MIN average under property
    prop_map = average_value(demo_dict, prop=first_last_equal_and_sum_even)
    min_pair, min_val = None, None
    for pair, avg in prop_map.items():
        if min_val is None or avg < min_val:
            min_pair, min_val = pair, avg
    print("\nBONUS — min average under property:")
    print(" pair:", min_pair)
    print(" avg :", min_val)

def even_descending_check(nine_digits):
    s = str(nine_digits)
    if len(s) != 9 or not s.isdigit():
        return False

    # extract position 2, 4, 6, 8
    pick = [int(s[1]), int(s[3]), int(s[5]), int(s[7])]

    for d in pick:
        if d % 2 != 0:
            return False

    for i in range(len(pick) - 1):
        if pick[i] <= pick[i + 1]:
            return False

    return True

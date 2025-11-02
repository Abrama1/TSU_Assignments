import os


def build_index(root):

    root = os.path.normpath(root)
    lev1 = os.path.basename(root)
    result = {}

    for dirpath, dirnames, filenames in os.walk(root):
        # relative path from root
        rel_dir = os.path.relpath(dirpath, root)
        if rel_dir == ".":
            # skip the root itself
            continue

        parts = rel_dir.split(os.sep)
        if len(parts) != 2:
            # accept exactly two levels below root
            continue

        lev2, lev3 = parts[0], parts[1]
        key = (lev1, lev2)
        if key not in result:
            result[key] = []

        # add(lev3, "./...") for each file in this folder
        for fname in filenames:
            full_path = os.path.join(root, rel_dir, fname)
            rel_path = full_path.replace("\\", "/")
            result[key].append((lev3, rel_path))

    # for stable output sort tuples by(lev3, rel_path)
    for k in result:
        result[k].sort()

    return result


here = os.path.dirname(__file__)
root_folder = os.path.normpath(os.path.join(here, "..", "data", "Root"))

index = build_index(root_folder)
print(index)

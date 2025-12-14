import os
from equation_process import EquationProcess, build_expanded_matrix


def main():
    files = []

    for name in os.listdir("."):
        if name.endswith(".in"):
            files.append(name)

    files.sort()

    print(len(files))

    if files:
        e = build_expanded_matrix(files[0])
        print(e.shape)


if __name__ == "__main__":
    main()

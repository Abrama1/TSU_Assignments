import os
from equation_process import EquationProcess, solve_norm_from_file


def main():
    files = []

    for name in os.listdir("."):
        if name.endswith(".in"):
            files.append(name)

    files.sort()

    print(len(files))

    if files:
        norm = solve_norm_from_file(files[0])
        print(files[0])
        print(norm)


if __name__ == "__main__":
    main()

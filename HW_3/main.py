import os
from equation_process import EquationProcess


def main():
    files = []

    for name in os.listdir('.'):
        if name.endswith('.in'):
            files.append(name)

    files.sort()

    print(len(files))


if __name__ == "__main__":
    main()

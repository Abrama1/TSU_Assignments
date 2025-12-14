import os
from equation_process import EquationProcess


def main():
    files = []

    for name in os.listdir("."):
        if name.endswith(".in"):
            files.append(name)

    files.sort()

    print(len(files))

    if not files:
        return

    p = EquationProcess(files[0])
    p.start()
    p.join()

    out_name = files[0] + ".out"
    with open(out_name, "r") as f:
        print(files[0])
        print(f.read().strip())


if __name__ == "__main__":
    main()

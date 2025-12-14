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

    procs = []
    for fn in files:
        p = EquationProcess(fn)
        p.start()
        procs.append(p)

    for p in procs:
        p.join()

    results = {}
    for fn in files:
        out_name = fn + ".out"
        try:
            with open(out_name, "r") as f:
                results[fn] = float(f.read().strip())
        except:
            results[fn] = float("nan")

    print(len(results))


if __name__ == "__main__":
    main()

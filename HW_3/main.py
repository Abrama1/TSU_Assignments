import os
from equation_process import EquationProcess
import math


def main():
    files = []

    for name in os.listdir("."):
        if name.endswith(".in"):
            files.append(name)

    files.sort()

    if not files:
        return

    procs = []
    for fn in files:
        p = EquationProcess(fn)
        p.start()
        procs.append(p)

    for p in procs:
        p.join()

    best_file = None
    best_norm = -1.0

    for fn in files:
        out_name = fn + ".out"
        try:
            with open(out_name, "r") as f:
                val = float(f.read().strip())
            if not math.isnan(val) and val > best_norm:
                best_norm = val
                best_file = fn
        except:
            pass

    if best_file is not None:
        print(best_file)


if __name__ == "__main__":
    main()

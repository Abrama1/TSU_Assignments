from multiprocessing import Process
import numpy as np


def _parse_equation_tokens(tokens, n):
    row = [0] * (n + 1)

    for t in tokens:
        if t == "b":
            row[n] += 1
        elif t == "-b":
            row[n] -= 1
        else:
            sign = -1 if t[0] == "-" else 1
            s = t[1:] if sign == -1 else t
            idx = int(s[1:]) - 1
            row[idx] += sign

    return row


def build_expanded_matrix(filename):
    with open(filename, "r") as f:
        lines = [ln.strip() for ln in f if ln.strip()]

    n = len(lines)
    rows = []

    for ln in lines:
        rows.append(_parse_equation_tokens(ln.split(), n))

    return np.array(rows, dtype=float)


class EquationProcess(Process):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def run(self):
        pass

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


def cramer_determinants_from_expanded(E):
    n = E.shape[0]
    A = E[:, :n]
    B = E[:, n]
    detA = float(np.linalg.det(A))

    detAi = []
    for i in range(n):
        Ai = A.copy()
        Ai[:, i] = B
        detAi.append(float(np.linalg.det(Ai)))

    return detA, detAi


def solve_norm_from_expanded(E, eps=1e-9):
    detA, detAi = cramer_determinants_from_expanded(E)

    if abs(detA) < eps:
        return float("nan")

    X = np.array([d / detA for d in detAi], dtype=float)
    return float(np.linalg.norm(X))


def solve_norm_from_file(filename):
    E = build_expanded_matrix(filename)
    return solve_norm_from_expanded(E)


class EquationProcess(Process):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def run(self):
        norm = solve_norm_from_file(self.filename)
        out_name = self.filename + ".out"
        with open(out_name, "w") as f:
            f.write(str(norm))

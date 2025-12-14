from multiprocessing import Process


class EquationProcess(Process):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def run(self):
        pass

import math
from Model import Model


class Kursawe(Model):
    def __init__(self):
        self.domMin = [-5, -5, -5]
        self.domMax = [5, 5, 5]
        self.decisions = 3
        self.objectives = 2
        self.x = [0, 0, 0]
        self.setDecs()

    def getObjs(self):
        f1 = 0
        f2 = 0
        for i in range(0, self.decisions):
            if i < self.decisions - 1:
                f1 += (-10) * math.pow(math.exp(1),
                                       (-0.2 * math.sqrt(math.pow(self.x[i], 2) + math.pow(self.x[i + 1], 2))))
            f2 += math.pow(math.fabs(self.x[i]), 0.8) + 5 * math.sin(self.x[i])
        return [f1, f2]

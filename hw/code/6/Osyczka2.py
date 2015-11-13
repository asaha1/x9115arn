import math
from Model import Model

class Osyczka2(Model):
    def __init__(self):
        self.domMin = [0, 0, 1, 0, 1, 0]
        self.domMax = [10, 10, 5, 6, 5, 10]
        self.decisions = 6
        self.objectives = 2
        self.x = [0, 0, 0, 0, 0, 0]
        self.setDecs()

    def getObjs(self):
        f1 = (-1) * (
            25 * math.pow((self.x[0] - 2), 2) + math.pow((self.x[1] - 2), 2) + (
                math.pow((self.x[2] - 1), 2)) * math.pow(
                (self.x[3] - 4), 2) + math.pow((self.x[4] - 1), 2))
        f2 = math.pow(self.x[0], 2) + math.pow(self.x[1], 2) + math.pow(self.x[2], 2) + math.pow(self.x[3],
                                                                                                 2) + math.pow(
            self.x[4], 2) + math.pow(self.x[5], 2)
        return [f1, f2]

    def constraints(self):
        if (self.x[0] + self.x[1] - 2 < 0):
            return False
        elif (6 - self.x[0] - self.x[1] < 0):
            return False
        elif (2 - self.x[1] + self.x[0] < 0):
            return False
        elif (2 - self.x[0] + 3 * self.x[1] < 0):
            return False
        elif (4 - math.pow((self.x[2] - 3), 2) - self.x[3] < 0):
            return False
        elif (math.pow((self.x[4] - 3), 3) + self.x[5] - 4 < 0):
            return False
        else:
            for i in range(0, self.decisions):
                if self.x[i] < self.domMin[i] or self.x[i] > self.domMax[i]:
                    return False
            return True

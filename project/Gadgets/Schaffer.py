import math
from Model import Model
class Schaffer(Model):
    def __init__(self):
        self.domMin = [-100000]
        self.domMax = [100000]
        self.decisions = 1
        self.objectives = 2
        self.x = [0]
        self.setDecs()

    def getObjs(self):
        f1 = math.pow(self.x[0], 2)
        f2 = math.pow((self.x[0] - 2), 2)
        return [f1, f2]
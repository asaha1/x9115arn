import math
import random
import copy

# adapted the structure of model from https://github.com/maverickmishra/x9115NVN/tree/master/hw/code/6

class Model(object):
    def __init__(self):
        self.domMin = [0]
        self.domMax = [0]
        self.decs = 0
        self.objs = 0
        self.val = [0]

    def eval(self):
        return sum(self.getObjs())

    def getObjs(self):
        pass

    def setDecs(self):
        while True:
            for i in range(0, self.decs):
                self.val[i] = random.uniform(self.domMin[i], self.domMax[i])
            if self.constraints(): break

    def constraints(self):
        for i in range(0, self.decs):
            if self.val[i] < self.domMin[i] or self.val[i] > self.domMax[i]:
                return False
        return True


class Schaffer(Model):
    def __init__(self):
        self.decs = 1
        self.objs = 2
        self.val = [0]
        self.domMin = [-100000]
        self.domMax = [100000]
        self.setDecs()

    def getObjs(self):
        f1 = math.pow(self.val[0], 2)
        f2 = math.pow((self.val[0] - 2), 2)
        return [f1, f2]


class Osyczka2(Model):
    def __init__(self):
        self.decs = 6
        self.objs = 2
        self.domMin = [0, 0, 1, 0, 1, 0]
        self.domMax = [10, 10, 5, 6, 5, 10]
        self.val = [0, 0, 0, 0, 0, 0]
        self.setDecs()

    def getObjs(self):
        f1 = (-1) * (
            25 * math.pow((self.val[0] - 2), 2) + math.pow((self.val[1] - 2), 2) + (math.pow((self.val[2] - 1), 2)) * math.pow(
            (self.val[3] - 4), 2) + math.pow((self.val[4] - 1), 2))
        f2 = math.pow(self.val[0], 2) + math.pow(self.val[1], 2) + math.pow(self.val[2], 2) + math.pow(self.val[3],
                                                                                                       2) + math.pow(
            self.val[4], 2) + math.pow(self.val[5], 2)
        return [f1, f2]

    def constraints(self):
        if (self.val[0] + self.val[1] - 2 < 0):
            return False
        elif (6 - self.val[0] - self.val[1] < 0):
            return False
        elif (2 - self.val[1] + self.val[0] < 0):
            return False
        elif (2 - self.val[0] + 3 * self.val[1] < 0):
            return False
        elif (4 - math.pow((self.val[2] - 3), 2) - self.val[3] < 0):
            return False
        elif (math.pow((self.val[4] - 3), 3) + self.val[5] - 4 < 0):
            return False
        else:
            for i in range(0, self.decs):
                if self.val[i] < self.domMin[i] or self.val[i] > self.domMax[i]:
                    return False
            return True


class Kursawe(Model):
    def __init__(self):
        self.decs = 3
        self.objs = 2
        self.domMin = [-5, -5, -5]
        self.domMax = [5, 5, 5]
        self.val = [0, 0, 0]
        self.setDecs()

    def getObjs(self):
        f1 = 0
        f2 = 0
        for i in range(0, self.decs):
            if i < self.decs - 1:
                f1 += (-10) * math.pow(math.exp(1),
                                       (-0.2 * math.sqrt(math.pow(self.val[i], 2) + math.pow(self.val[i + 1], 2))))
            f2 += math.pow(math.fabs(self.val[i]), 0.8) + 5 * math.sin(self.val[i])
        return [f1, f2]

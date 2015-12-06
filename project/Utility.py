import random

bounds = list()
bounds.append([1, 10])
bounds.append([1, 5])
bounds.append([1, 2])
bounds.append([1, 50])
bounds.append([1, 5])
bounds.append([0.2, 0.4])
bounds.append([0, 10])
bounds.append([12.5, 25])
bounds.append([0.9, 1.5])
bounds.append([0, 10])
bounds.append([1, 2]) #10
bounds.append([0, 10])
bounds.append([0, 2])
bounds.append([0, 2])
bounds.append([0, 10])
bounds.append([0, 10])
bounds.append([0, 10])

def getRandomElement(min, max):
    return random.uniform(min, max)

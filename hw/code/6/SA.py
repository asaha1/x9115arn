import Model
import math
import random
import copy
import Schaffer, Osyczka2, Kursawe


def SimulatedAnnealing(model):
    s = model()
    sb = model()
    sb = copy.deepcopy(s)
    k = 1
    kMax = 1000
    width = 25
    print "%05d " % (int(k)),
    while (k <= kMax):
        sn = neighbor(s, random.randint(0, s.decs - 1), model)
        if (sn.eval() < sb.eval()):
            sb = copy.deepcopy(sn)
            s = copy.deepcopy(sn)
            print "!",
        elif (sn.eval() < s.eval()):
            s = copy.deepcopy(sn)
            print "+",
        elif (probability(sn.eval(), s.eval(), (k / kMax)) < random.uniform(0, 1)):
            s = copy.deepcopy(sn)
            print "?",
        else:
            print ".",

        k = k + 1
        if (k % width == 0):
            print ""
            if k != kMax:
                print "%05d " % (int(k)),

    print "\nThe best solution is ",
    for value in sb.val: print str(value) + ", ",
    print ""
    return True


def neighbor(s, index, model):
    sn = model()
    sn = copy.deepcopy(s)
    while True:
        sn.val[index] = random.uniform(sn.domMin[index], sn.domMax[index])
        if sn.constraints(): break
    return sn


def probability(en, e, t):
    if t != 0:
        return math.exp((e - en) / t)

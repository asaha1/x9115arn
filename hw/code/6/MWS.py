import Model
import math
import random
import copy


def MaxWalkSat(model):
    eval = 0
    maxtries = 100
    maxchanges = 50
    threshold = -10000
    p = 0.5
    step = 10
    count = 0
    print "%05d " % count,
    for i in range(0, maxtries):
        s = model()
        if i == 0:
            sbest = copy.deepcopy(s)
        for j in range(0, maxchanges):
            eval += 1
            if s.eval() < threshold:
                print ""
                print "The best solution is \n %s" % s.val
                return True

            which = random.randint(0, s.decs - 1)
            score_old = s.eval()
            if p < random.random():
                s = neighbor(s, which, model)
            else:
                s = optc(s, which, step, model)
            if s.eval() < sbest.eval():
                sbest = copy.deepcopy(s)
                print "!",
            elif s.eval() < score_old:
                print  "+",
            elif s.eval() == score_old:
                print ".",
            else:
                print "?",

        count += 1
        print ""
        if i != maxtries:
            print "%05d " % (count * 50),

    print "\nThe best solution is ",
    for value in sbest.val:
        print str(value) + ", ",
    print ""


def optc(s, index, step, model):
    sn = copy.deepcopy(s)
    snbest = copy.deepcopy(sn)
    dis = (sn.domMax[index] - sn.domMin[index]) / step
    if dis != 0:
        for i in range(-int((s.val[index] - s.domMin[index]) / dis), int((s.domMax[index] - s.val[index]) / dis) + 1):
            sn.val[index] = sn.val[index] + i * dis
            if not sn.constraints(): continue
            if sn.eval() < snbest.eval():
                snbest = copy.deepcopy(sn)
    return snbest


def neighbor(s, index, model):
    sn = copy.deepcopy(s)
    while True:
        sn.val[index] = random.uniform(sn.domMin[index], sn.domMax[index])
        if sn.constraints(): break
    return sn

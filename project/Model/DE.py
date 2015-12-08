import random
import copy
import numpy


def DE(model):
    print "Model: ", model.__name__

    F = 0.75    # crossover factor
    CR = 0.3    # crossover probability
    maxtries = 25
    NumCandidates = 160
    best = model()
    candidates = [best]

    for i in range(1, NumCandidates):
        candidate = model()
        candidates.append(candidate)
        if candidate.eval() < best.eval():
            best = copy.deepcopy(candidate)

    def mutate(candidates, F, CR, best):
        for i in range(len(candidates)):
            tmp = range(len(candidates))
            tmp.remove(i)
            while True:
                choice = numpy.random.choice(tmp, 3)
                # print "choice",choice
                X = candidates[choice[0]]
                Y = candidates[choice[1]]
                Z = candidates[choice[2]]

                old = candidates[i]
                # print "~~~~old",old.val
                r = random.randint(0, old.decs - 1)
                new = model()
                for j in range(old.decs):
                    if random.random() < CR or j == r:
                        new.val[j] = X.val[j] + F * (Y.val[j] - Z.val[j])  # Mutate: X + F*(Y - Z)
                    else:
                        new.val[j] = old.val[j]
                if new.constraints(): break
            if new.eval() < best.eval():
                best = copy.deepcopy(new)
                printList.append("!")
                # printList.append (str(best.val)) ##Gadgets Best Found
            elif new.eval() < old.eval():
                printList.append("+")
            elif new.eval() == old.eval():
                printList.append("?")
            else:
                new = old
                printList.append(".")
            # print "~~~~new",new.val
            yield new, best

    min_val=[]
    for tries in range(maxtries):
        printList = []
        print "Gen %02d" % (tries + 1),
        print "|",
        newcandidates = []
        for new, best in mutate(candidates, F, CR, best):
            newcandidates.append(new)
        candidates = newcandidates
        print "".join(printList),
        min_val.append(sum(best.getObjs(best.val)))

        print("")
    print "Best solutions= "
    for value in best.val:
        print value

    return min_val




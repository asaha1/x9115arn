import random
from deap import tools, base, creator
from random import uniform
import array
import numpy


def SPEA2(model):
    print "Model: ", model.__name__
    GEN = 50
    MU = 100
    creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0))
    creator.create("Individual", array.array, typecode='d', fitness=creator.FitnessMin)
    toolbox = base.Toolbox()

    model = model()
    BOUND_LOW, BOUND_UP = model.domMin, model.domMax
    NDIM = model.decs

    def uniform(low, up, size=None):
        try:
            return [random.uniform(a, b) for a, b in zip(low, up)]
        except TypeError:
            return [random.uniform(a, b) for a, b in zip([low] * size, [up] * size)]

    toolbox.register("attr_float", uniform, BOUND_LOW, BOUND_UP, NDIM)
    toolbox.register("r_list", tools.initIterate, creator.Individual, toolbox.attr_float)
    toolbox.register("population", tools.initRepeat, list, toolbox.r_list)

    toolbox.register("evaluate", model.getObjs)
    toolbox.register("mate", tools.cxSimulatedBinaryBounded, eta=20.0, low=BOUND_LOW, up=BOUND_UP)
    toolbox.register("mutate", tools.mutPolynomialBounded, eta=20.0, low=BOUND_LOW, up=BOUND_UP, indpb=1.0 / NDIM)
    toolbox.register("select", tools.selSPEA2)
    # binary tournament selection
    toolbox.register("selectTournament", tools.selTournament, tournsize=2)

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)

    logbook = tools.Logbook()
    logbook.header = "gen", "evals", "std", "min", "avg", "max"

    # binary tournament selection
    # Step 1 Initialization
    pop = toolbox.population(n=MU)

    archive = []
    curr_gen = 1
    min_val = []

    while True:
        # Step 2 Fitness assignement
        for ind in pop:
            ind.fitness.values = toolbox.evaluate(ind)

        for ind in archive:
            ind.fitness.values = toolbox.evaluate(ind)

        # Step 3 Environmental selection
        archive = toolbox.select(pop + archive, k=GEN)

        # Step 4 Termination
        if curr_gen >= GEN:
            final_set = archive
            break

        # Step 5 Mating Selection
        mating_pool = toolbox.selectTournament(archive, k=GEN)
        offspring_pool = map(toolbox.clone, mating_pool)

        # Step 6 Variation
        # crossover 100% and mutation 6%
        for child1, child2 in zip(offspring_pool[::2], offspring_pool[1::2]):
            toolbox.mate(child1, child2)

        for mutant in offspring_pool:
            if random.random() < 0.06:
                toolbox.mutate(mutant)

        pop = offspring_pool
        record = stats.compile(pop)
        logbook.record(gen=curr_gen, evals=100, **record)
        print(logbook.stream)

        curr_gen += 1

    min = final_set[0]
    for ind in final_set:
        if sum(model.getObjs(ind)) < sum(model.getObjs(min)):
            min = ind
        min_val.append(ind.fitness.values[0] + ind.fitness.values[1])
    print "Best solution = "
    for i in min:
        print i

    return min_val

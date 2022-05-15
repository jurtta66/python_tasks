import matplotlib.pyplot as plt
import random
import numpy as np
from deap import base, creator, tools, algorithms

# Константы
pop_size = 100  # Количество особей в популяции
pr_cross = 0.8  # Вероятность скрещивания
pr_mut = 0.1  # Вероятность мутации
generations = 200  # Количество поколений
length = 20  # мощность подмножества

# Сгенерируем список чисел и найдем с помощью генетического алгоритма
# его подмножество с максимальной суммой (Оптимальная сумма
# равна сумме 20 максимальных элементов)
nums = [random.uniform(-50, 50) for i in range(50)]


creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)


def oneMaxFitness(ind):
    return sum(ind),


def pick_gen():
    index = random.randint(0, len(nums) - 1)
    return nums[index]

'''
def mutate(ind, pr_gen=0.02):
    indexes = [i[1] for i in ind]
    for i in range(len(ind)):
        if random.random() <= pr_gen:
            j = random.randint(0, len(ind) - 1)
            while j in indexes:
                j = random.randint(0, len(ind) - 1)
            ind[i[0]] = ind[j[0]]
            ind[i[1]] = j
'''


def mutate(ind, pr_gen=0.02):
    for i in range(len(ind)):
        if random.random() <= pr_gen:
            j = random.randint(0, len(nums) - 1)
            if ind[i] <= nums[j]: ind[i] = nums[j]
    return ind,


toolbox = base.Toolbox()
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, pick_gen, length)
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

pop = toolbox.populationCreator(n=pop_size)

toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", mutate)
toolbox.register("evaluate", oneMaxFitness)

stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("max", np.max)
stats.register("avg", np.mean)


# Генетический алгоритм
pop, logbook = algorithms.eaSimple(pop, toolbox,
                                   cxpb=pr_cross,
                                   mutpb=pr_mut,
                                   ngen=generations,
                                   stats=stats,
                                   verbose=True)


print("Оптимальная сумма: ", 20*max(nums))

maxFitnessValues, meanFitnessValues = logbook.select("max", "avg")

plt.plot(maxFitnessValues, color='blue')
plt.plot(meanFitnessValues, color='green')
plt.xlabel('Поколение')
plt.ylabel('Макс/средняя приспособленность')
plt.title('Зависимость максимальной и средней приспособленности от поколения')
plt.show()

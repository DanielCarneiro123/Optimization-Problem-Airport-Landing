'''
Representation of Solutions:
 Best soilution is found where no improvements can be made
Define a chromosome representation that encodes the landing schedule for airplanes. Each chromosome represents a potential solution, where the genes represent the landing times of airplanes.
Fitness Function:

Design a fitness function that evaluates the quality of a landing schedule based on criteria such as safety (e.g., ensuring airplanes land with sufficient fuel reserves), efficiency (e.g., minimizing delays and maximizing runway utilization), and adherence to constraints (e.g., expected landing times, airport capacity).
Initialization:

Initialize a population of chromosomes representing potential landing schedules. The initial population can be generated randomly or through heuristic methods.
Selection:

Select parent chromosomes from the population based on their fitness scores. Employ selection techniques such as roulette wheel selection, tournament selection, or rank-based selection.
Crossover:

Perform crossover operations to create offspring chromosomes from selected parent chromosomes. Crossover points can be chosen randomly or based on specific heuristics.
Mutation:

Apply mutation operators to introduce diversity into the population. Mutation can involve randomly changing genes in a chromosome to explore new regions of the solution space.
Evaluation:

Evaluate the fitness of offspring chromosomes using the fitness function. Determine which individuals survive to the next generation based on their fitness scores.
Replacement:

Select individuals for the next generation using replacement strategies such as elitism (preserving the best-performing individuals) or generational replacement (replacing the entire population).
Termination:

Determine termination conditions, such as reaching a maximum number of generations, achieving a satisfactory solution, or stagnation in fitness improvement.
Iteration:

Iterate through the above steps until the termination conditions are met, continually refining the population to find an optimal or near-optimal solution.
Post-Processing:

After termination, analyze the best solution obtained from the genetic algorithm and perform any necessary post-processing to finalize the landing schedule.

'''

"""
My study object chromossome will be the complete Landing Schedule for the plane.
I will evaluate the fittest of the random population
"""

""" Selection Part
Algorithm i'm going to use 
 -> Rank Selection
 -> Tournament Selection
 -> Stochastic Selection
 -> 


Data model for initialization part;
Airplane

## Termination condition -> Stop the algorithm when number of generations max, no difference relative to last generations, or make a fitness threshold, that is considered a sub-optimal solution to the problem.


"""

from chromosome import *



def generate_chromosomes(population_size):
    chromosome = []
    for i in range(population_size):
        chromosome.append(Airplane())
    chromosomes = []

    for i in range(population_size):
        new_chromosome = chromosome[:]
        random.shuffle(new_chromosome)
        chromosomes.append(new_chromosome)

    return chromosomes



def print_population(population):
    for chromosome in population:
        chromosome.print_schedule()


def checkFreeRunway(runway_state):
    if runway_state[0] == 0:
        return 0
    elif runway_state[1] == 0:
        return 1
    elif runway_state[2] == 0:
        return 2
    return -1


def enoughGas(airplane):
    gasHour = airplane.fuel_consumption_rate*60
    if airplane.arriving_fuel_level > gasHour:
        return True
    return False


def onTime(airplane):
    if airplane.expected_landing_time < 0:
        return False
    return True


def calculate_fitness(chromosome,airport):
    fitness = 0
    for gene in chromosome:
        runway_state = airport.get_runway_state()
        runway_free= checkFreeRunway(runway_state)
        if runway_free != -1:
            checkGas = enoughGas(gene)
            if checkGas:
                fitness += 1
            checkTime = onTime(gene)
            if checkTime:
                fitness += 1
            if runway_free == 0:
                airport.mutate_runway1(gene)
            elif runway_free == 1:
                airport.mutate_runway2(gene)
            else:
                airport.mutate_runway3(gene)

        else:
            gene.mutate_airplane_arriving_fuel_level(gene.arriving_fuel_level - gene.fuel_consumption_rate*3)
            gene.mutate_airplane_arriving_time(gene.expected_landing_time - 3)
            checkGas = enoughGas(gene)
            if checkGas:
                fitness += 1
            checkTime = onTime(gene)
            if checkTime:
                fitness += 1
            seed = random.randint(1,3)
            if seed == 1:
                airport.mutate_runway1(gene)
            elif seed == 2:
                airport.mutate_runway2(gene)
            else:
                airport.mutate_runway3(gene)
    return fitness

def get_fitness(chromosomes):
    total_fitness = 0
    for (_,fitness) in chromosomes:
        total_fitness += fitness
    return total_fitness


def roulette_selection(chromosomes):
    total_fitness = get_fitness(chromosomes)
    selected = []
    selection_probabilities = [(chromosome, fitness / total_fitness) for chromosome, fitness in chromosomes]

    while len(selected) < len(chromosomes):
        r = random.random()
        cumulative_probability = 0

        for chromosome, probability in selection_probabilities:
            cumulative_probability += probability
            if cumulative_probability > r:
                selected.append(chromosome)
                break

    return selected



def rank_selection(chromosomes, selection_pressure):
    n = len(chromosomes)
    selected = []

    if selection_pressure < 1 or selection_pressure > 2:
        raise ValueError("Selection pressure must be between 1 and 2")

    # Calculate rank-based probabilities
    rank_probabilities = [(chromosome, (selection_pressure - (2 * selection_pressure - 2) * (i - 1) / (n - 1)) / n)
                          for i, (chromosome, _) in enumerate(sorted(chromosomes, key=lambda x: x[1]))]

    # Perform rank-based selection
    while len(selected) < n:
        # Spin the roulette wheel
        r = random.random()
        cumulative_probability = 0

        for chromosome, probability in rank_probabilities:
            cumulative_probability += probability
            if cumulative_probability > r:
                selected.append(chromosome)
                break

    return selected


def reproduction(chromosome1, chromosome2):
    n = len(chromosome1)
    point = random.randint(0, n - 1)
    new_chromosome = []

    new_chromosome.extend(chromosome1[:point])

    for gene in chromosome2:
        if gene not in new_chromosome:
            new_chromosome.append(gene)

    return new_chromosome


def mutation(chromosome):
    n = len(chromosome)
    points = random.sample(range(n), 2)
    point1, point2 = points[0], points[1]
    chromosome[point1], chromosome[point2] = chromosome[point2], chromosome[point1]
    return chromosome

def geneticAI(population_size, selection_method):
    # Initialization of population
    airport = Airport()
    population = generate_chromosomes(population_size)
    population_fitness = []
    for chromosome in population:
        fitness = calculate_fitness(chromosome,airport)
        population_fitness.append((chromosome, fitness))

    while (number_of_generations(10))
    # Calculate the fitness
    for chromosome in population:
        fitness = calculate_fitness(chromosome)
        population_fitness.append((chromosome, fitness))
    # Selection
    match selection_method:
        case "roulette":
            best_chromosomes = roulette_selection(population_fitness)
        case "rank":
            best_chromosomes = rank_selection(population_fitness)
        case _:
            raise ValueError("Unknown selection method: " + selection_method)
    # Reproduction
    if len(best_chromosomes) % 2 != 0:
        # If the number of best chromosomes is odd, remove the last one
        del best_chromosomes[-1]

    # Perform pairwise reproduction for all remaining chromosomes
    for i in range(0, len(best_chromosomes), 2):
        c1, c2 = best_chromosomes[i], best_chromosomes[i + 1]
        reproduction(c1, c2)



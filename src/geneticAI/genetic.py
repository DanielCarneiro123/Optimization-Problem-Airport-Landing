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

from schedule import *


# def genetic_main():


def generate_population(population_size):
    population = []
    for i in range(population_size):
        chromosome = generate_chromosome()
        population.append(chromosome)
    return population


def print_population(population):
    for chromosome in population:
        chromosome.print_schedule()


size = 5
pop1 = generate_population(size)
print_population(pop1)

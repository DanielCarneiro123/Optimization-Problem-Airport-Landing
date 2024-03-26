from airplane import *
from landing_strip import *
from tabu_search import *
import random

def generate_chromosomes(chromosome,population_size):
    """
    This function generates a list of chromosomes for a genetic algorithm.

    Parameters:
    population_size (int): The size of the population

    Returns:
    List[List[Airplane]]: A list of chromosomes
    """
    chromosomes = []
    for _ in range(population_size):
        new_chromosome = chromosome[:]
        random.shuffle(new_chromosome)
        chromosomes.append(new_chromosome)

    return chromosomes


def roulette_selection(chromosomes):
    total_fitness = sum(fitness for _, fitness in chromosomes)
    relative_fitness = [fitness / total_fitness for _, fitness in chromosomes]
    cumulative_probability = [sum(relative_fitness[:i+1]) for i in range(len(relative_fitness))]
    
    rand = random.random()

    selected = []

    for i, fitness in enumerate(cumulative_probability):
        if rand <= fitness:
            selected.append(chromosomes[i][0])

    return selected


# Partially mapped crossover (PMX)
def reproduction(parent1, parent2):
    """
    Perform Partially Mapped Crossover (PMX) between two parent chromosomes.

    Parameters:
    parent1 (List[int]): The first parent chromosome.
    parent2 (List[int]): The second parent chromosome.

    Returns:
    Tuple[List[int], List[int]]: The offspring chromosomes.
    """
    n = len(parent1)
    # Choose crossover points
    point1 = random.randint(0, n - 1)
    point2 = random.randint(0, n - 1)
    if point1 > point2:
        point1, point2 = point2, point1

    # Initialize offsprings with middle of respective parents
    offspring1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    offspring2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    # Map genes from parent1 to parent2 and vice versa within the crossover points
    mapping_1 = {}
    mapping_2 = {}
 
    for i in range(point1,point2):
        mapping_1[offspring1[i]] = offspring2[i]
        mapping_2[offspring2[i]] = offspring1[i]

    # Repair offspring 1
    for i in range(0,point1):
        while (offspring1[i] in mapping_1):
            offspring1[i] = mapping_1[offspring1[i]]
    for i in range(point2,n):
        while (offspring1[i] in mapping_1):
            offspring1[i] = mapping_1[offspring1[i]]

    # Repair offspring 1
    for i in range(0,point1):
        while (offspring2[i] in mapping_2):
            offspring2[i] = mapping_2[offspring2[i]]
    for i in range(point2,n):
        while (offspring2[i] in mapping_2):
            offspring2[i] = mapping_2[offspring2[i]]


    return offspring1, offspring2

def reproduction_all(chromosomes, size_new_gen):
    """
    This function takes a list of chromosomes and returns a new list of offspring chromosomes.

    Parameters:
    chromosomes (List[Airplane]): A list of chromosomes to be used for reproduction
    size_new_gen (int): The desired size of the new generation

    Returns:
    List[Airplane]: A list of offspring chromosomes
    """
    new_generation = []
    while len(new_generation) < size_new_gen:
        parent1, parent2 = random.sample(chromosomes, 2)
        c1, c2 = reproduction(parent1, parent2)  
        new_generation.append(c1)
        new_generation.append(c2)
    return new_generation

def mutation(chromosome):
    """
    This function takes a chromosome and returns a new chromosome that suffered a mutation.

    Parameters:
    chromosome (List[Airplane]): Chromosome  to be mutated

    Returns:
    List[Airplane]: A list of mutated chromosomes
    """
    n = len(chromosome)
    points = random.sample(range(n), 2)
    point1, point2 = points[0], points[1]
    chromosome[point1], chromosome[point2] = chromosome[point2], chromosome[point1]
    return chromosome

def mutation_all(chromosomes):
    """
    This function takes a list of chromosomes and returns a new list of mutated chromosomes.

    Parameters:
    chromosomes (List[Airplane]): A list of chromosomes to be mutated

    Returns:
    List[Airplane]: A list of mutated chromosomes
    """
    new_generation = []
    for chromosome in chromosomes:
        go_to_mutation = random.random() 
        if go_to_mutation < 0.05:
            _, fitness1, unsafe_waiting1, curr_num_of_crashes1 = generateResults(chromosome)
            new_chromosome = chromosome
            new_chromosome = mutation(chromosome)
            _, fitness2, unsafe_waiting2, curr_num_of_crashes2 = generateResults(new_chromosome)
            acceptWeakMutation = random.random()
            if ((fitness2 < fitness1) and (unsafe_waiting2 <= unsafe_waiting1) and (curr_num_of_crashes2 <= curr_num_of_crashes1)) or ((unsafe_waiting2 < unsafe_waiting1) and (curr_num_of_crashes2 <= curr_num_of_crashes1)) or (curr_num_of_crashes2 < curr_num_of_crashes1):
                    new_generation.append(chromosome)
            else:
                if acceptWeakMutation < 0.5:
                    new_generation.append(new_chromosome)
                else:
                    new_generation.append(chromosome)

        else:
            new_generation.append(chromosome)

    
    return new_generation

def get_elites(population_fitness,elite_size):
    population_fitness.sort(key=lambda x: x[1], reverse=True)  
    elite_population= [x[0] for x in population_fitness[:elite_size]]
    return elite_population

# Doing
def geneticAI(airplanes, population_size, max_number_of_iterations, selection_method,elite_percentage):
    population = generate_chromosomes(airplanes, population_size) # Generate population
    current_fitness_of_best_chromosome = float('inf') # Best fitness
    best_chromosome = None # Best chromosome
    num_of_crashes = 100000
    unsafe_planes = 100000 
    elite_size = int(population_size*elite_percentage)-1 # Elite size individuals to retain for next iteration

    for _ in range(max_number_of_iterations):

        population_fitness = []

        # Evaluate fitness for each chromosome in the population
        for chromosome in population:
            _, fitness, unsafe_waiting, curr_num_of_crashes = generateResults(chromosome)
            population_fitness.append((chromosome, fitness))

            if ((fitness < current_fitness_of_best_chromosome) and (unsafe_waiting <= unsafe_planes) and (curr_num_of_crashes <= num_of_crashes)) or ((unsafe_waiting < unsafe_planes) and (curr_num_of_crashes <= num_of_crashes)) or (curr_num_of_crashes < num_of_crashes):
                current_fitness_of_best_chromosome = fitness
                best_chromosome = chromosome
                num_of_crashes = curr_num_of_crashes
                unsafe_planes = unsafe_waiting
        
         #print(current_fitness_of_best_chromosome)
        # Elite population 
        elite_population = get_elites(population_fitness,elite_size)

        # Select best chromosomes for reproduction
        if selection_method == "roulette":
            selection_population = roulette_selection(population_fitness)
        else:
            raise ValueError("Unknown selection method: " + selection_method)
        
        if(len(selection_population) <= 1):
            break

        # Generate new generation through reproduction and mutation
        reproduction_size = len(population) - elite_size
        reproduction_population = reproduction_all(selection_population, reproduction_size)
        mutate_population = mutation_all(reproduction_population)
        new_generation = mutate_population+elite_population

        # Update population with mutated generation
        population = new_generation

    return best_chromosome, current_fitness_of_best_chromosome
def main():
    population_size = 100
    max_number_of_iterations = 1000
    elite_percentage = 0.05
    selection_method = "roulette"


    airplane1 = Airplane(1000, 15, 0)
    airplane2 = Airplane(2000, 25, 20)
    airplane3 = Airplane(1500, 20, 50)  
    airplane4 = Airplane(1800, 18, 70)
    airplane5 = Airplane(2500, 22, 40)
    airplane6 = Airplane(1200, 12, 80)
    airplane7 = Airplane(2800, 30, 20)
    airplane8 = Airplane(2000, 28, 60)
    airplane9 = Airplane(1600, 16, 10)
    airplane10 = Airplane(2200, 24, 85)


   
    # Store airplanes in a list
    airplanes = [airplane1, airplane2, airplane9, airplane10
                 , airplane5, airplane6, airplane7, airplane8, airplane3, airplane4,
    ]
 
    
    best_solution,best_cost = geneticAI(airplanes,population_size, max_number_of_iterations, selection_method,elite_percentage)
    print("BEST SOLUTION:")
    print_airplanes_and_strips(best_solution)
    print("Best cost:", best_cost)

def print_airplanes_and_strips(best_solution):
    landing_strips, sum_difference, unsafe_waiting, n = generateResults(best_solution)
    print("Sum of differences between actual and expected landing times:", sum_difference)
    for i, landing_strip in enumerate(landing_strips):
        print(f"Landing Strip {i}:")
        for airplane in landing_strip.current_airplanes:
            print(airplane)
            if (airplane.is_gonna_crash()):
                print("CRAAAAAAAAAAAAAAAASH")
    print("Crashes:", n)
    print("Unsafe waiting:", unsafe_waiting)

if __name__ == "__main__":
    main()
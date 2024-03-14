import random
import copy


import random

# Done
class Airplane:
    def __init__(self, fuel_level, fuel_consumption_rate, expected_landing_time):
        self.arriving_fuel_level = fuel_level
        self.fuel_consumption_rate = fuel_consumption_rate
        self.expected_landing_time = expected_landing_time
        self.actual_landing_time = 0 
        self.safe = self.ensure_enough_fuel()

    def get_arriving_fuel_level(self):
        return self.arriving_fuel_level

    def get_fuel_consumption_rate(self):
        return self.fuel_consumption_rate

    def get_expected_landing_time(self):
        return self.expected_landing_time

    def get_actual_landing_time(self):
        return self.actual_landing_time

    def get_safe(self):
        return self.safe

    def __str__(self):
        return f"Fuel level: {self.arriving_fuel_level}, Fuel consumption rate: {self.fuel_consumption_rate}, Expected landing time: {self.expected_landing_time}, Actual landing time: {self.actual_landing_time}, Safe Landing: {self.safe}"
        

    def is_gonna_crash(self):
        
        actual_fuel_needed = self.fuel_consumption_rate * self.actual_landing_time
        
        return self.arriving_fuel_level < actual_fuel_needed
    
    def ensure_enough_fuel(self):
        fuel_needed = self.fuel_consumption_rate * 60
        fuel_left = (self.arriving_fuel_level - self.fuel_consumption_rate*self.expected_landing_time)
        return fuel_left >= fuel_needed

# Done 
class LandingStrip:
    def __init__(self):
        self.current_airplanes = []  # List of airplanes currently on the landing strip
        self.empty_time = 0  # Time when the landing strip will be empty

    def add_airplane(self, airplane):
        self.current_airplanes.append(airplane)

    def remove_airplane(self, airplane):
        self.current_airplanes.remove(airplane)

    def set_empty_time(self, time):
        self.empty_time = time

    def get_empty_time(self):
        return self.empty_time

    def is_empty(self):
        return len(self.current_airplanes) == 0

    def get_current_airplanes(self):
        return self.current_airplanes
    
    def count_unsafe_airplanes(self):
        return sum(1 for airplane in self.current_airplanes if not airplane.safe)
    
    def generateResults(airplanes):
        landing_strips = [LandingStrip() for _ in range(3)]
        landed_airplanes = set()

        for airplane in airplanes:
            for landing_strip in landing_strips:
                if airplane not in landed_airplanes:
                    landing_strip.land_airplane(airplane, landing_strips)
                    landed_airplanes.add(airplane)
                    break
        sum_difference = 0
        unsafe_waiting = 0
        num_of_crashes= 0
        
        for airplane in airplanes:
            
            sum_difference += airplane.actual_landing_time - airplane.expected_landing_time
            if(airplane.actual_landing_time - airplane.expected_landing_time!=0 and not airplane.safe):
                unsafe_waiting += 1
            if(airplane.is_gonna_crash()):
                 
                 num_of_crashes += 1
                
       
        return landing_strips, sum_difference, unsafe_waiting, num_of_crashes


    def land_airplane(self, airplane, landing_strips):
        
        if airplane.expected_landing_time >= self.empty_time:
            # If the expected landing time is after the current empty time, no waiting is needed
            max_empty_time = max(landing_strip.get_empty_time() for landing_strip in landing_strips)
            actual_landing_time = max(max_empty_time,airplane.expected_landing_time)
            self.empty_time = actual_landing_time + 3
            airplane.actual_landing_time = actual_landing_time
            self.add_airplane(airplane)
        else:
            # If the expected landing time is before the current empty time, adjust accordingly
            max_empty_time = max(landing_strip.get_empty_time() for landing_strip in landing_strips)
            min_empty_time_strip = min(range(len(landing_strips)), key=lambda i: landing_strips[i].get_empty_time())
            min_empty_time = landing_strips[min_empty_time_strip].get_empty_time()
            actual_landing_time = max(max_empty_time - 3, max(airplane.expected_landing_time, min_empty_time))
            landing_strips[min_empty_time_strip].set_empty_time(actual_landing_time + 3)
            airplane.actual_landing_time = actual_landing_time
            landing_strips[min_empty_time_strip].add_airplane(airplane)

# Done
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
    not_selected = []
    avg_fitness = []
    avg_not_selected = []
    for i, fitness in enumerate(cumulative_probability):
        if rand <= fitness:
            selected.append(chromosomes[i][0])
            avg_fitness.append(fitness)
        else:
            not_selected.append(chromosomes[i][0])
            avg_not_selected.append(fitness)

    if len(selected) % 2 != 0:
        popped_chromosome = selected.pop()
        not_selected.append(popped_chromosome)  # Append fitness

    return selected, not_selected


def reproduction(chromosome1, chromosome2):
    """
    This function takes two chromosomes and returns a new offspring chromosome.

    Parameters:
    chromosome1 (List[Airplane]): The first chromosome.
    chromosome2 (List[Airplane]): The second chromosome.

    Returns:
    List[Airplane]: The offspring chromosome.
    """
    n = len(chromosome1)
    point1 = random.randint(0, n - 1)
    point2 = random.randint(0, n - 1)
    # Ensure point2 is greater than point1
    if point2 < point1:
        point1, point2 = point2, point1
    # Perform crossover
    new_chromosome1 = chromosome1[:point1] + [gene for gene in chromosome2 if gene not in (chromosome1[:point1]+chromosome1[point2:])] + chromosome1[point2:]
    new_chromosome2 = chromosome2[:point1] + [gene for gene in chromosome1 if gene not in (chromosome2[:point1]+chromosome2[point2:])] + chromosome2[point2:]
    return new_chromosome1, new_chromosome2


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
        if go_to_mutation < 0.1:
            new_chromosome = chromosome
            new_chromosome = mutation(chromosome)
            new_generation.append(new_chromosome)
        else:
            new_generation.append(chromosome)

    
    return new_generation


# Doing
def geneticAI(airplanes, population_size, max_number_of_iterations, selection_method):
    population = generate_chromosomes(airplanes, population_size)
    current_fitness_of_best_chromosome = 0
    best_chromosome = None

    for _ in range(max_number_of_iterations):
        population_fitness = []
        # Evaluate fitness for each chromosome in the population
        for chromosome in population:
            _, fitness, _, _ = LandingStrip.generateResults(chromosome)
            population_fitness.append((chromosome, fitness))

            # Update best_chromosome and current_fitness_of_best_chromosome if a better fitness is found
            if fitness > current_fitness_of_best_chromosome:
                current_fitness_of_best_chromosome = fitness
                best_chromosome = chromosome
        print(current_fitness_of_best_chromosome)
        # Select best chromosomes for reproduction
        if selection_method == "roulette":
            best_chromosomes, _ = roulette_selection(population_fitness)
        else:
            raise ValueError("Unknown selection method: " + selection_method)

        # Generate new generation through reproduction and mutation
        size_new_gen = population_size - len(best_chromosomes)
        print(len(best_chromosomes),size_new_gen)
        new_generation = reproduction_all(best_chromosomes, size_new_gen)
        mutate_generation = mutation_all(new_generation)
        mutate_generation += best_chromosomes
        # Evaluate fitness for chromosomes in mutated generation
        for chromosome in mutate_generation:
            _, fitness, _, _ = LandingStrip.generateResults(chromosome)
            if fitness > current_fitness_of_best_chromosome:
                current_fitness_of_best_chromosome = fitness
                best_chromosome = chromosome

        # Update population with mutated generation
        population = mutate_generation

    return best_chromosome, current_fitness_of_best_chromosome
def main():
    chromosome_size = 10 # Number of airplane
    population_size = 100
    max_number_of_iterations = 1000
    airplanes = []
    for _ in range(0, chromosome_size):
        fuel_level = random.randint(1000, 5000)  # Random fuel level between 1000 and 2000
        fuel_consumption_rate = random.randint(15, 25)  # Random fuel consumption rate between 15 and 25
        expected_landing_time = random.randint(0, 90)  # Random expected landing time between 0 and 90
        airplane = Airplane(fuel_level, fuel_consumption_rate, expected_landing_time)
        airplanes.append(airplane)

    selection_method = "roulette"
    best_solution,best_cost = geneticAI(airplanes,population_size, max_number_of_iterations, selection_method)
    print("BEST SOLUTION:")
    print_airplanes_and_strips(best_solution)
    print("Best cost:", best_cost)

def print_airplanes_and_strips(best_solution):
    landing_strips, sum_difference, unsafe_waiting, n = LandingStrip.generateResults(best_solution)
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
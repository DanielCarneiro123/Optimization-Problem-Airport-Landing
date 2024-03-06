import random
import copy


class Airplane:
    def __init__(self):
        self.arriving_fuel_level = int(random.uniform(100000, 500000))  # Level of fuel for the plane
        self.fuel_consumption_rate = int(random.uniform(1, 2))  # Fuel consumption rate
        self.expected_landing_time = int(random.uniform(1, 10000))  # Expected time to reach the destination
        self.safe_landing = False
        self.on_time = False
        self.actual_landing_time = None
    def __eq__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.arriving_fuel_level == other.arriving_fuel_level and self.fuel_consumption_rate == other.fuel_consumption_rate and self.expected_landing_time == other.expected_landing_time and self.actual_landing_time == other.actual_landing_time and self.safe_landing == other.safe_landing and self.on_time == other.on_time 

    def print_airplane(self):
        print("\n" + "=" * 30)
        print("    Airplane Details Menu")
        print("=" * 30 + "\n")
        print(" " * 15 + "Genes\n")
        print("1. Arriving Fuel Level: {} gallons".format(self.arriving_fuel_level))
        print("2. Fuel Consumption Rate: {} gallons per minute".format(self.fuel_consumption_rate))
        print("3. Expected Landing Time: {} minutes".format(self.expected_landing_time))
        print("4. Actual Landing Time: {} minutes".format(self.actual_landing_time))
        print("5. Safe Laning Time: {} minutes".format(self.safe_landing))
        print("6. On Time: {} minutes".format(self.on_time))
        print("\n" + "=" * 30)

    def __copy__(self):
        new_airplane = Airplane()
        new_airplane.arriving_fuel_level = self.arriving_fuel_level
        new_airplane.fuel_consumption_rate = self.fuel_consumption_rate
        new_airplane.expected_landing_time = self.expected_landing_time
        new_airplane.safe_landing = self.safe_landing
        new_airplane.on_time = self.on_time
        new_airplane.actual_landing_time = self.actual_landing_time
        return new_airplane


class Airport:

    def __init__(self):
        self.runway = [0, 0, 0]

    def mutate_runway1(self, airplane):
        self.runway[0] = airplane

    def mutate_runway2(self, airplane):
        self.runway[1] = airplane

    def mutate_runway3(self, airplane):
        self.runway[2] = airplane

    def __copy__(self):
        new_airport = Airport()
        new_airport.runway = copy.copy(self.runway)
        return new_airport


def generate_chromosomes(population_size):
    """
    This function generates a list of chromosomes for a genetic algorithm.

    Parameters:
    population_size (int): The size of the population

    Returns:
    List[List[Airplane]]: A list of chromosomes
    """
    chromosome = []
    for i in range(population_size):
        chromosome.append(Airplane())
    chromosomes = []

    for i in range(population_size):
        new_chromosome = chromosome[:]
        random.shuffle(new_chromosome)
        chromosomes.append(new_chromosome)

    return chromosomes


def check_free_runway(airport, time_spent):
    """
    Check if there is a free runway at the airport.

    Parameters:
    airport (Airport): The airport object.
    time_spent (int): The time spent at the airport.

    Returns:
    int: The index of the free runway (random choice), or -1 if no runway is free.
    """
    free_runways = []

    # Check each runway for availability
    if airport.runway[0] == 0 or time_spent - airport.runway[0] >= 3:
        free_runways.append((0, airport.runway[0]))
    if airport.runway[1] == 0 or time_spent - airport.runway[1] >= 3:
        free_runways.append((1, airport.runway[1]))
    if airport.runway[2] == 0 or time_spent - airport.runway[2] >= 3:
        free_runways.append((2, airport.runway[2]))

    # Find the runway with the minimum value

    if len(free_runways) == 0:
        min_waiting_time = 3 - time_spent + min(airport.runway)
        return -1, min_waiting_time

    min_runway = min(free_runways, key=lambda x: x[1])
    # Return the index of the runway with the minimum value
    return min_runway[0], min_runway[1]


def enough_gas(airplane, time_spent):
    """
    Check if an airplane has enough fuel to reach its destination.

    Parameters:
    airplane (Airplane): The airplane object.
    time_spent (int): The time spent until the plane arrived.

    Returns:
    bool: True if the airplane has enough fuel, False otherwise.
    """
    gas_hour = airplane.fuel_consumption_rate * 60
    return airplane.arriving_fuel_level - (time_spent * airplane.fuel_consumption_rate) >= gas_hour


def on_time(airplane, time_spent):
    """
    Check if an airplane arrived on time.

    Parameters:
    airplane (Airplane): The airplane object.
    time_spent (int): The time spent until the plane arrived.

    Returns:
    bool: True if the airplane arrived on time, False otherwise.
    """
    if time_spent > airplane.expected_landing_time:
        return False
    return True


def calculate_fitness(chromosome, airport):
    """
    Calculates the fitness of a chromosome based on its performance at the airport.

    Parameters:
        chromosome (List[Airplane]): The chromosome to evaluate.
        airport (Airport): The airport object.

    Returns:
        float: The fitness of the chromosome.
    """
    fitness = 0
    time_spent = 0
    for gene in chromosome:
        if gene.expected_landing_time - time_spent > 0:
            time_spent += gene.expected_landing_time - time_spent  # If the plane can land, check if it has enough fuel and arrived on time

        runway_free, value = check_free_runway(airport, time_spent)
        if runway_free != -1:
            gene.actual_landing_time = time_spent
            check_gas = enough_gas(gene, time_spent)
            if check_gas:
                # Add 2 points if the plane has enough fuel
                fitness += 2
            check_time = on_time(gene, time_spent)
            if check_time:
                # Add 1 point if the plane arrived on time
                fitness += 1
            if runway_free == 0:
                # Mutate the first runway
                airport.mutate_runway1(time_spent)
            elif runway_free == 1:
                # Mutate the second runway
                airport.mutate_runway2(time_spent)
            else:
                # Mutate the third runway
                airport.mutate_runway3(time_spent)
        else:
            # If the plane cannot land, add 3 - min(waiting time) minutes to the time spent and check again
            time_spent += value
            gene.actual_landing_time = time_spent
            runway_free, value = check_free_runway(airport, time_spent)
            check_gas = enough_gas(gene, time_spent)
            if check_gas:
                # Add 2 points if the plane has enough fuel
                fitness += 2
            check_time = on_time(gene, time_spent)
            if check_time:
                # Add 1 point if the plane arrived on time
                fitness += 1
            if runway_free == 0:
                # Mutate the first runway
                airport.mutate_runway1(time_spent)
            elif runway_free == 1:
                # Mutate the second runway
                airport.mutate_runway2(time_spent)
            elif runway_free == 2:
                # Mutate the third runway
                airport.mutate_runway3(time_spent)
            else:
                raise ValueError("Double check on the runway is impossible to happen")
    return fitness


def get_fitness(chromosomes):
    """
    Calculates the total fitness of a population based on the fitness values of each chromosome.

    Parameters:
        chromosomes (List[Tuple[Airplane, float]]): A list of tuples containing the chromosomes and their fitness values

    Returns:
        float: The total fitness of the population
    """
    total_fitness = 0
    for chromosome, fitness in chromosomes:
        total_fitness += fitness
    return total_fitness


def order_c(chromosome):
    fitness_by_order = 0

    # Check if the chromosome has at least two genes
    if len(chromosome) >= 2:
        # Initialize the previous landing time
        prev_landing_time = chromosome[0].expected_landing_time

        # Iterate over the genes in the chromosome starting from the second one
        for gene in chromosome[1:]:
            # Compare the current landing time with the previous one
            if gene.expected_landing_time >= prev_landing_time:
                # If the landing time is in ascending order, increment the fitness score
                fitness_by_order += 1
            # Update the previous landing time for the next iteration
            prev_landing_time = gene.expected_landing_time

    return fitness_by_order

def roulette_selection(chromosomes):
    """
    Selects a subset of chromosomes using roulette wheel selection.

    Parameters:
        chromosomes (List[Tuple[Airplane, float]]): A list of tuples containing the chromosomes and their fitness values

    Returns:
        List[Airplane]: The selected chromosomes

    """
    total_fitness = get_fitness(chromosomes)
    selected = []
    not_selected = []

    selection_probabilities = [(chromosome, fitness / total_fitness) for chromosome, fitness in
                               chromosomes]
    cumulative_probabilities = [(selection_probabilities[i][0], sum([p[1] for p in selection_probabilities[:i + 1]]))
                                for i in range(len(selection_probabilities))]

    for chromosome, cumulative_prob in cumulative_probabilities:
        if cumulative_prob <= random.uniform(0, 1) or order_c(chromosome) > 0.2*len(chromosome):
            selected.append(chromosome)
        else:
            not_selected.append(chromosome)

    if len(selected) % 2 != 0:
        popped_chromosome = selected.pop()
        not_selected.append(popped_chromosome)

    return selected, not_selected


def rank_selection(chromosomes, selection_pressure):
    """
    Selects the best chromosomes from a population using rank selection with a given selection pressure.

    Parameters:
        chromosomes (List[Airplane]): The population of chromosomes.
        selection_pressure (float): The selection pressure, which determines the strength of the rank selection.

    Returns:
        List[Airplane]: The selected chromosomes.

    Raises:
        ValueError: If the selection pressure is not between 1 and 2.

    """
    n = len(chromosomes)
    selected = []

    if selection_pressure < 1 or selection_pressure > 2:
        raise ValueError("Selection pressure must be between 1 and 2")

    rank_probabilities = [(chromosome, (selection_pressure - (2 * selection_pressure - 2) * (i - 1) / (n - 1)) / n)
                          for i, (chromosome, _) in enumerate(sorted(chromosomes, key=lambda x: x[1]))]

    while len(selected) < n:
        r = random.random()
        cumulative_probability = 0

        for chromosome, probability in rank_probabilities:
            cumulative_probability += probability
            if cumulative_probability > r:
                selected.append(chromosome)
                break
    if len(selected) % 2 != 0:
        selected.pop()
    return selected


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
    new_chromosome1 = chromosome1[:point1] + [gene for gene in chromosome2 if
                                              gene not in (chromosome1[:point1] + chromosome1[point2:])] + chromosome1[
                                                                                                           point2:]
    new_chromosome2 = chromosome2[:point1] + [gene for gene in chromosome1 if
                                              gene not in (chromosome2[:point1] + chromosome2[point2:])] + chromosome2[
                                                                                                           point2:]

    return new_chromosome1, new_chromosome2


def reproduction_all(chromosomes):
    """
    This function takes a list of chromosomes and returns a new list of offspring chromosomes.

    Parameters:
    chromosomes (List[Airplane]): A list of chromosomes to be used for reproduction

    Returns:
    List[Airplane]: A list of offspring chromosomes
    """
    new_generation = []
    for i in range(0, len(chromosomes), 2):
        chromosome1 = chromosomes[i]
        chromosome2 = chromosomes[i + 1]
        c1, c2 = reproduction(chromosome1, chromosome2)
        new_generation.append(c1)
        new_generation.append(c2)
    return new_generation


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
        go_to_mutation = random.choice([0, 1])
        if go_to_mutation:
            new_chromosome = chromosome
            for _ in range(int(len(chromosome) * 0.2)):
                new_chromosome = mutation(chromosome)
            new_generation.append(new_chromosome)
        else:
            new_generation.append(chromosome)
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


def geneticAI(population_size, max_number_of_iterations, selection_method):
    airport = Airport()  # Generate an Airport object with 3 lanes for landing.

    population = generate_chromosomes(population_size)  # Generate a population with different orders for the same
    # planes.
    optimal_fitness = population_size * 3  # This is the optimal_fitness because safe landing is valued at 2 points and
    # good schedule 1 point.
    current_fitness_of_best_chromosome = 0
    i = 0
    best_chromosome = None

    while i < max_number_of_iterations and current_fitness_of_best_chromosome < optimal_fitness:

        population_fitness = []

        for chromosome in population:
            fitness = calculate_fitness(chromosome, copy.copy(airport))
            if fitness > current_fitness_of_best_chromosome:
                current_fitness_of_best_chromosome = fitness
                best_chromosome = chromosome
            population_fitness.append((chromosome, fitness))
        # Selection of the best chromosomes according to a heuristic  #To check
        if selection_method == "roulette":
            best_chromosomes, not_selected = roulette_selection(population_fitness)
        elif selection_method == "rank":
            pressure = random.uniform(1, 2)
            best_chromosomes = rank_selection(population_fitness, pressure)
        else:
            raise ValueError("Unknown selection method: " + selection_method)

        new_generation = reproduction_all(best_chromosomes)  # Change mutation and reproduction
        mutate_generation = mutation_all(new_generation)  # Done
        mutate_generation += not_selected

        for chromosome in mutate_generation:
            fitness = calculate_fitness(chromosome, copy.copy(airport))
            if fitness > current_fitness_of_best_chromosome:
                current_fitness_of_best_chromosome = fitness
                best_chromosome = chromosome

        population = mutate_generation
        i += 1
    return best_chromosome, current_fitness_of_best_chromosome

def test_fitness(chromosome,airport):
    fitness = 0
    time_spent = 0
    for gene in chromosome:
        if gene.expected_landing_time - time_spent > 0:
            time_spent += gene.expected_landing_time - time_spent  # If the plane can land, check if it has enough fuel and arrived on time

        runway_free, value = check_free_runway(airport, time_spent)
        if runway_free != -1:
            gene.actual_landing_time = time_spent
            check_gas = enough_gas(gene, time_spent)
            if check_gas:
                gene.safe_landing = True
                # Add 2 points if the plane has enough fuel
                fitness += 2
            else:
                gene.safe_landing = False
            check_time = on_time(gene, time_spent)
            if check_time:
                gene.on_time = True
                # Add 1 point if the plane arrived on time
                fitness += 1
            else:
                gene.on_time = False
            if runway_free == 0:
                # Mutate the first runway
                airport.mutate_runway1(time_spent)
            elif runway_free == 1:
                # Mutate the second runway
                airport.mutate_runway2(time_spent)
            else:
                # Mutate the third runway
                airport.mutate_runway3(time_spent)
        else:
            # If the plane cannot land, add 3 - min(waiting time) minutes to the time spent and check again
            time_spent += value
            gene.actual_landing_time = time_spent
            runway_free, value = check_free_runway(airport, time_spent)
            check_gas = enough_gas(gene, time_spent)
            if check_gas:
                gene.safe_landing = True
                # Add 2 points if the plane has enough fuel
                fitness += 2
            else:
                gene.safe_landing = False
            check_time = on_time(gene, time_spent)
            if check_time:
                gene.on_time = True
                # Add 1 point if the plane arrived on time
                fitness += 1
            else:
                gene.on_time = False
            if runway_free == 0:
                # Mutate the first runway
                airport.mutate_runway1(time_spent)
            elif runway_free == 1:
                # Mutate the second runway
                airport.mutate_runway2(time_spent)
            elif runway_free == 2:
                # Mutate the third runway
                airport.mutate_runway3(time_spent)
            else:
                raise ValueError("Double check on the runway is impossible to happen")
    return fitness

def print_results(chromosome,fitness):
    airport = Airport()
    test_fitness(chromosome,copy.copy(airport))
    count_time = 0
    count_safe = 0
    count_crashes = 0
    count_late = 0
    print(2)
    for gene in chromosome:
        if gene.on_time == True:
            count_time += 1
        else:
            count_late += 1
        
        if gene.safe_landing == True:
            count_safe += 1
        else:
            count_crashes += 1

        gene.print_airplane()

    print("The number of planes that arrived at time: {}".format(count_time))
    print("The number of planes that arrived late: {}".format(count_late))
    print("The number of planes that arrived safely: {}".format(count_safe))
    print("The number of planes that crashed: {}".format(count_crashes))

    max_fit_score = 3*len(chromosome)
    print("The max fitness score is {} and the fitness for the optimal chromosome is {}".format(max_fit_score,fitness))

    


def main():
    population_size = 100
    max_number_of_iterations = 100
    selection_method = "roulette"
    best_chromosome, fitness = geneticAI(population_size, max_number_of_iterations, selection_method)
    print_results(best_chromosome, fitness)

if __name__ == "__main__":
    main()
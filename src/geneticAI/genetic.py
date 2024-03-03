import random


class Airplane:
    def __init__(self):
        self.arriving_fuel_level = int(random.uniform(1000, 5000))  # Level of fuel for the plane
        self.fuel_consumption_rate = int(random.uniform(5, 20))  # Fuel consumption rate
        self.expected_landing_time = int(random.uniform(10, 120))  # Expected time to reach the destination

    def mutate_airplane(self, other_airplane):
        self.arriving_fuel_level = other_airplane.arriving_fuel_level
        self.fuel_consumption_rate = other_airplane.fuel_consumption_rate
        self.expected_landing_time = other_airplane.expected_

    def mutate_airplane_arriving_fuel_level(self, other_airplane):
        self.arriving_fuel_level = other_airplane.arriving_fuel_level

    def mutate_airplane_arriving_fuel_rate(self, other_airplane):
        self.fuel_consumption_rate = other_airplane.fuel_consumption_rate

    def mutate_airplane_arriving_time(self, other_airplane):
        self.expected_landing_time = other_airplane.expected_landing_time

    def __eq__(self, other):
        if not isinstance(other, Airplane):
            return NotImplemented
        return self.arriving_fuel_level == other.arriving_fuel_level and self.fuel_consumption_rate == other.fuel_consumption_rate and self.expected_landing_time == other.expected_landing_time

    def print_airplane(self):
        print("\n" + "=" * 30)
        print("    Airplane Details Menu")
        print("=" * 30 + "\n")
        print(" " * 15 + "Genes\n")
        print("1. Arriving Fuel Level: {} gallons".format(self.arriving_fuel_level))
        print("2. Fuel Consumption Rate: {} gallons per minute".format(self.fuel_consumption_rate))
        print("3. Expected Landing Time: {} minutes".format(self.expected_landing_time))
        print("\n" + "=" * 30)


class Airport:

    def __init__(self):
        self.runway = [0, 0, 0]

    def mutate_runway1(self, airplane):
        self.runway[0] = airplane

    def mutate_runway2(self, airplane):
        self.runway[1] = airplane

    def mutate_runway3(self, airplane):
        self.runway[2] = airplane

    def get_runway_state(self):
        return self.runway

    def print_schedule(self):
        print("\n" + "=" * 30)
        print("Airport State")
        for i, status in enumerate(self.runway):
            if status != 0:
                print(f"Runway {i + 1}: Occupied")
            else:
                print(f"Runway {i + 1}: Not Occupied")
        print("\n" + "=" * 30)


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
    gasHour = airplane.fuel_consumption_rate * 60
    if airplane.arriving_fuel_level > gasHour:
        return True
    return False


def onTime(airplane):
    if airplane.expected_landing_time < 0:
        return False
    return True


def calculate_fitness(chromosome, airport):
    fitness = 0
    for gene in chromosome:
        runway_state = airport.get_runway_state()
        runway_free = checkFreeRunway(runway_state)
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
            gene.mutate_airplane_arriving_fuel_level(gene.arriving_fuel_level - gene.fuel_consumption_rate * 3)
            gene.mutate_airplane_arriving_time(gene.expected_landing_time - 3)
            checkGas = enoughGas(gene)
            if checkGas:
                fitness += 1
            checkTime = onTime(gene)
            if checkTime:
                fitness += 1
            seed = random.randint(1, 3)
            if seed == 1:
                airport.mutate_runway1(gene)
            elif seed == 2:
                airport.mutate_runway2(gene)
            else:
                airport.mutate_runway3(gene)
    return fitness


def get_fitness(chromosomes):
    total_fitness = 0
    for (_, fitness) in chromosomes:
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
    airport = Airport()

    population = generate_chromosomes(population_size)

    while True:
        population_fitness = []
        initial_fitness = 0

        for chromosome in population:
            fitness = calculate_fitness(chromosome, airport)
            initial_fitness += fitness
            population_fitness.append((chromosome, fitness))

        if selection_method == "roulette":
            best_chromosomes = roulette_selection(population_fitness)
        elif selection_method == "rank":
            best_chromosomes = rank_selection(population_fitness)
        else:
            raise ValueError("Unknown selection method: " + selection_method)

        new_generation = reproduction_all(best_chromosomes) # Change mutation and reproduction
        mutate_generation = mutation(new_generation)
        new_fitness = sum(calculate_fitness(chromosome, airport) for chromosome in mutate_generation)

        if new_fitness > initial_fitness:
            break

        population = mutate_generation

    return population

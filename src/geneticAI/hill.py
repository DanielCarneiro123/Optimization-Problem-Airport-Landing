import random

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



def cost_function(solution):
    cost = 0
    for landing_strip in solution:
        for airplane in landing_strip.get_current_airplanes():  # Acesse a lista de aviões dentro de cada landing strip
            delay = airplane.get_actual_landing_time() - airplane.get_expected_landing_time()
            if delay > 0 and airplane.get_priority() == 1:
                cost += delay
            elif airplane.get_priority() > 1:
                cost += airplane.get_priority()
            elif delay > 0 and airplane.get_priority() > 1:
                cost += delay + airplane.get_priority()
            else:
                cost += airplane.get_priority()
    return cost





def generate_initial_solution(airplanes):
    # Sort airplanes based on a combination of expected landing time and fuel level
    # initial_solution = sorted(airplanes, key=lambda x: (x.expected_landing_time, -x.arriving_fuel_level))
    return airplanes


def generate_neighbors(airplanes):
    neighbors = []
    num_airplanes = len(airplanes)
    
    # Generate neighbors by swapping the landing order of pairs of airplanes
    for i in range(num_airplanes):
        for j in range(i + 1, num_airplanes):
            neighbor = airplanes[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    
    return neighbors
    
def hill_climbing(airplanes, max_iterations=1000):
    current_solution = generate_initial_solution(airplanes)
    _,current_cost,_,_ = LandingStrip.generateResults(current_solution)
    iteration = 0

    while iteration < max_iterations:
        neighbors = generate_neighbors(current_solution)
        cost_neighbor = float('-inf')
        best_neighbor = None
        for neighbor in neighbors:
            _,neighbor_value,_,_ = LandingStrip.generateResults(neighbor)

            if neighbor_value > cost_neighbor:
                current_solution = neighbor
                cost_neighbor = neighbor_value
                best_neighbor = neighbor


        if (cost_neighbor <= current_cost):
            return current_solution,current_cost
        current_solution = best_neighbor
        current_cost = cost_neighbor
        iteration += 1
    return current_solution,current_cost


# Uso do algoritmo
def main():
    airplanes = []
    for _ in range(1, 61):
        fuel_level = random.randint(1000, 5000)  # Random fuel level between 1000 and 2000
        fuel_consumption_rate = random.randint(15, 25)  # Random fuel consumption rate between 15 and 25
        expected_landing_time = random.randint(0, 90)  # Random expected landing time between 0 and 90
        airplane = Airplane(fuel_level, fuel_consumption_rate, expected_landing_time)
        airplanes.append(airplane)   
    best_solution, best_cost = hill_climbing(airplanes)
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
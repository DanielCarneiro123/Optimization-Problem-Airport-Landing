

import copy
import random
import itertools

class Airplane:
    def __init__(self, fuel_level, fuel_consumption_rate, expected_landing_time):
        self.arriving_fuel_level = fuel_level
        self.fuel_consumption_rate = fuel_consumption_rate
        self.expected_landing_time = expected_landing_time
        self.actual_landing_time = None
        self.safe = self.ensure_enough_fuel()

    def __str__(self):
        return f"Fuel level: {self.arriving_fuel_level}, Fuel consumption rate: {self.fuel_consumption_rate}, Expected landing time: {self.expected_landing_time}, Actual landing time: {self.actual_landing_time}, Safety: {self.safe}"

    def ensure_enough_fuel(self):
        fuel_needed = self.fuel_consumption_rate * 60
        # Ensure arriving fuel level is enough for one hour of flight
        return self.arriving_fuel_level >= fuel_needed
    
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
    
    def count_unsafe_airplanes(self):
        return sum(1 for airplane in self.current_airplanes if not airplane.safe)

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


    

    def generateResults(airplanes):
        landing_strips = [LandingStrip() for _ in range(3)]
        landed_airplanes = set()

        # Simulate landing airplanes on strips
        for airplane in airplanes:
            for landing_strip in landing_strips:
                if airplane not in landed_airplanes:
                    landing_strip.land_airplane(airplane, landing_strips)
                    landed_airplanes.add(airplane)
                    break
        sum_difference = 0
        unsafe_waiting = 0
        # Calculate the sum of differences between actual and expected landing times for the current solution
        for airplane in airplanes:
            sum_difference += airplane.actual_landing_time - airplane.expected_landing_time
            if(airplane.actual_landing_time - airplane.expected_landing_time!=0 and not airplane.safe):
                unsafe_waiting += 1
                
       
        return landing_strips, sum_difference, unsafe_waiting


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


def generate_initial_solution(airplanes):
    # Sort airplanes based on a combination of expected landing time and fuel level
   #better if no unsafelandings initial_solution = sorted(airplanes, key=lambda x: (x.expected_landing_time, -x.arriving_fuel_level))
    return airplanes


def tabu_search(max_iterations, tabu_size, airplanes):
    current_solution = generate_initial_solution(airplanes)
    best_solution = current_solution
    best_solution_value = float('inf')  # Initialize best_solution_value
    tabu_list = []
    unsafe_planes = 100000  # Initialize to a large value

    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_solution)  # You can optimize this step
        
        
        # Find the best non-tabu neighbor
        best_neighbor = None
        best_neighbor_value = float('inf')
        
        for neighbor in neighbors:
                
            if neighbor not in tabu_list:
                landing_strips, neighbor_value, unsafe_waiting = LandingStrip.generateResults(neighbor)
               
                if (((neighbor_value < best_neighbor_value) and (unsafe_waiting <= unsafe_planes)) or (unsafe_waiting<unsafe_planes)):
                    
                    best_neighbor = neighbor
                    best_neighbor_value = neighbor_value
                    unsafe_planes = unsafe_waiting
                    


        # If no non-tabu neighbors found, break
        if best_neighbor is None:
            break

        # Update current solution
        current_solution = best_neighbor
        
        # Update best solution if necessary
        if best_neighbor_value < best_solution_value:
            best_solution = current_solution
            best_solution_value = best_neighbor_value

        # Update tabu list
        tabu_list.append(best_neighbor)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    return best_solution





def main():
     
    airplane1 = Airplane(1300, 20, 1)
    airplane2 = Airplane(1500, 20, 2)
    airplane3 = Airplane(1300, 20, 3)
    airplane4 = Airplane(1600, 20, 89)
    airplane5 = Airplane(1100, 20, 49)
    airplane6 = Airplane(1600, 20, 39)
    airplane7 = Airplane(1600, 20, 29)
    airplane8 = Airplane(1600, 20, 19)
    airplane9 = Airplane(1600, 20, 9)
    airplane10 = Airplane(1600, 20, 9)
    airplane11 = Airplane(1300, 20, 90)
    airplane12 = Airplane(1500, 20, 89)
    airplane13 = Airplane(1300, 20, 490)
    airplane14 = Airplane(1300, 20, 89)
    airplane15 = Airplane(1300, 20, 149)
    airplane16 = Airplane(1600, 20, 39)
    airplane17 = Airplane(1600, 20, 29)
    airplane18 = Airplane(1600, 20, 19)
    airplane19 = Airplane(1600, 20, 9)
    airplane20 = Airplane(1600, 20, 9)
    airplane21 = Airplane(1300, 20, 90)
    airplane22 = Airplane(1500, 20, 89)
    airplane23 = Airplane(1300, 20, 90)
    airplane24 = Airplane(1600, 20, 589)
    airplane25 = Airplane(1300, 20, 49)
    airplane26 = Airplane(1600, 20, 39)
    airplane27 = Airplane(1600, 20, 29)
    airplane28 = Airplane(1600, 20, 19)
    airplane29 = Airplane(1600, 20, 9)
    airplane30 = Airplane(1600, 20, 559)
    airplane31 = Airplane(1300, 20, 90)
    airplane32 = Airplane(1500, 20, 89)
    airplane33 = Airplane(1300, 20, 590)
    airplane34 = Airplane(1600, 20, 89)
    airplane35 = Airplane(1300, 20, 49)
    airplane36 = Airplane(1600, 20, 39)
    airplane37 = Airplane(1600, 20, 529)
    airplane38 = Airplane(1600, 20, 19)
    airplane39 = Airplane(1600, 20, 9)
    airplane40 = Airplane(1600, 20, 9)
    airplane41 = Airplane(1300, 20, 490)
    airplane42 = Airplane(1500, 20, 89)
    airplane43 = Airplane(1300, 20, 90)
    airplane44 = Airplane(1600, 20, 489)
    airplane45 = Airplane(1300, 20, 49)
    airplane46 = Airplane(1600, 20, 39)
    airplane47 = Airplane(1600, 20, 29)
    airplane48 = Airplane(1600, 20, 19)
    airplane49 = Airplane(1600, 20, 449)
    airplane50 = Airplane(1100, 20, 9)

    # Store airplanes in a list
    airplanes = [airplane1, airplane2, airplane3, airplane4, airplane5, airplane6, airplane7, airplane8, airplane9, airplane10,
                airplane11, airplane12, airplane13, airplane14, airplane15, airplane16, airplane17, airplane18, airplane19, airplane20,
                airplane21, airplane22, airplane23, airplane24, airplane25, airplane26, airplane27, airplane28, airplane29, airplane30,
                airplane31, airplane32, airplane33, airplane34, airplane35, airplane36, airplane37, airplane38, airplane39, airplane40,
                airplane41, airplane42, airplane43, airplane44, airplane45, airplane46, airplane47, airplane48, airplane49, airplane50]
    
    
   
    

    



    # Perform tabu search
    best_solution = tabu_search(max_iterations=300, tabu_size=10, airplanes=airplanes)

    # Print the best solution
    print("BEST SOLUTION:")
    print_airplanes_and_strips(best_solution)


def print_airplanes_and_strips(best_solution):
    landing_strips, sum_difference, unsafe_waiting = LandingStrip.generateResults(best_solution)
    print("Sum of differences between actual and expected landing times:", sum_difference)
    for i, landing_strip in enumerate(landing_strips):
        print(f"Landing Strip {i}:")
        for airplane in landing_strip.current_airplanes:
            print(airplane)
    print("Unsafe waiting:", unsafe_waiting)

if __name__ == "__main__":
    main()

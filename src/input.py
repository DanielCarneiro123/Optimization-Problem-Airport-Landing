

import copy
import random
import itertools

from numpy import sort

class Airplane:
    def __init__(self, fuel_level, fuel_consumption_rate, expected_landing_time):
        self.arriving_fuel_level = fuel_level
        self.fuel_consumption_rate = fuel_consumption_rate
        self.expected_landing_time = expected_landing_time
        self.actual_landing_time = None
        self.safe = self.ensure_enough_fuel()
        

    def __str__(self):
        return f"Fuel level: {self.arriving_fuel_level}, Fuel consumption rate: {self.fuel_consumption_rate}, Expected landing time: {self.expected_landing_time}, Actual landing time: {self.actual_landing_time}, Safety: {self.safe}"

    
  
    
    
    def is_gonna_crash_init(self):
        
        actual_fuel_needed = self.fuel_consumption_rate * self.expected_landing_time
        
        return self.arriving_fuel_level < actual_fuel_needed
    
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
        num_of_crashes= 0
        
        # Calculate the sum of differences between actual and expected landing times for the current solution
        for airplane in airplanes:
            
            sum_difference += airplane.actual_landing_time - airplane.expected_landing_time
            if(airplane.actual_landing_time - airplane.expected_landing_time!=0 and not airplane.safe):
                unsafe_waiting += 1
            if(airplane.is_gonna_crash()):
                 
                 num_of_crashes += 1
                
       
        return landing_strips, sum_difference, unsafe_waiting, num_of_crashes


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
    initial_solution = sorted(airplanes, key=lambda x: (x.expected_landing_time, -x.arriving_fuel_level))
    return initial_solution


def tabu_search(max_iterations, tabu_size, airplanes):
    current_solution = generate_initial_solution(airplanes)
    best_solution = current_solution
    best_solution_value = float('inf')  # Initialize best_solution_value
    tabu_list = []
    unsafe_planes = 100000  # Initialize to a large value
    unsafe_planes_sol = 100000  # Initialize to a large value
    num_of_crashes = 100000
    num_of_crashes_sol = 100000

    for _ in range(max_iterations):
        neighbors = generate_neighbors(current_solution)  # You can optimize this step
        
        
        # Find the best non-tabu neighbor
        best_neighbor = None
        best_neighbor_value = float('inf')
        #print("new batch")
        for neighbor in neighbors:
            #print("new neighbor")
            #for a in neighbor:
             #   print(a)
            
            if neighbor not in tabu_list:
                landing_strips, neighbor_value, unsafe_waiting, curr_num_of_crashes = LandingStrip.generateResults(neighbor)
               
                if (((neighbor_value < best_neighbor_value) and (unsafe_waiting <= unsafe_planes) and (curr_num_of_crashes<=num_of_crashes)) or ((unsafe_waiting<unsafe_planes) and (curr_num_of_crashes <= num_of_crashes) ) or (curr_num_of_crashes < num_of_crashes)):
                    
                    best_neighbor = neighbor
                    best_neighbor_value = neighbor_value
                    unsafe_planes = unsafe_waiting
                    num_of_crashes = curr_num_of_crashes
                    


        # If no non-tabu neighbors found, break
        if best_neighbor is None:
            break

        # Update current solution
        current_solution = best_neighbor

      
          
        
        # Update best solution if necessary
        if ((best_neighbor_value < best_solution_value) and (unsafe_planes<= unsafe_planes_sol) and (num_of_crashes<=num_of_crashes_sol)) or ((unsafe_planes<unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or (num_of_crashes < num_of_crashes_sol):
            
            best_solution = current_solution
            best_solution_value = best_neighbor_value
            unsafe_planes_sol = unsafe_planes
            num_of_crashes_sol = num_of_crashes

        # Update tabu list
        tabu_list.append(best_neighbor)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    return best_solution




def main():
    

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
    airplane11 = Airplane(2700, 21, 30)
    airplane12 = Airplane(1900, 17, 75)
    airplane13 = Airplane(2300, 26, 45)
    airplane14 = Airplane(1400, 14, 55)
    airplane15 = Airplane(3000, 29, 5)
    airplane16 = Airplane(1750, 19, 65)
    airplane17 = Airplane(2100, 23, 20)
    airplane18 = Airplane(2600, 27, 25)
    airplane19 = Airplane(1700, 13, 35)
    airplane20 = Airplane(2400, 20, 15)
    airplane21 = Airplane(2600, 22, 80)
    airplane22 = Airplane(1500, 16, 65)
    airplane23 = Airplane(2200, 28, 30)
    airplane24 = Airplane(2800, 25, 45)
    airplane25 = Airplane(1900, 12, 90)
    airplane26 = Airplane(1400, 19, 50)
    airplane27 = Airplane(3000, 24, 75)
    airplane28 = Airplane(2000, 17, 25)
    airplane29 = Airplane(2500, 30, 60)
    airplane30 = Airplane(1800, 14, 40)
    airplane31 = Airplane(2700, 23, 10)
    airplane32 = Airplane(1700, 27, 20)
    airplane33 = Airplane(2300, 15, 20)
    airplane34 = Airplane(1600, 21, 55)
    airplane35 = Airplane(2900, 18, 95)
    airplane36 = Airplane(2100, 26, 35)
    airplane37 = Airplane(2400, 13, 5)
    airplane38 = Airplane(2300, 29, 70)
    airplane39 = Airplane(2500, 22, 15)
    airplane40 = Airplane(1900, 16, 50)
    airplane41 = Airplane(1800, 20, 85)
    airplane42 = Airplane(2700, 24, 30)
    airplane43 = Airplane(1400, 28, 20)
    airplane44 = Airplane(3000, 17, 25)
    airplane45 = Airplane(2200, 19, 90)
    airplane46 = Airplane(1600, 27, 55)
    airplane47 = Airplane(2100, 15, 20)
    airplane48 = Airplane(2900, 25, 75)
    airplane49 = Airplane(1700, 23, 5)
    airplane50 = Airplane(2300, 30, 40)
    airplane51 = Airplane(2000, 14, 70)
    airplane52 = Airplane(2500, 18, 35)
    airplane53 = Airplane(1900, 26, 20)
    airplane54 = Airplane(2700, 16, 15)
    airplane55 = Airplane(1400, 22, 50)
    airplane56 = Airplane(2800, 19, 95)
    airplane57 = Airplane(2200, 27, 25)
    airplane58 = Airplane(1600, 23, 60)
    airplane59 = Airplane(3000, 15, 10)
    airplane60 = Airplane(1800, 21, 45)

   


    # Store airplanes in a list
    airplanes = [airplane1, airplane2, airplane9, airplane10
                 , airplane5, airplane6, airplane7, airplane8, airplane3, airplane4,
                airplane11, airplane12, airplane13, airplane14, airplane15, airplane16, airplane17, airplane18, airplane19, airplane20,
                airplane21, airplane22, airplane23, airplane24, airplane25, airplane26, airplane27, airplane28, airplane29, airplane30,
                airplane31, airplane32, airplane33, airplane34, airplane35, airplane36, airplane37, airplane38, airplane39, airplane40,
                airplane41, airplane42, airplane43, airplane44, airplane45, airplane46, airplane47, airplane48, airplane49, airplane50,
                 airplane51, airplane52, airplane53, airplane54, airplane55, airplane56, airplane57, airplane58, airplane59, airplane60]
    
    '''
    counter = 0
    for airplane in airplanes:
        counter += 1
        if airplane.is_gonna_crash_init():
            print(counter)
            print("isgonna crash")
    '''

    # Perform tabu search
    best_solution = tabu_search(max_iterations=4, tabu_size=100, airplanes=airplanes)

    # Print the best solution
    print("BEST SOLUTION:")
    print_airplanes_and_strips(best_solution)
    
        


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

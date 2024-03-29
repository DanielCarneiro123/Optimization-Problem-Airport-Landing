
import random
from airplane import *
from landing_strip import *



def print_improved_solution(landing_strips):
    output = ""
    
    
    for i, landing_strip in enumerate(landing_strips):
        output += f"Landing Strip {i}:\n"
        for airplane in landing_strip.current_airplanes:
            output += str(airplane) + "\n"
            if airplane.is_gonna_crash():
                output += "Crashed\n"
    
    return output

def print_airplanes_and_strips(best_solution):
        landing_strips, sum_difference, unsafe_waiting, n = generateResults(best_solution)
        print("Sum of differences between actual and expected landing times:", sum_difference)
        for i, landing_strip in enumerate(landing_strips):
            print(f"Landing Strip {i}:")
            for airplane in landing_strip.current_airplanes:
                print(airplane)
                if (airplane.is_gonna_crash()):
                    print("Crashed")
        print("Crashes:", n)
        print("Unsafe waiting:", unsafe_waiting)


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
    
    # Swap neighboring elements
    for i in range(num_airplanes - 1):
        neighbor = airplanes[:]
        neighbor[i], neighbor[i + 1] = neighbor[i + 1], neighbor[i]
        neighbors.append(neighbor)
    
    # Introduce occasional random swaps to explore other areas
    for _ in range(num_airplanes):
        i, j = random.sample(range(num_airplanes), 2)
        neighbor = airplanes[:]
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        neighbors.append(neighbor)
    
    return neighbors


def generate_initial_solution(airplanes):
    
    initial_solution = sorted(airplanes, key=lambda x: (x.expected_landing_time, x.arriving_fuel_level/x.fuel_consumption_rate))
    return initial_solution

def generate_initial_solution2(airplanes):
    
    initial_solution = airplanes[:]
    
    random.shuffle(initial_solution)
    return initial_solution

def generate_initial_solution3(airplanes):
    # Sort airplanes based on a combination of expected landing time
    initial_solution = sorted(airplanes, key=lambda x: (x.expected_landing_time))
    return initial_solution

import random

def generate_neighbors_random_swaps(airplanes):
    neighbors = []
    num_airplanes = len(airplanes)
    
    
    for _ in range(num_airplanes): 
        neighbor = airplanes[:]
        i, j = random.sample(range(num_airplanes), 2)
        neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
        neighbors.append(neighbor)
    
    return neighbors

def generate_neighbors_comb(airplanes):
    neighbors = []
    num_airplanes = len(airplanes)
    
    for i in range(num_airplanes):
        for j in range(1, min(i + 2, num_airplanes - i + 1)):
            neighbor = airplanes[:]
            neighbor[i], neighbor[(i+j)%num_airplanes] = neighbor[(i+j)%num_airplanes], neighbor[i]
            neighbors.append(neighbor)
            i, j = random.sample(range(num_airplanes), 2)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    
    return neighbors



from airplane import *
from landing_strip import *
from utils import *
import random
import pandas as pd
import math
import copy
import random


def simulated_annealing(airplanes, initial_temperature=1000, cooling_rate=0.99, stopping_temperature=0.01, max_iterations=1000):
    current_solution = generate_initial_solution(airplanes)
    best_solution = current_solution
    landing_strips, neighbor_value, unsafe_planes, num_of_crashes = generateResults(current_solution)
    best_cost = neighbor_value
    best_landing_strip = landing_strips
    unsafe_planes_sol = unsafe_planes
    num_of_crashes_sol = num_of_crashes
    temperature = initial_temperature
    iteration = 0
    with open("output.txt", 'w') as file:
        while (temperature > stopping_temperature) and (iteration < max_iterations):
            neighbors = generate_neighbors_random_swaps(best_solution)
            best_neighbor = None
            best_neighbor_value = float('inf')
            num_of_crashes = 100000
            unsafe_planes = 100000 
            for neighbor in neighbors:
                landing_strips, neighbor_value, unsafe_waiting, curr_num_of_crashes = generateResults(neighbor)
                if (((neighbor_value < best_neighbor_value) and (unsafe_waiting <= unsafe_planes) and (curr_num_of_crashes<=num_of_crashes)) or ((unsafe_waiting<unsafe_planes) and (curr_num_of_crashes <= num_of_crashes) ) or (curr_num_of_crashes < num_of_crashes)):
                    best_neighbor_value = neighbor_value
                    best_neighbor = neighbor
                    unsafe_planes = unsafe_waiting
                    num_of_crashes = curr_num_of_crashes
                    best_solution_landing_strips = landing_strips

            if ((best_neighbor_value < best_cost) and (unsafe_planes <= unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or ((unsafe_planes < unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or (num_of_crashes < num_of_crashes_sol) or min(1, math.exp(-(best_neighbor_value - best_cost) / temperature)) > random.random():
                #file.write(f"New Best Solution:\n" + print_improved_solution(best_solution_landing_strips) + "\n")
                best_solution = best_neighbor
                best_cost = best_neighbor_value
                unsafe_planes_sol = unsafe_planes
                num_of_crashes_sol = num_of_crashes
                file.write(f"New Best Solution Value: {best_cost}\n")
                file.write(f"Unsafe Planes: {unsafe_planes_sol}\n")
                file.write(f"Number of Crashes: {num_of_crashes_sol}\n")
                file.write('\n')

            temperature *= cooling_rate
            iteration += 1

    return best_solution, best_cost


def print_improved_solution(landing_strips):
        output = ""
        
        for i, landing_strip in enumerate(landing_strips):
            output += f"Landing Strip {i}:\n"
            for airplane in landing_strip.current_airplanes:
                output += str(airplane) + "\n"
                if airplane.is_gonna_crash():
                    output += "Crashed\n"
        
        return output
from airplane import *
from landing_strip import *
from utils import *
import random
import pandas as pd
import numpy as np
import copy
import random


def simulated_annealing(airplanes, initial_temperature=1000, cooling_rate=0.99, stopping_temperature=0.1, max_iterations=1000):
    current_solution = generate_initial_solution2(airplanes)
    best_solution = current_solution
    landing_strips, neighbor_value, unsafe_planes, num_of_crashes = generateResults(current_solution)
    best_cost = neighbor_value
    best_landing_strip = landing_strips
    unsafe_planes_sol = unsafe_planes
    num_of_crashes_sol = num_of_crashes
    temperature = initial_temperature
    iteration = 0
    unsafe_planes_sol = 100000  
    num_of_crashes_sol = 100000
    with open("output.txt", 'w') as file:
        while (temperature > stopping_temperature) and (iteration < max_iterations):
            neighbors = generate_neighbors_random_swaps(best_solution)
            for neighbor in neighbors:
                landing_strips, neighbor_value, unsafe_planes, num_of_crashes = generateResults(neighbor)
                current_solution = neighbor
                current_cost = neighbor_value
                curr_landing_strip = landing_strips
                delta_cost = current_cost - best_cost
                if (((current_cost < best_cost) and (unsafe_planes <= unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or ((unsafe_planes < unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or (num_of_crashes < num_of_crashes_sol))  or np.exp(-delta_cost / temperature) > random.random(): 
                    best_solution = neighbor
                    best_cost = neighbor_value
                    best_landing_strip = curr_landing_strip
                    unsafe_planes_sol = unsafe_planes
                    num_of_crashes_sol = num_of_crashes

            #file.write(f"New Best Solution:\n" + print_improved_solution(best_landing_strip) + "\n")
            file.write(f"Best Solution Value: {best_cost}\n")
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
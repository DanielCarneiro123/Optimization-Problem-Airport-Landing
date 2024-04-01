from airplane import *
from landing_strip import *
from utils import *
import random
import pandas as pd
import math
import copy
import random


def simulated_annealing(airplanes, initial_temperature, cooling_rate, stopping_temperature, max_iterations):
    # function that generates a possible landing schedule (could be random - generate_initial_solution2 - or initially oraganized by time and fuel - generate_initial_solution)
    current_solution = generate_initial_solution(airplanes)
    best_solution = current_solution
    #function that evaluates all solutions 
    landing_strips, neighbor_value, unsafe_planes, num_of_crashes = generateResults(current_solution)
    best_cost = neighbor_value
    best_landing_strip = landing_strips
    unsafe_planes_sol = unsafe_planes
    num_of_crashes_sol = num_of_crashes
    temperature = initial_temperature
    iteration = 0
    with open("output.txt", 'w') as file:
        while (temperature > stopping_temperature) and (iteration < max_iterations):
            #neighbouring function 
            neighbors = generate_neighbors_random_swaps(best_solution)
            best_neighbor = None
            best_neighbor_value = float('inf')
            num_of_crashes = 100000
            unsafe_planes = 100000 
            for neighbor in neighbors:
                landing_strips, neighbor_value, unsafe_waiting, curr_num_of_crashes = generateResults(neighbor)
                #updating to the best neighbouring solution
                if (((neighbor_value < best_neighbor_value) and (unsafe_waiting <= unsafe_planes) and (curr_num_of_crashes<=num_of_crashes)) or ((unsafe_waiting<unsafe_planes) and (curr_num_of_crashes <= num_of_crashes) ) or (curr_num_of_crashes < num_of_crashes)):
                    best_neighbor_value = neighbor_value
                    best_neighbor = neighbor
                    unsafe_planes = unsafe_waiting
                    num_of_crashes = curr_num_of_crashes
                    best_neighbour_landing_strips = landing_strips
            #updating to the best general solution or accepting a worst solution 
            if ((best_neighbor_value < best_cost) and (unsafe_planes <= unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or ((unsafe_planes < unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or (num_of_crashes < num_of_crashes_sol) or min(1, math.exp(-(best_neighbor_value - best_cost) / temperature)) > random.random():
                best_landing_strip = best_neighbour_landing_strips
                best_solution = best_neighbor
                best_cost = best_neighbor_value
                unsafe_planes_sol = unsafe_planes
                num_of_crashes_sol = num_of_crashes
                file.write(f"New Best Solution:\n" + print_improved_solution(best_landing_strip) + "\n")
                file.write(f"New Best Solution Value: {best_cost}\n")
                file.write(f"Unsafe Planes: {unsafe_planes_sol}\n")
                file.write(f"Number of Crashes: {num_of_crashes_sol}\n")
                file.write('\n')

            temperature *= cooling_rate
            iteration += 1

    return best_solution, best_cost


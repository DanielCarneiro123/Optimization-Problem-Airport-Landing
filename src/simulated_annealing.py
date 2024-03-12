from airplane import *
from landing_strip import *
from tabu_search import *
import random
import pandas as pd
import math
import copy
import random


def simulated_annealing(airplanes, initial_temperature=1000, cooling_rate=0.95, stopping_temperature=0.01, max_iterations=100):
    current_solution = generate_initial_solution(airplanes)
    current_cost = float('inf')
    best_solution = current_solution
    best_cost = current_cost
    temperature = initial_temperature
    iteration = 0
    unsafe_planes = 100000  # Initialize to a large value
    unsafe_planes_sol = 100000  # Initialize to a large value
    num_of_crashes = 100000
    num_of_crashes_sol = 100000

    while temperature > stopping_temperature and iteration < max_iterations:
        print("aaa")
        neighbors = generate_neighbors(current_solution)
        for neighbor in neighbors:
            landing_strips, neighbor_value, unsafe_waiting, curr_num_of_crashes = generateResults(neighbor)

            delta_cost = neighbor_value - best_cost
            if delta_cost < 0 or math.exp(-delta_cost / temperature) > random.random():
                print("dsadsa")
                best_solution = neighbor
                best_cost = neighbor_value
                unsafe_planes_sol = unsafe_planes
                num_of_crashes_sol = num_of_crashes
                
        temperature *= cooling_rate
        iteration += 1
    return best_solution, best_cost
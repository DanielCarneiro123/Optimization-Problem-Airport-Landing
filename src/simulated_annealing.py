from airplane import *
from landing_strip import *
from utils import *
import random
import pandas as pd
import math
import copy
import random


def simulated_annealing(airplanes, initial_temperature=100000, cooling_rate=0.99, stopping_temperature=0.1, max_iterations=120):
    current_solution = generate_initial_solution2(airplanes)
    current_cost = float('inf')
    best_solution = current_solution
    best_cost = current_cost
    temperature = initial_temperature
    iteration = 0
    unsafe_planes_sol = 100000  
    num_of_crashes_sol = 100000

    with open("output.txt", "w") as file:
        while (iteration < max_iterations):
            neighbors = generate_neighbors2(current_solution)
            for neighbor in neighbors:
                landing_strips, neighbor_value, unsafe_planes, num_of_crashes = generateResults(neighbor)
                current_solution = neighbor
                current_cost = neighbor_value
                delta_cost = neighbor_value - best_cost
                if (((neighbor_value < best_cost) and (unsafe_planes <= unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or ((unsafe_planes <= unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or (num_of_crashes <= num_of_crashes_sol)) and math.exp(-delta_cost / temperature) > random.random(): 
                    best_solution = neighbor
                    best_cost = neighbor_value
                    unsafe_planes_sol = unsafe_planes
                    num_of_crashes_sol = num_of_crashes

            # Escreva as informações no arquivo apenas no final de cada iteração
            file.write(f"New Best Solution:\n" + print_improved_solution(landing_strips) + "\n")
            file.write(f"Best Solution Value: {best_cost}\n")
            file.write(f"Unsafe Planes: {unsafe_planes_sol}\n")
            file.write(f"Number of Crashes: {num_of_crashes_sol}\n")
            file.write('\n')

            # Atualize a temperatura e iteração
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
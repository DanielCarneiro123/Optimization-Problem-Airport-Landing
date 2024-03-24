from airplane import *
from landing_strip import *
from tabu_search import *




    
def hill_climbing(airplanes, max_iterations=1000):
    current_solution = generate_initial_solution(airplanes)
    _,current_cost,_,_ = generateResults(current_solution)
    iteration = 0

    while iteration < max_iterations:
        neighbors = generate_neighbors(current_solution)
        cost_neighbor = float('-inf')
        best_neighbor = None
        for neighbor in neighbors:
            _,neighbor_value,_,_ = generateResults(neighbor)

            if neighbor_value < cost_neighbor:
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

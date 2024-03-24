from airplane import *
from landing_strip import *
from tabu_search import *




    
def hill_climbing(airplanes, max_iterations=1000):
    current_solution = generate_initial_solution(airplanes)
    best_solution = current_solution
    best_solution_value = float('inf')  
    unsafe_planes_sol = 100000  
    num_of_crashes_sol = 100000
    iteration = 0

    while iteration < max_iterations:
        neighbors = generate_neighbors(current_solution)
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

        if ((best_neighbor_value >= best_solution_value) and (unsafe_planes >= unsafe_planes_sol) and (num_of_crashes >= num_of_crashes_sol)) or ((unsafe_planes >= unsafe_planes_sol) and (num_of_crashes >= num_of_crashes_sol)) or (num_of_crashes >= num_of_crashes_sol):
            return best_solution,best_solution_value
        
        best_solution = best_neighbor
        best_solution_value = best_neighbor_value
        unsafe_planes_sol = unsafe_planes
        num_of_crashes_sol = num_of_crashes
        iteration += 1
    return best_solution,best_solution_value


# Uso do algoritmo

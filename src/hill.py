from airplane import *
from landing_strip import *
from utils import *

    
def hill_climbing(airplanes, output_file, max_iterations=1000):
    current_solution = generate_initial_solution(airplanes)
    best_solution = current_solution
    best_solution_landing_strips, best_solution_value, unsafe_planes_sol, num_of_crashes_sol = generateResults(best_solution) 
    iteration = 0
    with open(output_file, 'w') as f:
        while iteration < max_iterations:
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

            if ((best_neighbor_value < best_solution_value) and (unsafe_planes <= unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or ((unsafe_planes < unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or (num_of_crashes < num_of_crashes_sol):
                #f.write(f"New Best Solution:\n" + print_improved_solution(best_solution_landing_strips) + "\n")
                f.write(f"New Best Solution Value: {best_solution_value}\n")
                f.write(f"Unsafe Planes: {unsafe_planes_sol}\n")
                f.write(f"Number of Crashes: {num_of_crashes_sol}\n")
                f.write('\n')
            
            best_solution = best_neighbor
            best_solution_value = best_neighbor_value
            unsafe_planes_sol = unsafe_planes
            num_of_crashes_sol = num_of_crashes
            iteration += 1
    return best_solution,best_solution_value

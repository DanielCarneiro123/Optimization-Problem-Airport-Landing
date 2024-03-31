from airplane import *
from utils import *
from landing_strip import *




def tabu_search(max_iterations, tabu_size, airplanes, output_file):
    ini_tabu_size = tabu_size
    current_solution = generate_initial_solution(airplanes)
    best_solution = current_solution
    best_solution_value = float('inf')  # Initialize best_solution_value
    tabu_list = []
    unsafe_planes = 100000  # Initialize to a large value
    unsafe_planes_sol = 100000  # Initialize to a large value
    num_of_crashes = 100000
    num_of_crashes_sol = 100000
    stagnation_counter = 0
    max_stagnation = 10  # Maximum number of iterations to detect stagnation

    with open(output_file, 'w') as f:
        for iteration in range(max_iterations):
            hasImproved = False
            neighbors = generate_neighbors_random_swaps(current_solution) 

            # Find the best non-tabu neighbor
            best_neighbor = None
            best_neighbor_value = float('inf')
            for neighbor in neighbors:
                
                if neighbor not in tabu_list:
                    landing_strips, neighbor_value, unsafe_waiting, curr_num_of_crashes = generateResults(neighbor)
                    if (((neighbor_value < best_neighbor_value) and (unsafe_waiting <= unsafe_planes) and (curr_num_of_crashes <= num_of_crashes)) or ((unsafe_waiting < unsafe_planes) and (curr_num_of_crashes <= num_of_crashes)) or (curr_num_of_crashes < num_of_crashes)):
                        best_neighbor = neighbor
                        best_neighbor_value = neighbor_value
                        best_neighbor_landing_strips = landing_strips
                        unsafe_planes = unsafe_waiting
                        num_of_crashes = curr_num_of_crashes
                        
               

            # If no non-tabu neighbors found, break
            if best_neighbor is None:
                break

            # Update current solution
            current_solution = best_neighbor

            # Update best solution if necessary
            if ((best_neighbor_value < best_solution_value) and (unsafe_planes <= unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or ((unsafe_planes < unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or (num_of_crashes < num_of_crashes_sol):
                best_solution = current_solution
                best_solution_value = best_neighbor_value
                best_solution_landing_strips = best_neighbor_landing_strips
                unsafe_planes_sol = unsafe_planes
                num_of_crashes_sol = num_of_crashes
                hasImproved = True
                
                
                f.write(f"New Best Solution:\n" + print_improved_solution(best_solution_landing_strips) + "\n")
                f.write(f"New Best Solution Value: {best_solution_value}\n")
                f.write(f"Unsafe Planes: {unsafe_planes_sol}\n")
                f.write(f"Number of Crashes: {num_of_crashes_sol}\n")
                f.write(f"Iteration: {iteration}\n")
                f.write('\n')
                
                
                

            
            tabu_list.append(best_neighbor)
            if len(tabu_list) > tabu_size:
                tabu_list.pop(0)
            if not hasImproved:
            
                stagnation_counter += 1
            
                if stagnation_counter >= max_stagnation:
                    
                    tabu_size = int(tabu_size + pow(tabu_size, 0.5))
                    stagnation_counter = 0
                    
            else:
           
                stagnation_counter = 0
                tabu_size = ini_tabu_size

    return best_solution

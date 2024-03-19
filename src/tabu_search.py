from airplane import *
from landing_strip import *




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
    
    # Generate neighbors by swapping the landing order of pairs of airplanes
    for i in range(num_airplanes):
        for j in range(i + 1, num_airplanes):
            neighbor = airplanes[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)

    return neighbors


def generate_initial_solution(airplanes):
    # Sort airplanes based on a combination of expected landing time and fuel level
    initial_solution = sorted(airplanes, key=lambda x: (x.expected_landing_time, -x.arriving_fuel_level))
    return initial_solution


def tabu_search(max_iterations, tabu_size, airplanes):
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
    

    for iteration in range(max_iterations):
        hasImproved = False
        neighbors = generate_neighbors(current_solution)

        best_neighbor = None
        best_neighbor_value = float('inf')

        for neighbor in neighbors:
            if neighbor not in tabu_list:
                landing_strips, neighbor_value, unsafe_waiting, curr_num_of_crashes = generateResults(neighbor)
               
                if (((neighbor_value < best_neighbor_value) and (unsafe_waiting <= unsafe_planes) and (curr_num_of_crashes<=num_of_crashes)) or ((unsafe_waiting<unsafe_planes) and (curr_num_of_crashes <= num_of_crashes) ) or (curr_num_of_crashes < num_of_crashes)):
                    
                    best_neighbor = neighbor
                    best_neighbor_value = neighbor_value
                    unsafe_planes = unsafe_waiting
                    num_of_crashes = curr_num_of_crashes

        # If no non-tabu neighbors found, break
        if best_neighbor is None:
            break

        # Update current solution
        current_solution = best_neighbor
        
        # Update best solution if necessary
        if ((best_neighbor_value < best_solution_value) and (unsafe_planes<= unsafe_planes_sol) and (num_of_crashes<=num_of_crashes_sol)) or ((unsafe_planes<unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or (num_of_crashes < num_of_crashes_sol):
            
            best_solution = current_solution
            best_solution_value = best_neighbor_value
            unsafe_planes_sol = unsafe_planes
            num_of_crashes_sol = num_of_crashes
            hasImproved = True
            
        # Update tabu list
        tabu_list.append(best_neighbor)
        
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        
        # Check for stagnation
        if not hasImproved:
            print("did not improve")
            stagnation_counter += 1
            print(stagnation_counter)
            if stagnation_counter >= max_stagnation:
                print(tabu_size)
                tabu_size = int(tabu_size + pow(tabu_size, 0.5))  # Increase tabu tenure
                stagnation_counter = 0
                print("new tabu size", tabu_size)
                print("increasing tt")
        else:
            print("improved")
            stagnation_counter = 0
            tabu_size = ini_tabu_size

    return best_solution

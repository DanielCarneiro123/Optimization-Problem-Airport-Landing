from airplane import *
from landing_strip import *
from tabu_search import *
from simulated_annealing import *
from genetic import*
from hill import *
from utils import *
import time



def main():
    

    airplane1 = Airplane(2000, 15, 20)
    airplane1 = Airplane(2000, 15, 20)
    airplane2 = Airplane(2000, 25, 20)
    airplane3 = Airplane(2500, 20, 21)
    airplane4 = Airplane(2800, 18, 22)
    airplane5 = Airplane(2500, 22, 20)
    airplane6 = Airplane(2200, 12, 21)
    airplane7 = Airplane(2800, 30, 25)
    airplane8 = Airplane(2000, 28, 24)
    airplane9 = Airplane(2600, 16, 10)
    airplane3 = Airplane(2500, 20, 21)
    airplane4 = Airplane(2800, 18, 22)
    airplane5 = Airplane(2500, 22, 20)
    airplane6 = Airplane(2200, 12, 21)
    airplane7 = Airplane(2800, 30, 25)
    airplane8 = Airplane(2000, 28, 24)
    airplane9 = Airplane(2600, 16, 10)
    airplane10 = Airplane(2200, 24, 85)
    airplane11 = Airplane(2700, 21, 30)
    airplane12 = Airplane(1900, 17, 75)
    airplane13 = Airplane(2300, 26, 45)
    airplane14 = Airplane(2400, 14, 25)
    airplane15 = Airplane(3000, 29, 25)
    airplane16 = Airplane(2750, 19, 25)
    airplane14 = Airplane(2400, 14, 25)
    airplane15 = Airplane(3000, 29, 25)
    airplane16 = Airplane(2750, 19, 25)
    airplane17 = Airplane(2100, 23, 20)
    airplane18 = Airplane(2600, 27, 25)
    airplane19 = Airplane(2700, 13, 35)
    airplane19 = Airplane(2700, 13, 35)
    airplane20 = Airplane(2400, 20, 15)
    airplane21 = Airplane(2600, 22, 23)
    airplane22 = Airplane(2500, 16, 65)
    airplane21 = Airplane(2600, 22, 23)
    airplane22 = Airplane(2500, 16, 65)
    airplane23 = Airplane(2200, 28, 30)
    airplane24 = Airplane(2800, 25, 45)
    airplane25 = Airplane(2900, 12, 20)
    airplane26 = Airplane(2400, 19, 50)
    airplane25 = Airplane(2900, 12, 20)
    airplane26 = Airplane(2400, 19, 50)
    airplane27 = Airplane(3000, 24, 75)
    airplane28 = Airplane(2000, 17, 25)
    airplane29 = Airplane(2500, 30, 60)
    airplane30 = Airplane(2800, 14, 40)
    airplane30 = Airplane(2800, 14, 40)
    airplane31 = Airplane(2700, 23, 10)
    airplane32 = Airplane(2700, 27, 20)
    airplane32 = Airplane(2700, 27, 20)
    airplane33 = Airplane(2300, 15, 20)
    airplane34 = Airplane(3600, 21, 55)
    airplane34 = Airplane(3600, 21, 55)
    airplane35 = Airplane(2900, 18, 95)
    airplane36 = Airplane(3100, 26, 35)
    airplane36 = Airplane(3100, 26, 35)
    airplane37 = Airplane(2400, 13, 5)
    airplane38 = Airplane(2300, 29, 70)
    airplane39 = Airplane(2500, 22, 15)
    airplane40 = Airplane(3900, 16, 50)
    airplane41 = Airplane(3800, 20, 85)
    airplane40 = Airplane(3900, 16, 50)
    airplane41 = Airplane(3800, 20, 85)
    airplane42 = Airplane(2700, 24, 30)
    airplane43 = Airplane(3400, 28, 20)
    airplane43 = Airplane(3400, 28, 20)
    airplane44 = Airplane(3000, 17, 25)
    airplane45 = Airplane(2200, 19, 90)
    airplane46 = Airplane(2600, 27, 55)
    airplane46 = Airplane(2600, 27, 55)
    airplane47 = Airplane(2100, 15, 20)
    airplane48 = Airplane(2900, 25, 75)
    airplane49 = Airplane(3700, 23, 5)
    airplane49 = Airplane(3700, 23, 5)
    airplane50 = Airplane(2300, 30, 40)
    airplane51 = Airplane(2000, 14, 70)
    airplane52 = Airplane(2500, 18, 35)
    airplane53 = Airplane(2900, 26, 20)
    airplane53 = Airplane(2900, 26, 20)
    airplane54 = Airplane(2700, 16, 15)
    airplane55 = Airplane(1400, 22, 50)
    airplane56 = Airplane(2800, 19, 95)
    airplane57 = Airplane(2200, 27, 25)
    airplane58 = Airplane(1600, 23, 60)
    airplane59 = Airplane(3000, 15, 10)
    airplane60 = Airplane(1800, 21, 45)
    airplane61 = Airplane(2000, 15, 20)
    airplane62 = Airplane(3000, 25, 20)
    airplane63 = Airplane(1500, 20, 21)
    airplane64 = Airplane(1800, 18, 22)
    airplane65 = Airplane(2500, 22, 20)
    airplane66 = Airplane(3200, 12, 21)
    airplane67 = Airplane(2800, 30, 25)
    airplane68 = Airplane(2000, 28, 24)
    airplane69 = Airplane(1600, 16, 10)
    airplane70 = Airplane(2200, 24, 85)
    airplane71 = Airplane(2700, 21, 30)
    airplane72 = Airplane(1900, 17, 75)
    airplane73 = Airplane(2300, 26, 45)
    airplane74 = Airplane(1400, 14, 25)
    airplane75 = Airplane(3000, 29, 25)
    airplane76 = Airplane(3750, 19, 25)
    airplane77 = Airplane(2100, 23, 20)
    airplane78 = Airplane(2600, 27, 25)
    airplane79 = Airplane(1700, 13, 35)
    airplane80 = Airplane(2400, 20, 15)
    airplane81 = Airplane(2600, 22, 23)
    airplane82 = Airplane(1500, 16, 65)
    airplane83 = Airplane(2200, 28, 30)
    airplane84 = Airplane(2800, 25, 45)
    airplane85 = Airplane(3900, 12, 20)
    airplane86 = Airplane(3400, 19, 50)
    airplane87 = Airplane(3000, 24, 75)
    airplane88 = Airplane(2000, 17, 25)
    airplane89 = Airplane(2500, 30, 60)
    airplane90 = Airplane(2800, 14, 40)
    airplane91 = Airplane(2700, 23, 10)
    airplane92 = Airplane(1700, 27, 20)
    airplane93 = Airplane(2300, 15, 20)
    airplane94 = Airplane(1600, 21, 55)
    airplane95 = Airplane(2900, 18, 95)
    airplane96 = Airplane(2100, 26, 35)
    airplane97 = Airplane(2400, 13, 5)
    airplane98 = Airplane(2300, 29, 70)
    airplane99 = Airplane(2500, 22, 15)
    airplane100 = Airplane(1900, 16, 50)
    airplane101 = Airplane(1800, 20, 85)
    airplane102 = Airplane(2700, 24, 30)
    airplane103 = Airplane(3400, 28, 20)
    airplane104 = Airplane(3000, 17, 25)
    airplane105 = Airplane(2200, 19, 90)
    airplane106 = Airplane(3600, 27, 55)
    airplane107 = Airplane(2100, 15, 20)
    airplane108 = Airplane(2900, 25, 75)
    airplane109 = Airplane(1700, 23, 5)
    airplane110 = Airplane(2300, 30, 40)
    airplane111 = Airplane(2000, 14, 70)
    airplane112 = Airplane(2500, 18, 35)
    airplane113 = Airplane(1900, 26, 20)
    airplane114 = Airplane(2700, 16, 15)
    airplane115 = Airplane(1400, 22, 50)
    airplane116 = Airplane(2800, 19, 95)
    airplane117 = Airplane(2200, 27, 25)
    airplane118 = Airplane(1600, 23, 60)
    airplane119 = Airplane(3000, 15, 10)
    airplane120 = Airplane(2800, 21, 45)

   


    # Store airplanes in a list
    airplanes = [airplane1, airplane2, airplane3, airplane4
                 , airplane5, airplane6, airplane7, airplane8, airplane9, airplane10,
                airplane11, airplane12, airplane13, airplane14, airplane15, airplane16, airplane17, airplane18, airplane19, airplane20,
                airplane21, airplane22, airplane23, airplane24, airplane25, airplane26, airplane27, airplane28, airplane29, airplane30,
                airplane31, airplane32, airplane33, airplane34, airplane35, airplane36, airplane37, airplane38, airplane39, airplane40,
                airplane41, airplane42, airplane43, airplane44, airplane45, airplane46, airplane47, airplane48, airplane49, airplane50,
                 airplane51, airplane52, airplane53, airplane54, airplane55, airplane56, airplane57, airplane58, airplane59, airplane60]
    
  
    airplanes.extend([airplane61, airplane62, airplane63, airplane64, airplane65, airplane66, airplane67, airplane68, airplane69, airplane70,
                  airplane71, airplane72, airplane73, airplane74, airplane75, airplane76, airplane77, airplane78, airplane79, airplane80,
                  airplane81, airplane82, airplane83, airplane84, airplane85, airplane86, airplane87, airplane88, airplane89, airplane90,
                  airplane91, airplane92, airplane93, airplane94, airplane95, airplane96, airplane97, airplane98, airplane99, airplane100,
                  airplane101, airplane102, airplane103, airplane104, airplane105, airplane106, airplane107, airplane108, airplane109, airplane110,
                  airplane111, airplane112, airplane113, airplane114, airplane115, airplane116, airplane117, airplane118, airplane119, airplane120])

    
    airplanes = generate_initial_solution2(airplanes)

    '''
    counter = 0
    for airplane in airplanes:
        counter += 1
        if airplane.is_gonna_crash_init():
            print(counter)
            print("isgonna crash")
    '''
    string_resposta = ""

    while string_resposta != "q":
        print("==================== MENU ====================")
        print("[PRESS 1] - Tabu Search")
        print("[PRESS 2] - Simulated Annealing")
        print("[PRESS 3] - Genetic Algorithm")
        print("[PRESS 4] - Hill Climbing")
        print("[PRESS q] - Exit the menu")
        print("==============================================")
        string_resposta = input()
        if string_resposta == "q":
            break
        if string_resposta == "1":
            while True:
                print("==================== MENU ====================")
                print("How many airplanes do you wish to simulate? (1-120)")
                print("[PRESS e] - Go Back")
                print("==============================================")
                num_airplanes_input = input()
                if num_airplanes_input == "e":
                    break
        
                else:
                    try:
                        num_airplanes = int(num_airplanes_input)
                        if num_airplanes < 1 or num_airplanes > 120:
                            print("==============================================")
                            print("Please enter a number between 1 and 120.")
                            print("==============================================")
                        else:
                            # airplanes = generate_airplanes
                            print("==============================================")
                            print("How many iterations do you want to perform?")
                            print("==============================================")
                            max_iterations = int(input())
                            print("==============================================")
                            print("What should be the length of the tabu search? (A bigger tabu length leads to more diversification but to slower convergence towards optimal solution)")
                            print("==============================================")
                            tabu_size = int(input())
                            
                            start_time = time.time()

                            best_solution = tabu_search(max_iterations, tabu_size, airplanes[:num_airplanes], output_file="output.txt")

                            
                            end_time = time.time()

                            
                            elapsed_time = end_time - start_time

                            
                            
                            print("BEST SOLUTION:")
                            print_airplanes_and_strips(best_solution)
                            print("Time taken for tabu_search function:", elapsed_time, "seconds")
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
        if string_resposta == "2":
            while True:
                print("==================== MENU ====================")
                print("How many airplanes do you wish to simulate? (1-120)")
                print("[PRESS e] - Go Back")
                print("==============================================")
                num_airplanes_input = input()
                if num_airplanes_input == "e":
                    break

                
                else:
                    try:
                        num_airplanes = int(num_airplanes_input)
                        if num_airplanes < 1 or num_airplanes > 120:
                            print("==============================================")
                            print("Please enter a number between 1 and 120.")
                            print("==============================================")
                        else:
                            # airplanes = generate_airplanes
                            print("==============================================")
                            print("Choose a starting temperature: ")
                            print("==============================================")
                            starting_temperature = float(input())
                            print("==============================================")
                            print(" ")
                            print("==============================================")
                            print("==============================================")
                            print("Choose a cooling rate:")
                            print("==============================================")
                            cooling_rate = float(input())
                            print("==============================================")
                            print(" ")
                            print("==============================================")
                            print("==============================================")
                            print("Choose a stopping temperature: ")
                            print("==============================================")
                            stopping_temperature = float(input())
                            print("==============================================")
                            print(" ")
                            print("==============================================")
                            print("==============================================")
                            print("How many iterations do you want to perform?")
                            print("==============================================")
                            max_iterations = int(input())
                            print("==============================================")
                            print(" ")
                            print("==============================================")
                            # tabu_size = int(input())
                            # Perform tabu search
                            # best_solution = tabu_search(max_iterations=max_iterations, tabu_size=tabu_size, airplanes=airplanes)
                            best_solution, best_cost = simulated_annealing(airplanes[:num_airplanes])
                            print("BEST SOLUTION:")
                            print_airplanes_and_strips(best_solution)
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
        if string_resposta == "3":
             while True:
                print("==================== MENU ====================")
                print("How many airplanes do you wish to simulate? (1-120)")
                print("[PRESS e] - Go Back")
                print("==============================================")
                num_airplanes_input = input()
                if num_airplanes_input == "e":
                    break
                else:
                    try:
                        num_airplanes = int(num_airplanes_input)
                        if num_airplanes < 1 or num_airplanes > 120:
                            print("==============================================")
                            print("Please enter a number between 1 and 120.")
                            print("==============================================")
                        else:
                            
                            population_size = -1
                            while True:
                                print("==============================================")
                                print("How many chromosomes do you want in the population? (100-1000)")
                                print("==============================================")
                                
                                population_size = int(input())

                                if 100 <= population_size <= 1000:
                                    break
                                else:
                                    print("Invalid input. Please enter a number between 100 and 1000 (inclusive).")
                            
                            max_iterations = -1
                            while True:
                                print("==============================================")
                                print("How many iterations do you want to perform? (1-10000)")
                                print("==============================================")
                                
                                max_iterations = int(input())

                                if 1 <= max_iterations <= 10000:
                                    break
                                else:
                                    print("Invalid input. Please enter a number between 1 and 10000 (inclusive).")
                            
                            start_time = time.time()
                            best_solution, _ = geneticAI(airplanes[:num_airplanes],population_size,max_iterations,"roulette",0.05)
                            end_time = time.time()
                            elapsed_time = end_time - start_time
                            
                            print("BEST SOLUTION:")
                            print_airplanes_and_strips(best_solution)
                            print("Time taken for genetic function:", elapsed_time, "seconds")
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

        if string_resposta == "4":
            while True:
                print("==================== MENU ====================")
                print("How many airplanes do you wish to simulate? (1-120)")
                print("[PRESS e] - Go Back")
                print("==============================================")
                num_airplanes_input = input()
                if num_airplanes_input == "e":
                    break

                
                else:
                    try:
                        num_airplanes = int(num_airplanes_input)
                        if num_airplanes < 1 or num_airplanes > 120:
                            print("==============================================")
                            print("Please enter a number between 1 and 120.")
                            print("==============================================")
                        else:
                            
                            # tabu_size = int(input())
                            # Perform tabu search
                            # best_solution = tabu_search(max_iterations=max_iterations, tabu_size=tabu_size, airplanes=airplanes)
                            start_time = time.time()
                            best_solution, best_cost = hill_climbing(airplanes[:num_airplanes], "output.txt")
                            end_time = time.time()

                            
                            elapsed_time = end_time - start_time
                            print("BEST SOLUTION:")
                            print_airplanes_and_strips(best_solution)
                            print("Time taken for hill_climbing_search function:", elapsed_time, "seconds")
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")



if __name__ == "__main__":
    main()
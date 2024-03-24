from airplane import *
from landing_strip import *
from tabu_search import *
from simulated_annealing import *
from hill import *



def main():
    

    airplane1 = Airplane(1000, 15, 0)
    airplane2 = Airplane(2000, 25, 20)
    airplane3 = Airplane(1500, 20, 50)
    airplane4 = Airplane(1800, 18, 70)
    airplane5 = Airplane(2500, 22, 40)
    airplane6 = Airplane(1200, 12, 80)
    airplane7 = Airplane(2800, 30, 20)
    airplane8 = Airplane(2000, 28, 60)
    airplane9 = Airplane(1600, 16, 10)
    airplane10 = Airplane(2200, 24, 85)
    airplane11 = Airplane(2700, 21, 30)
    airplane12 = Airplane(1900, 17, 75)
    airplane13 = Airplane(2300, 26, 45)
    airplane14 = Airplane(1400, 14, 55)
    airplane15 = Airplane(3000, 29, 5)
    airplane16 = Airplane(1750, 19, 65)
    airplane17 = Airplane(2100, 23, 20)
    airplane18 = Airplane(2600, 27, 25)
    airplane19 = Airplane(1700, 13, 35)
    airplane20 = Airplane(2400, 20, 15)
    airplane21 = Airplane(2600, 22, 80)
    airplane22 = Airplane(1500, 16, 65)
    airplane23 = Airplane(2200, 28, 30)
    airplane24 = Airplane(2800, 25, 45)
    airplane25 = Airplane(1900, 12, 90)
    airplane26 = Airplane(1400, 19, 50)
    airplane27 = Airplane(3000, 24, 75)
    airplane28 = Airplane(2000, 17, 25)
    airplane29 = Airplane(2500, 30, 60)
    airplane30 = Airplane(1800, 14, 40)
    airplane31 = Airplane(2700, 23, 10)
    airplane32 = Airplane(1700, 27, 20)
    airplane33 = Airplane(2300, 15, 20)
    airplane34 = Airplane(1600, 21, 55)
    airplane35 = Airplane(2900, 18, 95)
    airplane36 = Airplane(2100, 26, 35)
    airplane37 = Airplane(2400, 13, 5)
    airplane38 = Airplane(2300, 29, 70)
    airplane39 = Airplane(2500, 22, 15)
    airplane40 = Airplane(1900, 16, 50)
    airplane41 = Airplane(1800, 20, 85)
    airplane42 = Airplane(2700, 24, 30)
    airplane43 = Airplane(1400, 28, 20)
    airplane44 = Airplane(3000, 17, 25)
    airplane45 = Airplane(2200, 19, 90)
    airplane46 = Airplane(1600, 27, 55)
    airplane47 = Airplane(2100, 15, 20)
    airplane48 = Airplane(2900, 25, 75)
    airplane49 = Airplane(1700, 23, 5)
    airplane50 = Airplane(2300, 30, 40)
    airplane51 = Airplane(2000, 14, 70)
    airplane52 = Airplane(2500, 18, 35)
    airplane53 = Airplane(1900, 26, 20)
    airplane54 = Airplane(2700, 16, 15)
    airplane55 = Airplane(1400, 22, 50)
    airplane56 = Airplane(2800, 19, 95)
    airplane57 = Airplane(2200, 27, 25)
    airplane58 = Airplane(1600, 23, 60)
    airplane59 = Airplane(3000, 15, 10)
    airplane60 = Airplane(1800, 21, 45)

   


    # Store airplanes in a list
    airplanes = [airplane1, airplane2, airplane9, airplane10
                 , airplane5, airplane6, airplane7, airplane8, airplane3, airplane4,
                airplane11, airplane12, airplane13, airplane14, airplane15, airplane16, airplane17, airplane18, airplane19, airplane20,
                airplane21, airplane22, airplane23, airplane24, airplane25, airplane26, airplane27, airplane28, airplane29, airplane30,
                airplane31, airplane32, airplane33, airplane34, airplane35, airplane36, airplane37, airplane38, airplane39, airplane40,
                airplane41, airplane42, airplane43, airplane44, airplane45, airplane46, airplane47, airplane48, airplane49, airplane50,
                 airplane51, airplane52, airplane53, airplane54, airplane55, airplane56, airplane57, airplane58, airplane59, airplane60]
    
    def print_airplanes_and_strips(best_solution):
        landing_strips, sum_difference, unsafe_waiting, n = generateResults(best_solution)
        print("Sum of differences between actual and expected landing times:", sum_difference)
        for i, landing_strip in enumerate(landing_strips):
            print(f"Landing Strip {i}:")
            for airplane in landing_strip.current_airplanes:
                print(airplane)
                if (airplane.is_gonna_crash()):
                    print("CRAAAAAAAAAAAAAAAASH")
        print("Crashes:", n)
        print("Unsafe waiting:", unsafe_waiting)
        
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
                print("How many airplanes do you wish to simulate? (1-60)")
                print("[PRESS e] - Go Back")
                print("==============================================")
                num_airplanes_input = input()
                if num_airplanes_input == "e":
                    break
        
                else:
                    try:
                        num_airplanes = int(num_airplanes_input)
                        if num_airplanes < 1 or num_airplanes > 60:
                            print("==============================================")
                            print("Please enter a number between 1 and 60.")
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
                            # Perform tabu search
                            best_solution = tabu_search(max_iterations=max_iterations, tabu_size=tabu_size, airplanes=airplanes)
                            print("BEST SOLUTION:")
                            print_airplanes_and_strips(best_solution)
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
        if string_resposta == "2":
            while True:
                print("==================== MENU ====================")
                print("How many airplanes do you wish to simulate? (1-60)")
                print("[PRESS e] - Go Back")
                print("==============================================")
                num_airplanes_input = input()
                if num_airplanes_input == "e":
                    break

                
                else:
                    try:
                        num_airplanes = int(num_airplanes_input)
                        if num_airplanes < 1 or num_airplanes > 60:
                            print("==============================================")
                            print("Please enter a number between 1 and 60.")
                            print("==============================================")
                        else:
                            # airplanes = generate_airplanes
                            '''print("==============================================")
                            print("How many iterations do you want to perform?")
                            print("==============================================")
                            max_iterations = int(input())
                            print("==============================================")
                            print(" ")
                            print("==============================================")'''
                            # tabu_size = int(input())
                            # Perform tabu search
                            # best_solution = tabu_search(max_iterations=max_iterations, tabu_size=tabu_size, airplanes=airplanes)
                            best_solution, best_cost = simulated_annealing(num_airplanes)
                            print("BEST SOLUTION:")
                            # print_airplanes_and_strips(best_solution)
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
        if string_resposta == "4":
            while True:
                print("==================== MENU ====================")
                print("How many airplanes do you wish to simulate? (1-60)")
                print("[PRESS e] - Go Back")
                print("==============================================")
                num_airplanes_input = input()
                if num_airplanes_input == "e":
                    break

                
                else:
                    try:
                        num_airplanes = int(num_airplanes_input)
                        if num_airplanes < 1 or num_airplanes > 60:
                            print("==============================================")
                            print("Please enter a number between 1 and 60.")
                            print("==============================================")
                        else:
                            # airplanes = generate_airplanes
                            '''print("==============================================")
                            print("How many iterations do you want to perform?")
                            print("==============================================")
                            max_iterations = int(input())
                            print("==============================================")
                            print(" ")
                            print("==============================================")'''
                            # tabu_size = int(input())
                            # Perform tabu search
                            # best_solution = tabu_search(max_iterations=max_iterations, tabu_size=tabu_size, airplanes=airplanes)
                            best_solution, best_cost = hill_climbing(airplanes)
                            print("BEST SOLUTION:")
                            print_airplanes_and_strips(best_solution)
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")



if __name__ == "__main__":
    main()
import random
import pandas as pd
import math
import copy
import random
'''
class Airplane:
    def __init__(self, fuel_level, fuel_consumption_rate, expected_landing_time):
        self.arriving_fuel_level = fuel_level
        self.fuel_consumption_rate = fuel_consumption_rate
        self.expected_landing_time = expected_landing_time
        self.actual_landing_time = 0 
        self.safe = self.ensure_enough_fuel()

    def get_arriving_fuel_level(self):
        return self.arriving_fuel_level

    def get_fuel_consumption_rate(self):
        return self.fuel_consumption_rate

    def get_expected_landing_time(self):
        return self.expected_landing_time

    def get_actual_landing_time(self):
        return self.actual_landing_time

    def get_safe(self):
        return self.safe

    def __str__(self):
        return f"Fuel level: {self.arriving_fuel_level}, Fuel consumption rate: {self.fuel_consumption_rate}, Expected landing time: {self.expected_landing_time}, Actual landing time: {self.actual_landing_time}, Safe Landing: {self.safe}"

    def is_gonna_crash_init(self):
        
        actual_fuel_needed = self.fuel_consumption_rate * self.expected_landing_time
        
        return self.arriving_fuel_level < actual_fuel_needed    

    def is_gonna_crash(self):
        
        actual_fuel_needed = self.fuel_consumption_rate * self.actual_landing_time
        
        return self.arriving_fuel_level < actual_fuel_needed
    
    def ensure_enough_fuel(self):
        fuel_needed = self.fuel_consumption_rate * 60
        fuel_left = (self.arriving_fuel_level - self.fuel_consumption_rate*self.expected_landing_time)
        return fuel_left >= fuel_needed

class LandingStrip:
    def __init__(self):
        self.current_airplanes = []  # List of airplanes currently on the landing strip
        self.empty_time = 0  # Time when the landing strip will be empty

    def add_airplane(self, airplane):
        self.current_airplanes.append(airplane)

    def remove_airplane(self, airplane):
        self.current_airplanes.remove(airplane)

    def set_empty_time(self, time):
        self.empty_time = time

    def get_empty_time(self):
        return self.empty_time

    def is_empty(self):
        return len(self.current_airplanes) == 0

    def get_current_airplanes(self):
        return self.current_airplanes
    
    def count_unsafe_airplanes(self):
        return sum(1 for airplane in self.current_airplanes if not airplane.safe)
    
    def generateResults(airplanes):
        landing_strips = [LandingStrip() for _ in range(3)]
        landed_airplanes = set()

        for airplane in airplanes:
            for landing_strip in landing_strips:
                if airplane not in landed_airplanes:
                    landing_strip.land_airplane(airplane, landing_strips)
                    landed_airplanes.add(airplane)
                    break
        sum_difference = 0
        unsafe_plains = 0
        num_of_crashes= 0
        
        for airplane in airplanes:
            
            sum_difference += airplane.actual_landing_time - airplane.expected_landing_time
            if (airplane.actual_landing_time - airplane.expected_landing_time != 0 and not airplane.safe):
                unsafe_plains += 1

            if (airplane.is_gonna_crash()):
                 
                 num_of_crashes += 1
                
       
        return landing_strips, sum_difference, unsafe_plains, num_of_crashes


    def land_airplane(self, airplane, landing_strips):
        
        if airplane.expected_landing_time >= self.empty_time:
            # If the expected landing time is after the current empty time, no waiting is needed
            max_empty_time = max(landing_strip.get_empty_time() for landing_strip in landing_strips)
            actual_landing_time = max(max_empty_time,airplane.expected_landing_time)
            self.empty_time = actual_landing_time + 3
            airplane.actual_landing_time = actual_landing_time
            self.add_airplane(airplane)
        else:
            # If the expected landing time is before the current empty time, adjust accordingly
            max_empty_time = max(landing_strip.get_empty_time() for landing_strip in landing_strips)
            min_empty_time_strip = min(range(len(landing_strips)), key=lambda i: landing_strips[i].get_empty_time())
            min_empty_time = landing_strips[min_empty_time_strip].get_empty_time()
            actual_landing_time = max(max_empty_time - 3, max(airplane.expected_landing_time, min_empty_time))
            landing_strips[min_empty_time_strip].set_empty_time(actual_landing_time + 3)
            airplane.actual_landing_time = actual_landing_time
            landing_strips[min_empty_time_strip].add_airplane(airplane)



def cost_function(solution):
    cost = 0
    for landing_strip in solution:
        for airplane in landing_strip.get_current_airplanes():  # Acesse a lista de aviões dentro de cada landing strip
            delay = airplane.get_actual_landing_time() - airplane.get_expected_landing_time()
            if delay > 0 and airplane.get_priority() == 1:
                cost += delay
            elif airplane.get_priority() > 1:
                cost += airplane.get_priority()
            elif delay > 0 and airplane.get_priority() > 1:
                cost += delay + airplane.get_priority()
            else:
                cost += airplane.get_priority()
    return cost


def neighbor(solucao):
    nova_solucao = copy.deepcopy(solucao)  

    for i in range(len(nova_solucao)):
        avioes_pista_atual = nova_solucao[i].get_current_airplanes()  
        for aviao in avioes_pista_atual:
            nova_pista_index = random.choice([idx for idx in range(len(nova_solucao)) if idx != i])
            avioes_pista_destino = nova_solucao[nova_pista_index].get_current_airplanes()  
            conflito_horario = False
            for aviao_destino in avioes_pista_destino:
                if abs(aviao.get_actual_landing_time() - aviao_destino.get_actual_landing_time()) <= 2:
                    conflito_horario = True
                    break
            if not conflito_horario:
                print("aaaa")
                nova_solucao[nova_pista_index].add_airplane(aviao) 
                nova_solucao[i].remove_airplane(aviao)  

    return nova_solucao



def generate_initial_solution(airplanes):
    airplanes.sort(key=lambda x: x.expected_landing_time)
    # Sort airplanes based on a combination of expected landing time and fuel level
    # initial_solution = sorted(airplanes, key=lambda x: (x.expected_landing_time, -x.arriving_fuel_level))
    return airplanes


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
    
def simulated_annealing(airplanes, initial_temperature=1000, cooling_rate=0.9, stopping_temperature=0.01, max_iterations=300):
    current_solution = generate_initial_solution(airplanes)
    current_cost = float('inf')
    best_solution = current_solution
    best_cost = current_cost
    temperature = initial_temperature
    iteration = 0
    unsafe_plains = 100000  
    unsafe_planes_sol = 100000  
    num_of_crashes = 100000
    num_of_crashes_sol = 100000

    with open("output.txt", "w") as file:
        while temperature > stopping_temperature and iteration < max_iterations:

            neighbors = generate_neighbors(current_solution)
            for neighbor in neighbors:
                landing_strips, neighbor_value, unsafe_plains, num_of_crashes = LandingStrip.generateResults(neighbor)
                current_solution = neighbor
                current_cost = neighbor_value
                delta_cost = neighbor_value - current_cost
                if ((current_cost < best_cost) and (unsafe_plains <= unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or ((unsafe_plains < unsafe_planes_sol) and (num_of_crashes <= num_of_crashes_sol)) or (num_of_crashes < num_of_crashes_sol) or math.exp(-delta_cost / temperature) > random.random(): 
                    best_solution = neighbor
                    best_cost = current_cost
                    unsafe_planes_sol = unsafe_plains
                    num_of_crashes_sol = num_of_crashes
                    file.write(f"New Best Solution:\n" + print_improved_solution(landing_strips) + "\n")
                    file.write(f"New Best Solution Value: {neighbor_value}\n")
                    file.write(f"Unsafe Planes: {unsafe_planes_sol}\n")
                    file.write(f"Number of Crashes: {num_of_crashes_sol}\n")
                    file.write('\n')
                    
                
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

# Uso do algoritmo
def main():
    airplanes = []
    '''
    for i in range(1, 61):
        fuel_level = random.randint(1000, 5000)  # Random fuel level between 1000 and 2000
        fuel_consumption_rate = random.randint(15, 25)  # Random fuel consumption rate between 15 and 25
        expected_landing_time = random.randint(0, 90)  # Random expected landing time between 0 and 90
        airplane = Airplane(fuel_level, fuel_consumption_rate, expected_landing_time)
        airplanes.append(airplane)   
        '''
         
    airplane1 = Airplane(1000, 1, 0)
    airplane2 = Airplane(2000, 2, 20)
    airplane3 = Airplane(1500, 2, 50)
    airplane4 = Airplane(1800, 1, 70)
    airplane5 = Airplane(2500, 2, 40)
    airplane6 = Airplane(1200, 1, 80)
    airplane7 = Airplane(2800, 3, 20)
    airplane8 = Airplane(2000, 2, 60)
    airplane9 = Airplane(1600, 6, 10)
    airplane10 = Airplane(2200, 2, 85)
    airplane11 = Airplane(2700, 2, 30)
    airplane12 = Airplane(1900, 1, 75)
    airplane13 = Airplane(2300, 2, 45)
    airplane14 = Airplane(1400, 1, 55)
    airplane15 = Airplane(3000, 2, 5)
    airplane16 = Airplane(1750, 1, 65)
    airplane17 = Airplane(2100, 2, 20)
    airplane18 = Airplane(2600, 2, 25)
    airplane19 = Airplane(1700, 3, 35)
    airplane20 = Airplane(2400, 2, 15)
    airplane21 = Airplane(2600, 2, 80)
    airplane22 = Airplane(1500, 6, 65)
    airplane23 = Airplane(2200, 2, 30)
    airplane24 = Airplane(2800, 2, 45)
    airplane25 = Airplane(1900, 1, 90)
    airplane26 = Airplane(1400, 1, 50)
    airplane27 = Airplane(3000, 2, 75)
    airplane28 = Airplane(2000, 1, 25)
    airplane29 = Airplane(2500, 3, 60)
    airplane30 = Airplane(1800, 1, 40)
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
    
    airplanes = [airplane1, airplane2, airplane3, airplane4
                 , airplane5, airplane6, airplane7, airplane8, airplane9, airplane10,
                airplane11, airplane12, airplane13, airplane14, airplane15, airplane16, airplane17, airplane18, airplane19, airplane20,
                airplane21, airplane22, airplane23, airplane24, airplane25, airplane26, airplane27, airplane28, airplane29, airplane30]




    best_solution, best_cost = simulated_annealing(airplanes)
    print("BEST SOLUTION:")
    #print("Best Cost: ", best_cost)
    #with open("output.txt", "w") as file:
    #print_airplanes_and_strips(best_solution, file)


def print_airplanes_and_strips(best_solution, file=None):
    landing_strips, best_value, unsafe_plains, n = LandingStrip.generateResults(best_solution)
    print("Sum of differences between actual and expected landing times:", best_value, file=file)
    for i, landing_strip in enumerate(landing_strips):
        print(f"Landing Strip {i}:", file=file)
        for airplane in landing_strip.current_airplanes:
            print(airplane, file=file)
            if (airplane.is_gonna_crash()):
                print("CRAAAAAAAAAAAAAAAASH", file=file)
    print("Best Value", best_value, file=file)
    print("Crashes:", n, file=file)
    print("Unsafe waiting:", unsafe_plains, file=file)

if __name__ == "__main__":
    main()

'''
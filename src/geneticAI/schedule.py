import random
from airplane import Airplane


class Schedule:

    def __init__(self, airplane):
        self.airplane = airplane
        self.runway = int(random.uniform(1, 3))
        self.arrival_time = int(random.uniform(0, 120))

    def mutate_airplane(self, schedule):
        self.airplane.mutate_airplane(schedule.airplane)

    def mutate_runway(self, schedule):
        self.runway = schedule.runway

    def mutate_arrival_time(self, schedule):
        self.arrival_time = schedule.arrival_time

    def print_schedule(self):
        print("\n" + "=" * 30)
        print("Schedule Details Menu (Chromosome)")
        print("=" * 30 + "\n")
        print(" " * 15 + "Genes\n")
        print("1. Runway: {} ".format(self.runway))
        self.airplane.print_airplane()
        print("3. Real Landing Time: {} minutes".format(self.arrival_time))
        print("\n" + "=" * 30)


def generate_chromosome():
    airplane_gene = Airplane()
    schedule = Schedule(airplane_gene)
    return schedule

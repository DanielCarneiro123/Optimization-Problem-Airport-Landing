import random
from gene import *


class Airport:

    def __init__(self):
        self.runway = [0, 0, 0]

    def mutate_runway1(self, airplane):
        self.runway[0] = airplane

    def mutate_runway2(self, airplane):
        self.runway[1] = airplane

    def mutate_runway3(self, airplane):
        self.runway[2] = airplane

    def get_runway_state(self):
        return self.runway

    def print_schedule(self):
        print("\n" + "=" * 30)
        print("Airport State")
        for i, status in enumerate(self.runway):
            if status != 0:
                print(f"Runway {i + 1}: Occupied")
            else:
                print(f"Runway {i + 1}: Not Occupied")
        print("\n" + "=" * 30)


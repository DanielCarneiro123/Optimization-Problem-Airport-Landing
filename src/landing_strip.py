class LandingStrip:
    def __init__(self):
        # Initialize landing strip attributes
        self.current_airplanes = []  # List of airplanes currently on the landing strip
        self.empty_time = 0  # Time when the landing strip will be empty

    def add_airplane(self, airplane):
        # Add an airplane to the landing strip
        self.current_airplanes.append(airplane)

    def set_empty_time(self, time):
        # Set the time when the landing strip will be empty
        self.empty_time = time

    def get_empty_time(self):
        # Get the time when the landing strip will be empty
        return self.empty_time


    def land_airplane(self, airplane, landing_strips):
        # Land an airplane on the landing strip

        if airplane.expected_landing_time >= self.empty_time:
            # If the expected landing time is after the current empty time, check which LS has biggest empty_time and calculate act_landing_time, update LS and airplane
            max_empty_time = max(landing_strip.get_empty_time() for landing_strip in landing_strips)
            actual_landing_time = max(max_empty_time, airplane.expected_landing_time)
            self.empty_time = actual_landing_time + 3
            airplane.actual_landing_time = actual_landing_time
            self.add_airplane(airplane)
        else:
            # If the expected landing time is before the current empty time, adjust accordingly finding where is it possible to land faster
            max_empty_time = max(landing_strip.get_empty_time() for landing_strip in landing_strips)
            min_empty_time_strip = min(range(len(landing_strips)), key=lambda i: landing_strips[i].get_empty_time())
            min_empty_time = landing_strips[min_empty_time_strip].get_empty_time()
            actual_landing_time = max(max_empty_time - 3, max(airplane.expected_landing_time, min_empty_time))
            landing_strips[min_empty_time_strip].set_empty_time(actual_landing_time + 3)
            airplane.actual_landing_time = actual_landing_time
            landing_strips[min_empty_time_strip].add_airplane(airplane)

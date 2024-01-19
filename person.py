import threading
import time
import random

class Person(threading.Thread):
    def __init__(self, name, garden):
        super().__init__()
        self.name = name
        self.garden = garden

    def run(self):
        while True:
            time_to_spend = random.randint(1, 3)  # Random time spent in the garden
            self.garden.enter_garden(self.name)
            time.sleep(time_to_spend)  # Time in the garden
            self.garden.leave_garden(self.name)
            time.sleep(random.randint(2, 5))  # Time before next visit

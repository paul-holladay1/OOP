import random

class insect:

    def __init__(self,w,l):
        self.wings = w
        self.legs = l
        self.flight = 0


    def calculate_flight(self):
        self.flight = random.randint(1,10)

    def get_flight(self):
        return self.flight




class ParkingSpsot:

    def __init__(self, capacity:int):
        self.capacity = capacity
        self.current_count = 0
        print(f"Parking Spot Initialized With {self.capacity}")

    def insert_car(self):
        if self.current_count <= self.capacity:
            self.capacity = self.capacity - 1
            self.current_count = self.current_count + 1
        else:
            self.capacity = 0

    def remove_car(self):
        if self.current_count >=0:
            self.current_count = self.current_count - 1
            self.capacity = self.capacity + 1


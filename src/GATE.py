
import os


class Gate:
    def __init__(self):
        self.gate_status= 0. # 0 for closing 1 for opening
        print(f"Parking Gate With {self.gate_status} where 0 = Close and 1 = open")

    def open_gate(self) -> None:
        self.gate_status = 1.
        print("Gate Open !!!")

    def close_gate(self, is_car_out_of_boundary:bool) -> None:
        if is_car_out_of_boundary:
            self.gate_status = 0.
        print("Gate Closed !!!")





import os
from GATE import Gate
from FaceDetect import DetectFace
class Car:

    def __init__(self):
        self.driver_face = None
        self.num_plate = None
        self.face_img = DetectFace()

    def take_driver_face_photo(self, save_dir:str):
        if self.num_plate:
            dir_path = os.path.join(save_dir, str(self.num_plate))
            os.makedirs(dir_path)
            self.face_img.capture(output_path=dir_path)
            self.driver_face = os.path.join(dir_path, "face.jpg")

    def take_num_plate(self, num:str):
        self.num_plate = num

    def send_parking_request(self, g:Gate):
        if self.driver_face and self.num_plate:
            g.open_gate()
        else:
            print("No Driver Photo and Number Plate !!! ")

    def send_out_request(self, g:Gate):
        pass



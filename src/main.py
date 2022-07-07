import os
from GATE import Gate
from PARKINGSPOT import ParkingSpsot
from CAR import Car
from FaceDetect import DetectFace
from CompImg import CompImg
CAPACITY = 4

DATA_PATH = "./DATA/"
IMG_PATH = os.path.join(DATA_PATH, "IMAGES")

if __name__ == '__main__':

    p_spot = ParkingSpsot(capacity=CAPACITY)
    gate = Gate()
    c = None

    while True:

        inp = input("Do you want to Park or Exit? (Press [p] for Parking and [e] for Exit) :")


        if str(inp).lower() == 'e':
           c = Car()
           num_plate_inp = input("Enter Your Number Plate:")
           prev_img_path = os.path.join(IMG_PATH, str(num_plate_inp), 'face.jpg')
           allow = False
           image_difference = 0.
           if os.path.exists(prev_img_path):
               fd = DetectFace()
               fd.capture(output_path='.')
               new_img_path = './face.jpg'
               compare_image = CompImg(prev_img_path,new_img_path)
               image_difference = compare_image.compare_image()
               if image_difference < 0.1:
                   allow = True
           if allow:
               p_spot.remove_car()
               print(f"You are Ready for Exit ! Spot remaining {p_spot.capacity} !!")
           else:
               print(f"Driver face image did not match {image_difference}, please call the operator !!")

        elif str(inp).lower() == 'p':
            c = Car()
            num_plate_inp = input("Enter Your Number Plate:")
            c.take_num_plate(num=num_plate_inp)
            c.take_driver_face_photo(save_dir=IMG_PATH)
            p_spot.insert_car()
            if p_spot.capacity > 0:
                print(f"You are Ready for Parking ! Spot remaining {p_spot.capacity} !!")
                c.send_parking_request(g=gate)
            else:
                print(f"Sorry {p_spot.capacity} Spot remaining !!")

        else:
            print("wrong Inp")






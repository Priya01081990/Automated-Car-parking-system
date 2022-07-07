
import os
import cv2

class DetectFace:

    def __init__(self):
        self.xml_path = "/Users/priyankadey/PycharmProjects/SmartCarPark1.0/XML_DATA/haarcascade_frontalface_default.xml"
        self.faceCascade = cv2.CascadeClassifier(self.xml_path)
        self.op_img_name = 'face.jpg'

    def detect(self, img_path:str, output_path:str):
        img = cv2.imread(img_path)
        faces = self.faceCascade.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            faces = img[y:y + h, x:x + w]
            cv2.imwrite(os.path.join(output_path, self.op_img_name), faces)

    def capture(self, output_path:str):
        video_capture = cv2.VideoCapture(0)
        while True:
            # Capture frame-by-frame
            ret, frames = video_capture.read()
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
            faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frames, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Display the resulting frame
            cv2.imshow('Video', frames)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite('./temp.jpg', frames)
                self.detect('./temp.jpg', output_path)
                video_capture.release()
                cv2.destroyAllWindows()
                break
        #video_capture.release()
        #cv2.destroyAllWindows()

if __name__ == '__main__':
    f = DetectFace()
    f.capture(output_path='/Users/priyankadey/PycharmProjects/SmartCarPark1.0/src/')
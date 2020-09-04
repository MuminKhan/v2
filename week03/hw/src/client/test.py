import cv2
import numpy as np

from datetime import datetime
from time import sleep

if __name__ == "__main__":
    print("Begining video stream.")
    video_capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 8)

        for (x, y, w, h) in faces:
            cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cur_time = datetime.now().strftime("%m_%d_%Y-%H_%M_%S")
            out_file = f'{cur_time}.png'
            cv2.imwrite(out_file, gray)
            print(f'Face found! Written to {out_file}')
            sleep(2)

        """
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        """

    video_capture.release()
    cv2.destroyAllWindows()

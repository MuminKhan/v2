import cv2
import numpy as np
import paho.mqtt.publish as publish
import sys

from datetime import datetime
from time import sleep

MQTT_HOST="mqtt"
MQTT_PORT=1883
MQTT_TOPIC="facey"
MQTT_QOS=1

if __name__ == "__main__":
    print("Begining video stream.")
    video_capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 8)

        for (x, y, w, h) in faces:
            gray = gray[y:y+h, x:x+w]
            cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cur_time = datetime.now().strftime("%m_%d_%Y-%H_%M_%S")
            out_file = f'{cur_time}.png'
            cv2.imwrite(out_file, gray)
            print('AHHHHHHHHHHHHHHHHHHHHHHHHHHHH')
            print(f'Face found! Written to {out_file}')
            
            encoded_img = cv2.imencode('.png', gray)[1].tobytes()
            publish.single(MQTT_TOPIC, payload=encoded_img, hostname=MQTT_HOST, port=MQTT_PORT, qos=MQTT_QOS)
            print(f'Published {out_file} to {MQTT_HOST}:{MQTT_PORT} topic: {MQTT_TOPIC}')
            sleep(5)

        """
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        """

    video_capture.release()
    cv2.destroyAllWindows()

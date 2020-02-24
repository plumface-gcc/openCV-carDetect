import numpy as np
import cv2
import urllib.request
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('IP', help = "Ip address from ipwebcam app.")
args = parser.parse_args()

car_cascade = cv2.CascadeClassifier("car.xml")

url = "http://" + args.IP + "/shot.jpg"

cap = cv2.VideoCapture()

def phonecamera():
    while True:

        ret, img = cap.read()  # read frame by frame
        img_arr = np.array(bytearray(urllib.request.urlopen(url).read()), dtype=np.uint8) # create a byte array that opens and reads a url
        img = cv2.imdecode(img_arr, -1)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        car_multiScale = car_cascade.detectMultiScale(gray, 1.10, 5) # self, layers, K neighbors

        for (x, y, w, h) in car_multiScale:
            cv2.putText(img, "Car", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3) # draw text over bounding box

            cv2.rectangle(img, (x, y), (x + y, y + h), (255, 255, 0), 2) # draw box to screen

        cv2.imshow('IPWebcam Output', img) # output image

        key = cv2.waitKey(35) & 0xff
        if key == 27:
            break

def mainrun():
    try:
        phonecamera()
    except urllib.error.URLError as e:
        print("Bad url entered. Please run program again with new args.")


mainrun()

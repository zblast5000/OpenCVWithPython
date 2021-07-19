# Programa de teste opneCV

import cv2
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #img = cv2.imread('OpenCV_Logo.png', cv2.IMREAD_COLOR)
    #cv2.namedWindow('Hello World')
    #cv2.imshow('Hello World', img)
    #cv2.waitKey()
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    cap.set(10,100)
    while True:
        success, img = cap.read()
        cv2.imshow('Video',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



# See PyCharm help at https://www.jetbrains.com/help/pycharm/

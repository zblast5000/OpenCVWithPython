#Script para detectar particulas em imagens MEV
#Autor: Danilo Mendes Amorim
#Data:18/07/21

import cv2
import numpy as np
import matplotlib.pyplot
from matplotlib import pyplot as plt

#import imagens
#img = cv2.imread('Images/MEV.png', cv2.IMREAD_COLOR)
img = cv2.imread('Images/futebol.jpg', cv2.IMREAD_COLOR)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.blur(imgGray, (7, 7))


#Mostra Imagens
#cv2.imshow('Imgagem', img)
cv2.imshow('Gray', imgGray)
cv2.imshow('Blur', imgBlur)

# Apply Hough transform on the blurred image.
#detected_circles = cv2.HoughCircles(imgBlur,
#                                    cv2.HOUGH_GRADIENT, 1, 20, param1=20,
#                                    param2=35, minRadius=1, maxRadius=40)

detected_circles = cv2.HoughCircles(imgBlur,
                                    cv2.HOUGH_GRADIENT, 1, 50, param1=30,
                                    param2=40, minRadius=20, maxRadius=60)




# Draw circles that are detected.
if detected_circles is not None:

    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)

        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 2)
        cv2.imshow("Detected Circle", img)





while True:
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break



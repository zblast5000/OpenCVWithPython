
import cv2
import numpy as np
import matplotlib.pyplot
from matplotlib import pyplot as plt

def smooth(a):
    result = []
    i=0
    i1=0
    i2=0
    i3=0
    i4=0
    i5=0
    i6=0
    i7=0
    media=0.0
    soma =0
    for element in a:
        i1=i2
        i2=i3
        i3=i4
        i4=i5
        i5=i6
        i6=i7
        i7=int(element)
        soma = ((i1 + i2 + i3+ i4+ i5+ i6+ i7))
        media = (soma // 7)
        res = media
        result.append(res)
    rt = np.array(result, dtype=np.uint8)
    return rt


def sm2d(arr):
    i=0
    result = np.array(arr, dtype=np.uint8)
    linha = np.array([], dtype=np.uint8)
    for row in arr:
        linha = smooth(row)
        result[i, :] = linha
        i = i + 1
        #for elem in row:
        #    print(elem, end=' ')
    return result


kernel = np.ones((2, 2), np.uint8)

#img = cv2.imread('OpenCV_Logo.png', cv2.IMREAD_COLOR)
img = cv2.imread('Images/MEV.png', cv2.IMREAD_COLOR)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGray4 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgGray2 = (imgGray[:] * 1.4).astype(np.uint8)
imgGray3 = imgGray2[:] *0 +125

h_eq = cv2.equalizeHist(imgGray4)
h_eq = cv2.bilateralFilter(h_eq, 11, 77, 77)
np.multiply(h_eq,0.6).astype(np.uint8)
(T, imgBin) = cv2.threshold(h_eq, 105, 255, cv2.THRESH_BINARY)

#h_eq = (h_eq[:] * 0.7).astype(np.uint8)
#h_eq = cv2.equalizeHist(imgGray4)
#h_eq = cv2.bilateralFilter(h_eq, 11, 77, 77)

#h_eq = sm2d(h_eq)
imgBlur = cv2.GaussianBlur(h_eq, (3, 3), 0)

imgCanny = cv2.Canny(imgGray, 100, 150)
imgCanny2 = cv2.Canny(imgGray2, 100, 150)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
#imgGray2 = sm2d(imgGray2)
blur = cv2.blur(imgGray2, (5, 5))
#blur = imgGray
#cv2.namedWindow('Hello World')
#cv2.namedWindow('Blur')
cv2.imshow('Gray', imgGray)
cv2.imshow('Gray2', imgGray2)
# cv2.imshow('Blur', imgBlur)
cv2.imshow('Canny', imgCanny)
cv2.imshow('Canny2', imgCanny2)
#a = smooth(imgGray[300,:])
#imgGray[300, :] = a
#imgGray[301, :] = a
#imgGray[302, :] = a

cv2.imshow('Finale', imgGray)
# cv2.imshow('dilate', imgDialation)
# cv2.waitKey()
frame = np.asarray(imgGray)
#valores frame[]
print ("teste: \n")
print(frame.size)
print (frame[300,:])
valores = [105235, 107697, 110256, 109236, 108859, 109986]
valotes = frame[300,:]
#h_eq = imgBin
imgCirc = h_eq
img2 = cv2.cvtColor(imgCirc, cv2.COLOR_GRAY2RGB)
#img3 = cv2.cvtColor(imgBin, cv2.COLOR_)


# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(imgCirc,
                                    cv2.HOUGH_GRADIENT, 1, 20, param1=20,
                                    param2=35, minRadius=1, maxRadius=40)

# Draw circles that are detected.
if detected_circles is not None:

    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))

    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]

        # Draw the circumference of the circle.
        cv2.circle(img2, (a, b), r, (0, 255, 0), 1)

        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img2, (a, b), 1, (0, 0, 255), 2)
        cv2.imshow("Detected Circle", img2)


circulos = detected_circles[0,:][:,[2]]
#circulos = circulos.T
matplotlib.pyplot.hist(circulos)
#matplotlib.pyplot.plot(imgGray[300,:])
#matplotlib.pyplot.plot(imgGray2[300,:])

#matplotlib.pyplot.plot(a)
#img5 = imgBlur + imgGray2
img5 = cv2.bitwise_and(imgGray2,imgGray2,mask = imgBin)
img5 = cv2.Canny(imgBin, 100, 150)
cv2.imshow("imgBlur", img5)
matplotlib.pyplot.show()

#Função calcHist para calcular o hisograma da imagem
h = cv2.calcHist([h_eq], [0], None, [256], [0, 256])
plt.plot(h)
plt.xlim([0, 256])
plt.show()


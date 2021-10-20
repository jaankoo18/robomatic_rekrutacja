import cv2
import numpy as np

img = cv2.imread("circles.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#finding the biggest area
if len(contours) >= 1:
    biggest_area = cv2.contourArea(contours[0])
    contour_to_draw = contours[0]
    for contour in contours:
        area = cv2.contourArea(contour)
        print(area)
        if area > biggest_area:
            biggest_area = area
            contour_to_draw = contour
else:
    print("nie ma niebieskiego obiektu")

cv2.drawContours(img, contour_to_draw, -1, (0, 0, 0), 3)
#cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow("lel", img)
cv2.imshow("lell", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()



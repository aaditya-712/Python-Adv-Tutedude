import cv2

img = cv2.imread("D:/My Programming Studies/Tutedude/18_open_cv/CONTENT FILES/highway.jpg", 0)

cv2.imshow("Car Image", img)

cv2.imwrite("car.jpg", img)

cv2.waitKey(0)

cv2.destroyAllWindows()
import cv2

img = cv2.imread("D:/My Programming Studies/Tutedude/18_open_cv/CONTENT FILES/highway.jpg")

print("Dimensions of the image are: ",img.shape)

width = 400
height = img.shape[0]
dim = (width, height)
resized = cv2.resize(img, dim)

cv2.imshow("window", resized)

cv2.waitKey(0)

cv2.destroyAllWindows()
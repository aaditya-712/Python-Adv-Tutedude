import cv2

img = cv2.imread("D:/My Programming Studies/Tutedude/18_open_cv/CONTENT FILES/highway.jpg", 1)
# to show the image in black & white pass above an argument 0
# 0 for black white
# 1 for original or rgb format (can use -1 also)

cv2.imshow("window", img)

cv2.waitKey(1000)
# wait key is in milliseconds
# 0 is to wait until manually closed
# for 1 sec use 1000 milliseconds

cv2.destroyAllWindows()
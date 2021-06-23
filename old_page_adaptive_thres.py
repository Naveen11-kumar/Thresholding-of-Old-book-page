import cv2
img=cv2.imread("old_page.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayshow=cv2.imshow("GrayImage", gray)
cv2.waitKey(0)
gaussian_blur=cv2.GaussianBlur(gray,(5,5),10)
cv2.imshow("GAUSSIAN BLUR",gaussian_blur)
cv2.waitKey(0)
adaptive_thres=cv2.adaptiveThreshold(gaussian_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 7, 5)
cv2.imshow("ADAPTIVE THRESHOLD",adaptive_thres)
cv2.waitKey(0)
cv2.imwrite("adaptive.jpg",adaptive_thres)
"""
with the arguments:
    gray: Input image (grayscale).
    circles: A vector that stores sets of 3 values: xc,yc,r for each detected circle.
    HOUGH_GRADIENT: Define the detection method. Currently this is the only one available in OpenCV.
    dp = 1: The inverse ratio of resolution.
    min_dist = gray.rows/16: Minimum distance between detected centers.
    param_1 = 200: Upper threshold for the internal Canny edge detector. (higher means more accurate usually)
    param_2 = 100*: Threshold for center detection.
    min_radius = 0: Minimum radius to be detected. If unknown, put zero as default.
    max_radius = 0: Maximum radius to be detected. If unknown, put zero as default.
"""
import cv2 as cv
import numpy as np
from PIL import Image, ImageDraw




capture = cv.VideoCapture(0)

while True:
    ret, src = capture.read()
    height = src.shape[1]
    width = src.shape[0]
#
    lum_img = Image.new('RGB', (height, width) , (0,0,0))

    draw = ImageDraw.Draw(lum_img)


    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    gray = cv.medianBlur(gray, 5)
    #gray=cv.Canny(gray,20,50)
    #cv.imshow("gray",gray)
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                              param1=200, param2=50,
                              minRadius=1, maxRadius=60)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(src, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]

            draw.pieslice(((i[0]-radius, i[1]-radius), (i[0]+radius, i[1]+radius)), 0, 360, fill=(255, 255, 255), outline="white")
            lum_img_arr = np.array(lum_img)
            cv.imshow("lum_img", lum_img_arr)
            final_img_arr = cv.bitwise_and(src, lum_img_arr)
            cv.imshow("final", final_img_arr)

            cv.circle(src, center, radius, (255, 0, 255), 3)

    cv.imshow("detected circles", src)
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break
cv.destroyAllWindows()
exit(1)

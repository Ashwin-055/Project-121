# import cv2 to capture videofeed
import cv2
import time
import numpy as np

# attach camera indexed as 0
camera = cv2.VideoCapture(0)
time.sleep(2)

# setting framewidth and frameheight as 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# loading the mountain image
bld = cv2.imread('googleplex.jpg')

# resizing the mountain image as 640 X 480
bld = cv2.resize(bld , (640 , 480))

while True:

    # read a frame from the attached camera
    status , frame = camera.read()

    # if we got the frame successfully
    if status:

        # flip it
        frame = cv2.flip(frame , 1)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # creating thresholds
        lower_bound = np.array([158, 157, 156])
        upper_bound = np.array([255, 255, 255])

        # thresholding image
        mask = cv2.inRange(frame_rgb, lower_bound, upper_bound)
        # inverting the mask
        mask = cv2.bitwise_not(mask)
        # bitwise and operation to extract foreground / person
        human = cv2.bitwise_and(frame, frame , mask = mask)
        # final image
        final_image = np.where(human == 0 , bld , human)

        # show it
        cv2.imshow('‎' , final_image)

        # wait of 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()
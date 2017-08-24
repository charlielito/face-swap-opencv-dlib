#! /usr/bin/env python

import argparse
import sys
import numpy as np
import cv2
from imutils import face_utils
import datetime
import imutils
import time
import dlib
from utils import face_swap, face_swap2, face_swap3

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser(description='Process some image swap the 2 first faces (if there are 2 or more)')
ap.add_argument("-f", "--filename", required=False, default="imgs/pitts.jpg", help="path to image")
ap.add_argument("-f2", "--filename2", required=False, help="path to image")
ap.add_argument('--webcam', action='store_true')

args = vars(ap.parse_args())
print(args)

# Make sure OpenCV is version 3.0 or above
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

if int(major_ver) < 3 :
    print >>sys.stderr, 'ERROR: Script needs OpenCV 3.0 or higher'
    sys.exit(1)

print("[INFO] loading facial landmark predictor...")
model = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(model)

webcam = args['webcam']

if webcam:

    video_capture = cv2.VideoCapture(0)

    while (True):

        ret, img2 = video_capture.read()
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        # detect faces in the grayscale frame
        rects2 = detector(gray2, 0)
        if (len(rects2) != 0 ):
            break

    video_capture.release()


# Read images will swap image1 into image2
filename1 = args['filename']
filename2 = args['filename2']

img1 = cv2.imread(filename1)

if not webcam:
    if filename2 is None:
        output = face_swap3(img1, detector, predictor)
        assert output is not None, "There are not 2 faces or more in the image!"
        cv2.imshow("Face Swapped", output)
        cv2.imwrite(filename1[:-4]+"_swapped.jpg",output)

    else:
        img2 = cv2.imread(filename2)
        output1, output2 = face_swap2(img2,img1, detector, predictor)
        assert output1 is not None or output1 is not None, "There were not found faces in either the first or second image"
        cv2.imshow("Face Swapped", output1)
        cv2.imwrite(filename1[:-4]+"_swapped.jpg",output1)
        cv2.imshow("Face Swapped2", output2)
        cv2.imwrite(filename2[:-4]+"_swapped.jpg",output2)
else:
        output1, output2 = face_swap2(img2,img1, detector, predictor)
        assert output1 is not None or output1 is not None, "There were not found faces in either the first or second image"
        cv2.imshow("Face Swapped", output1)
        cv2.imshow("Face Swapped2", output2)
        cv2.imwrite(filename1[:-4]+"_swapped.jpg",output1)
        cv2.imwrite("imgs/webcam_swapped.jpg",output2)

cv2.waitKey(0)
cv2.destroyAllWindows()

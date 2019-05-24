import argparse
import cv2
import os
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-p", required = True, help = "Path to the directory containing the images")
args = vars(ap.parse_args())

index = 0
for filename in os.listdir(args["p"]):
    os.rename(args["p"] + filename, args["p"] + str(index) + '.jpg')
    image = cv2.imread(args["p"] + str(index) + '.jpg')

    brighter       = np.ones(image.shape, dtype = "uint8") * 100
    darker         = np.ones(image.shape, dtype = "uint8") * 100
    brighter_image = cv2.add(image, brighter)
    darker_image   = cv2.subtract(image, darker)

    cv2.imwrite(args["p"] + str(index) + '-brighter.jpg', brighter_image)
    cv2.imwrite(args["p"] + str(index) + '-darker.jpg', darker_image)
    cv2.imshow("image", image)
    cv2.imshow("brighter_image", brighter_image)
    cv2.imshow("darker_image", darker_image)
    cv2.waitKey(0)
    index = index + 1

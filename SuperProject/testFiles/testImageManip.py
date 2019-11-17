import numpy as np
import cv2 as cv

# load a test image (B+W bitmap)
img = cv.imread('1_patternSampling.bmp', cv.IMREAD_GRAYSCALE)
cv.imshow('image',img)

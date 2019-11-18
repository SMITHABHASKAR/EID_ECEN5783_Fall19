import numpy as np
import cv2 as cv

def appendRow(row, image):
    if (row.size != image.shape[1]):
        print ("row is not the correct width")
        return image
    image.append(row)
    return image

# load a test image (B+W bitmap)
img = cv.imread('1_patternSampling.bmp', cv.IMREAD_GRAYSCALE)
cv.imshow('image',img)

#cv imports img as a numpy.ndarray

row = img[0, :] # should grab the first row?
width = row.size

# shape[0] returns the vertical dimension (image height)
# shape[1] returns the width
widthImage = img.shape[1]
print (str(row))
print ("image width = ", width)
print ("image width 2 = ", widthImage)

# axis=0 - vertical axis, grabs a whole row

for i in range(0, 20):
    # add a row to the bottom
    img = np.append(img, [row], axis=0)
    # delete a row from the top
    # img = np.delete(img, 0, axis = 0)

cv.imshow('image',img) # can call imshow multiple times to update the display window
cv.imwrite('1_patternSampling_MOD.bmp', img)

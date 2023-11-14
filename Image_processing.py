# install opencv-python to read images into a variable
import cv2
import numpy as np

array = cv2.imread("red.jpg ")
# print(array)
print(array.shape)
''''
the image we uploaded is red theme which means in cv2 the structure of array would be
array = [[[B,G,R]
          [B,G,R]]]
so if we can interchange red and blue . the coolness of the image may be changed lets check
'''
rows, cols, colors = array.shape
for row in range(rows):
    for col in range(cols):
        array[row][col][2], array[row][col][0] = array[row][col][0], array[row][col][2]
        break

cv2.imwrite("blue.png", array)

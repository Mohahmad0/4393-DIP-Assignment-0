import math
import dip
import math
from dip import *
"""
Do not import cv2, numpy and other third party libs
"""


class Operation:

    def __init__(self):
        pass

    def merge(self, image_left, image_right, column):
        """
        Merge image_left and image_right at column (column)
        
        image_left: the input image 1
        image_right: the input image 2
        column: column at which the images should be merged

        returns the merged image at column
        """
        # new code
        # add your code here
        "dip.*functionHere* is how you import"

        "first index = row "
        "second index = column "
        "third index = color channel(RGB)"



        "copy left image array up to the defined column number then replacing the merged image upto the column number"

        left_half = image_left[0:183, 0:column].copy()
        right_half = image_right[0:183, column:275].copy()

        rows = 183
        columns = 275

        left = image_left.copy()
        right = image_right.copy()

        for x in range(rows):
            for y in range(column):
                right[x][y] = left_half[x][y]

        for x in range(rows):
            for y in range(column, columns):
                left[x][y] = right_half[x][y - column]

        # Please do not change the structure
        return left  # Currently the original image is returned, please replace this with the merged image

    def color_slicing(self, color_image, blackwhite_image, target_color, threshold):
        """
        Perform color slicing to create an image where only the targeted color is preserved and the rest
        is black and white

        color_image: the input color image
        blackwhite_image: the input black and white image
        target_color: the target color to be extracted
        threshold: the threshold to determine the pixel to determine the prximity to the target color

        return: output_image
        """
        
        # add your code here
        "color_image/blackwhite_image = nparray"
        "target_color = array with 3 values ex:[0 , 0, 225]"
        "threshold = float number ex: 180.0"

        rows = 183
        cols = 275

        "Create a result/output image of the same shape as the input color image"
        output_image = dip.zeros((183, 275, 3), dtype=dip.uint8)

        for x in range(rows):

            for y in range(cols):
                "Calculate the Euclidean distance between every pixel of the color image and the target color"
                r = (color_image[x, y, 0] - target_color[0]) ** 2
                g = (color_image[x, y, 1] - target_color[1]) ** 2
                b = (color_image[x, y, 2] - target_color[2]) ** 2
                euclidean = r + g + b
                "If the distance is smaller than threshold, copy the color pixel, "
                "else copy the black-and-white pixel to the output image"
                if euclidean <= threshold ** 2:
                    output_image[x, y, 0] = color_image[x, y, 0]
                    output_image[x, y, 1] = color_image[x, y, 1]
                    output_image[x, y, 2] = color_image[x, y, 2]
                else:
                    output_image[x, y, 0] = blackwhite_image[x, y, 0]
                    output_image[x, y, 1] = blackwhite_image[x, y, 1]
                    output_image[x, y, 2] = blackwhite_image[x, y, 2]

        # Please do not change the structure
        return output_image
        # Currently the input image is returned, please replace this with the color extracted image

   
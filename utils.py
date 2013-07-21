import globals
from math import sqrt, pow


def index_to_pixel(i):
    '''
        Returns the pixel in the center of the square
        Since the board is square, only one coordinate is necessary
        as it can be used equally in both axis
    '''
    return int(i*globals.square_size + globals.square_size / 2)


def pixel_to_index(p):
    '''
        Returns the index of the square containing the pixel coordinate
        Since the board is square, only one coordinate is necessary
        as it can be used equally in both axis
    '''
    return int(p/globals.square_size)


def distance((x1, y1), (x2, y2)):
    x = pow(x1-x2, 2)
    y = pow(y1-y2, 2)
    return sqrt(x+y)

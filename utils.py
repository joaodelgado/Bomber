from math import sqrt, pow

import globals


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
    index = int(p/globals.square_size)
    return max(0, min(index, globals.squares_per_line-1))


def distance((x1, y1), (x2, y2)):
    x = pow(x1-x2, 2)
    y = pow(y1-y2, 2)
    return sqrt(x+y)

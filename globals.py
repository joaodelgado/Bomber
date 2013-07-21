##############################################################################
#                                  CONSTANTS                                 #
##############################################################################
# BOARD
width = 800
height = 600
square_size = 40
squares_per_line = width/square_size
squares_per_column = height/square_size

# COLORS
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
orange = 255, 128, 0
# PLAYER
p_size_diff = 0.7
p_radious = int(square_size * p_size_diff / 2)

# BOMB
b_size_diff = 0.7
b_size = int(square_size * b_size_diff)

#explosion
e_size_diff = 0.3
e_size = int(square_size * e_size_diff)
##############################################################################
#                               GAME VARIABLES                               #
##############################################################################
screen = None
display = None
clock = None

squares = []  # matrix with the board squares
bombs = []  # list of all the bombs on the map
explosions = []

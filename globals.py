##############################################################################
#                                  CONSTANTS                                 #
##############################################################################
# BOARD
width = 800
height = 800
square_size = 40
squares_per_line = width/square_size
squares_per_column = height/square_size

# COLORS
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
orange = 255, 128, 0
yellow = 255, 255, 0
green = 0, 255, 0
brown = 128, 64, 0

# PLAYER
p_images = [] #player, pose, direction, frame

# BOMB
b_timer = 2000
b_images = []

# EXPLOSION
e_images = []

# POWERUPS
pw_timer = 5000
pw_chance = 0.05
pw_images = []

# OTHER
animation_speed = 200

##############################################################################
#                               GAME VARIABLES                               #
##############################################################################
# STATE
MAIN_MENU = 0
RUNNING = 1
PAUSED = 2
GAME_OVER = 3
EXIT = 4

# PLAYER STATE
P_S_MOVING = 0
P_S_STILL = 1

# PLAYER DIRECTION
P_D_FRONT = 0
P_D_LEFT = 1
P_D_RIGHT = 2
P_D_BACK = 3

game_state_label = MAIN_MENU
game_state = None
winner = None
player1_score = 0
player2_score = 0

# WINDOW
screen = None
display = None

# ENTITIES
squares = []  # matrix with the board squares
bombs = []  # list of all the bombs on the map
explosions = []  # list of all explosions on the map
powerups = []

# OTHER
clock = None

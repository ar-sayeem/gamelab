import pygame, sys
import numpy as np

pygame.init()   # always need to initialize pygame if we use import pygame

# const
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIOUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# colors
RED = (255, 0, 0)
GREEN = (0, 153, 0)
BG_COLOR = (102, 178, 255)
LINE_COLOR = (96, 96, 96)     # (23, 135, 135)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe (PvP)')

# Load and set the window icon
icon = pygame.image.load(r'C:\Users\DarkBoyAR\Desktop\GitHub-sayeem-ar\gamelab\Tic-Tac-Toe\icon.png')  # Replace 'path' with desired icon file location
pygame.display.set_icon(icon)

screen.fill(BG_COLOR)

# board
board = np.zeros((BOARD_ROWS, BOARD_COLS))
#print(board)


# Function to draw the lines of the Tic Tac Toe grid
def draw_lines():
    # horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # vertical
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:    # Player 1
                pygame.draw.circle(screen, RED, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIOUS, CIRCLE_WIDTH)
                                                # 600//3 = 200 , 100 = 600//6
            elif board[row][col] == 2:  # Player 2
                pygame.draw.line(screen, GREEN, (col * 200 + SPACE, row * 200 + SPACE),       (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, GREEN, (col * 200 + SPACE, row * 200 + 200 - SPACE), (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player

def avainable_square(row, col):
    return board[row][col] == 0       # [same as below comment]
''' if board[row][col]:
        return True
    else:
        return False
'''

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    
    return True

'''
# false
print(is_board_full())
#marking all squares
for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            mark_square(row, col, 1)
# board is full true
print(is_board_full())
'''
# is the middle square abailable?
# print(avainable_square(1, 1))
# mark_square(1, 1, 1)                # (1, 1) spot taken by P1, so not available
# print(avainable_square(1, 1))

# mark_square(0, 0, 1)
# mark_square(1, 1, 2)

# print(board)

draw_lines()

player = 1

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:        # cordinates of clicked position
            mouseX = event.pos[0]    # x
            mouseY = event.pos[1]    # y

            # print(mouseX)
            # print(mouseY)

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            # print(clicked_row)
            # print(clicked_col)

            if avainable_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square(clicked_row, clicked_col, 1)
                    player = 2
# after click toggle player
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    player = 1
                
                draw_figures()
            
                #print(board)



    pygame.display.update()

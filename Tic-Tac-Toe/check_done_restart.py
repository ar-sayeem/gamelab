import pygame, sys
import numpy as np

pygame.init()

# Constants
WIDTH = 600
HEIGHT = WIDTH
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
CIRCLE_COLOR = (255, 0, 0)
CROSS_COLOR = (0, 153, 0)
BG_COLOR = (102, 178, 255)
LINE_COLOR = (96, 96, 96)
TEXT_COLOR = (255, 255, 255)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe (PvP)')
icon = pygame.image.load('Tic-Tac-Toe/icon.png')
pygame.display.set_icon(icon)

board = np.zeros((BOARD_ROWS, BOARD_COLS))

def draw_lines():
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)

def draw_winning_line(start_pos, end_pos, player):
    color = CIRCLE_COLOR if player == 1 else CROSS_COLOR
    pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)

def check_win(player):
    for col in range(BOARD_COLS):
        if all(board[row][col] == player for row in range(BOARD_ROWS)):
            draw_winning_line((col * SQUARE_SIZE + SQUARE_SIZE // 2, 15), (col * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - 15), player)
            return True
    for row in range(BOARD_ROWS):
        if all(board[row][col] == player for col in range(BOARD_COLS)):
            draw_winning_line((15, row * SQUARE_SIZE + SQUARE_SIZE // 2), (WIDTH - 15, row * SQUARE_SIZE + SQUARE_SIZE // 2), player)
            return True
    if all(board[i][i] == player for i in range(BOARD_ROWS)):
        draw_winning_line((15, 15), (WIDTH - 15, HEIGHT - 15), player)
        return True
    if all(board[i][BOARD_ROWS - i - 1] == player for i in range(BOARD_ROWS)):
        draw_winning_line((15, HEIGHT - 15), (WIDTH - 15, 15), player)
        return True
    return False

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] == 0

def restart():
    global board, game_over, player
    game_over = False
    board.fill(0)
    draw_selection_screen()
    player = choose_starting_player()
    draw_figures()

def draw_selection_screen():
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, CIRCLE_COLOR, (0, 0, WIDTH // 2, HEIGHT))
    pygame.draw.rect(screen, CROSS_COLOR, (WIDTH // 2, 0, WIDTH // 2, HEIGHT))
    font = pygame.font.Font(None, 60)
    text_circle = font.render("Start as Circle", True, TEXT_COLOR)
    text_cross = font.render("Start as Cross", True, TEXT_COLOR)
    screen.blit(text_circle, (WIDTH // 4 - text_circle.get_width() // 2, HEIGHT // 2 - text_circle.get_height() // 2))
    screen.blit(text_cross, (3 * WIDTH // 4 - text_cross.get_width() // 2, HEIGHT // 2 - text_cross.get_height() // 2))
    pygame.display.update()

def choose_starting_player():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, _ = event.pos
                return 1 if x < WIDTH // 2 else 2

draw_selection_screen()
player = choose_starting_player()
restart()

game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = event.pos
            row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
            if available_square(row, col):
                mark_square(row, col, player)
                draw_figures()
                if check_win(player):
                    game_over = True
                else:
                    player = 3 - player
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            restart()
    pygame.display.update()
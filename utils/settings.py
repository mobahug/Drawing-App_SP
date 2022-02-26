import pygame
pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
GREY = (128, 128, 128)
YELLOW = (255, 211, 67)

FPS = 120

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 50

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // COLS

BG_COLOR = GREY

DRAWN_GRID_LINES = True

def get_font(size):
	return pygame.font.SysFont("comicsans", size)
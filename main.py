from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")

# Changed the background color to white and keep updating it

def init_grid(rows, cols, color):
	grid = []

	for i in range(rows):
		grid.append([])
		for _ in range(cols):
			grid[i].append(color)
	return grid

# drawing the pixels to the window
# and in the "DRAW_GRID_LINE" we making the webs for the pixels

def draw_grid(win, grid):
	for i, row in enumerate(grid):
		for j, pixel in enumerate(row):
			pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i* PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

	if DRAWN_GRID_LINES:
		for i in range(ROWS + 1):
			pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
		for i in range(COLS + 1):
			pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

# during drawing keep upfate the window

def draw(win, grid, buttons):
	win.fill(BG_COLOR)
	draw_grid(win, grid)

	for button in buttons:
		button.draw(win)

	pygame.display.update()

# after click to the window get pos for each pixel

def get_row_col_from_pos(pos):
	x, y = pos
	row = y // PIXEL_SIZE
	col = x // PIXEL_SIZE

	if row >= ROWS:
		raise IndexError

	return row, col

# window gonna only close if we click to exit button

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT / 2 - 25
buttons = [
	Button(10, button_y, 50, 50, BLACK),
	Button(70, button_y, 50, 50, RED),
	Button(130, button_y, 50, 50, GREEN),
	Button(190, button_y, 50, 50, BLUE),
	Button(250, button_y, 50, 50, YELLOW),
	Button(310, button_y, 50, 50, WHITE),
	Button(370, button_y, 50, 50, GREY, "Kumi", BLACK),
	Button(430, button_y, 50, 50, GREY, "Uusi", BLACK),
]

while run:
	clock.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if pygame.mouse.get_pressed()[0]:	# clicking mouse button left
			pos = pygame.mouse.get_pos()	# get pos
			try:
				row, col = get_row_col_from_pos(pos)
				grid[row][col] = drawing_color
			except IndexError:
				for button in buttons:
					if not button.clicked(pos):
						continue
					drawing_color = button.color
					if button.text == "Uusi":	# cleaning paper
						grid = init_grid(ROWS, COLS, BG_COLOR)
						drawing_color = BLACK
	draw(WIN, grid, buttons)
pygame.quit()

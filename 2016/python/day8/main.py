from aoc_utils import run_with_timer

data = [x.strip().split(" ") for x in open("input.txt").readlines()]


def init_screen(height, width):
	screen = []
	for y in range(height):
		screen.append(["."] * width)
	return screen


def print_screen(screen):
	for y in screen:
		print("".join(y))
	print()


def make_rect(height, width, screen):
	for y in range(height):
		for x in range(width):
			screen[y][x] = "#"


def rotate_row(row, amount, screen):
	screen[row] = screen[row][-amount:] + screen[row][0:-amount]


def rotate_column(col, amount, screen):
	new_col = []
	for y in range(amount):
		new_col.append(screen[len(screen) - amount + y][col])
	for y in range(len(screen) - amount):
		new_col.append(screen[y][col])
	for i in range(len(screen)):
		screen[i][col] = new_col[i]


def build_screen(height, width):
	screen = init_screen(height, width)
	for x in data:
		if x[0] == "rect":
			parts = x[1].split("x")
			make_rect(int(parts[1]), int(parts[0]), screen)
		elif x[0] == "rotate":
			parts = x[2].split("=")
			if x[1] == "column":
				rotate_column(int(parts[1]), int(x[4]), screen)
			elif x[1] == "row":
				rotate_row(int(parts[1]), int(x[4]), screen)
	return screen


def part_one():
	return sum(1 for y in build_screen(6, 50) for x in y if x == "#")


def part_two():
	print_screen(build_screen(6, 50))
	return 0


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

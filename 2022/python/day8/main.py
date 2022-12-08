from aoc_utils import run_with_timer

data = [[int(y) for y in x.strip()] for x in open("input.txt").readlines()]


def is_visible(grid, x, y):
	return left(grid, x, y, False) or top(grid, x, y, False) or right(grid, x, y, False) or bottom(grid, x, y, False)


def visibility_score(grid, x, y):
	return left(grid, x, y, True) * top(grid, x, y, True) * right(grid, x, y, True) * bottom(grid, x, y, True)


def left(grid, x, y, visibility):
	if x > 0:
		for a in range(x-1, -1, -1):
			if grid[y][a] >= grid[y][x]:
				return x - a if visibility else False
	return x if visibility else True


def top(grid, x, y, visibility):
	if y > 0:
		for a in range(y-1, -1, -1):
			if grid[a][x] >= grid[y][x]:
				return y - a if visibility else False
	return y if visibility else True


def right(grid, x, y, visibility):
	if x < len(grid[y]) - 1:
		for a in range(x+1, len(grid[y]), 1):
			if grid[y][a] >= grid[y][x]:
				return a - x if visibility else False
	return len(grid[y]) - 1 - x if visibility else True


def bottom(grid, x, y, visibility):
	if y < len(grid) - 1:
		for a in range(y+1, len(grid), 1):
			if grid[a][x] >= grid[y][x]:
				return a - y if visibility else False
	return len(grid) - 1 - y if visibility else True


def part_one():
	return sum(1 for y in range(len(data)) for x in range(len(data[y])) if is_visible(data, x, y))


def part_two():
	return max(visibility_score(data, x, y) for y in range(len(data)) for x in range(len(data[y])))


if __name__ == '__main__':
	run_with_timer(part_one)  # 1662 -- took 24 ms
	run_with_timer(part_two)  # 537600 -- took 29 ms

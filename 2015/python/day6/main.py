from aoc_utils import run_with_timer

data = [x.strip() for x in open('input.txt').readlines()]


def get_coords(instruction):
	idx = 2
	if 'toggle' in instruction:
		idx = 1
	return tuple(map(int, instruction.split(' ')[idx].split(','))), tuple(map(int, instruction.split(' ')[idx+2].split(',')))


def build_grid(pop_func):
	grid = [[0 for i in range(1000)] for i in range(1000)]
	for instruction in data:
		start_coord, end_coord = get_coords(instruction)
		for i in range(start_coord[0], end_coord[0]+1):
			for j in range(start_coord[1], end_coord[1]+1):
				pop_func(grid, j, i, instruction)
	return grid


def set_grid_val1(grid, j, i, instruction):
	grid[j][i] = 0 if 'turn off' in instruction else (1 if 'turn on' in instruction else (0 if grid[j][i] else 1))


def set_grid_val2(grid, j, i, instruction):
	delta = -1 if 'turn off' in instruction and grid[j][i] > 0 else 0
	grid[j][i] += delta if 'turn off' in instruction else (1 if 'turn on' in instruction else 2)


def part_one():
	return sum(row.count(1) for row in build_grid(set_grid_val1))


def part_two():
	total_brightness = 0
	for row in build_grid(set_grid_val2):
		for i in row:
			total_brightness += i
	return total_brightness


if __name__ == '__main__':
	run_with_timer(part_one)  # 400410
	run_with_timer(part_two)  # 15343601

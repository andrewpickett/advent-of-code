from aoc_utils import run_with_timer

data = [[y for y in x.strip()] for x in open('input.txt').readlines()]


def get_neighbor(lights, row, col):
	if 0 <= row < len(lights) and 0 <= col < len(lights[0]):
		return lights[row][col]


def get_immediate_neighbors(lights, row, col):
	return [
		get_neighbor(lights, row - 1, col - 1),
		get_neighbor(lights, row - 1, col),
		get_neighbor(lights, row - 1, col + 1),

		get_neighbor(lights, row, col + 1),
		get_neighbor(lights, row, col - 1),

		get_neighbor(lights, row + 1, col + 1),
		get_neighbor(lights, row + 1, col),
		get_neighbor(lights, row + 1, col - 1)
	]


def run_x_steps(lights, all_light_pos, step_count):
	for i in range(step_count):
		lights_to_switch = []
		for point in all_light_pos:
			neighbors = get_immediate_neighbors(lights, point[0], point[1])
			if lights[point[0]][point[1]] == '#' and neighbors.count('#') not in (2, 3):
				lights_to_switch.append(point)
			elif lights[point[0]][point[1]] == '.' and neighbors.count('#') == 3:
				lights_to_switch.append(point)
		for light in lights_to_switch:
			lights[light[0]][light[1]] = '.' if lights[light[0]][light[1]] == '#' else '#'
	return sum(x.count('#') for x in lights)


def part_one():
	lights = [list(x) for x in data]
	all_light_pos = [(row, col) for row in range(len(lights)) for col in range(len(lights[row]))]
	return run_x_steps(lights, all_light_pos, 100)


def part_two():
	lights = [list(x) for x in data]
	lights[0][0] = '#'
	lights[0][-1] = '#'
	lights[-1][0] = '#'
	lights[-1][-1] = '#'
	all_light_pos = [(row, col) for row in range(len(lights)) for col in range(len(lights[row]))]
	all_light_pos.remove((0, 0))
	all_light_pos.remove((0, len(lights[0])-1))
	all_light_pos.remove((len(lights)-1, 0))
	all_light_pos.remove((len(lights)-1, len(lights[0])-1))
	return run_x_steps(lights, all_light_pos, 100)


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

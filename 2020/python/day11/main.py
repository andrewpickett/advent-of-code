from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def get_neighbor(seat_map, row, col):
	if 0 <= row < len(seat_map) and 0 <= col < len(seat_map[0]):
		return seat_map[row][col]


def get_immediate_neighbors(seat_map, row, col):
	return [
		get_neighbor(seat_map, row-1, col-1),
		get_neighbor(seat_map, row-1, col),
		get_neighbor(seat_map, row-1, col+1),

		get_neighbor(seat_map, row, col+1),
		get_neighbor(seat_map, row, col-1),

		get_neighbor(seat_map, row+1, col+1),
		get_neighbor(seat_map, row+1, col),
		get_neighbor(seat_map, row+1, col-1)
	]


def get_neighbor_row(seat_map, row, col):
	row_neighbors = []
	row_neighbors += [i for i in ''.join(seat_map[row][col+1:]) if i != '.'][0:1]
	row_neighbors += [i for i in ''.join(seat_map[row][:col])[::-1] if i != '.'][0:1]
	return row_neighbors


def get_neighbor_col(seat_map, row, col):
	col_neighbors = []
	col_neighbors += [i for i in ''.join([seat_map[x][col] for x in range(row)])[::-1] if i != '.'][0:1]
	col_neighbors += [i for i in ''.join([seat_map[x][col] for x in range(row+1, len(seat_map))]) if i != '.'][0:1]
	return col_neighbors


def get_diagonal_neighbor(seat_map, row, col, row_inc, col_inc):
	curr_row = row + row_inc
	curr_col = col + col_inc
	while 0 <= curr_row < len(seat_map) and 0 <= curr_col < len(seat_map[0]):
		if seat_map[curr_row][curr_col] != '.':
			return seat_map[curr_row][curr_col]
		curr_row += row_inc
		curr_col += col_inc


def get_neighbor_diags(seat_map, row, col):
	return [
		get_diagonal_neighbor(seat_map, row, col, -1, -1),
		get_diagonal_neighbor(seat_map, row, col, -1, 1),
		get_diagonal_neighbor(seat_map, row, col, 1, -1),
		get_diagonal_neighbor(seat_map, row, col, 1, 1)
	]


def get_distanced_neighbors(seat_map, row, col):
	neighbors = []
	neighbors += get_neighbor_row(seat_map, row, col)
	neighbors += get_neighbor_col(seat_map, row, col)
	neighbors += get_neighbor_diags(seat_map, row, col)
	return neighbors


def run_until_equillibrium(f, seat_map, neighbor_count):
	points_to_check = [(row, col) for row in range(len(seat_map)) for col in range(len(seat_map[row])) if seat_map[row][col] != '.']
	while True:
		points_to_switch = []
		for point in points_to_check:
			neighbors = f(seat_map, point[0], point[1])
			if not int(seat_map[point[0]][point[1]]) and not any(neighbors):
				points_to_switch.append(point)
			elif int(seat_map[point[0]][point[1]]) and sum(neighbors) >= neighbor_count:
				points_to_switch.append(point)
		for point in points_to_switch:
			seat_map[point[0]][point[1]] = (int(seat_map[point[0]][point[1]]) + 1) % 2

		if len(points_to_switch) == 0:
			break
	return sum(x for x in seat_map)


def part_one():
	return run_until_equillibrium(get_immediate_neighbors, [list(x) for x in data], 4)


def part_two():
	return run_until_equillibrium(get_distanced_neighbors, [list(x) for x in data], 5)


if __name__ == '__main__':
	run_with_timer(part_one)  # 2319 -- took 2077 ms
	run_with_timer(part_two)  # 2117 -- took 17833 ms

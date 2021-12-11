from aoc_utils import run_with_timer, Grid

data = [list(x.strip()) for x in open("input.txt").readlines()]


def take_step(m):
	for row in range(m.get_height()):
		for col in range(m.get_width()):
			p = m.get_point(row, col)
			p.set_value(int(p.get_value()) + 1)

	flashed_points = set()
	for row in range(m.get_height()):
		for col in range(m.get_width()):
			p = m.get_point(row, col)
			if p.get_value() > 9 and p not in flashed_points:
				increment_and_flash_neighbors(p, flashed_points)
	for point in flashed_points:
		point.set_value(0)
	return len(flashed_points)


def increment_and_flash_neighbors(p, flashed_points):
	flashed_points.add(p)
	for neighbor in p.get_neighbors():
		neighbor.set_value(neighbor.get_value() + 1)
		if neighbor.get_value() > 9 and neighbor not in flashed_points:
			increment_and_flash_neighbors(neighbor, flashed_points)


def part_one():
	m = Grid(values=data)
	m.set_neighbors_for_all(True)
	return sum(take_step(m) for _ in range(1, 101))


def part_two():
	m = Grid(values=data)
	m.set_neighbors_for_all(True)

	i = 0
	while not sum(1 for row in range(m.get_height()) if len(list(filter(lambda x: x.get_value() != 0, m.get_row(row)))) != 0) == 0:
		take_step(m)
		i += 1
	return i


if __name__ == '__main__':
	run_with_timer(part_one)  # 1675 -- took 46 ms
	run_with_timer(part_two)  # 515 -- took 206 ms

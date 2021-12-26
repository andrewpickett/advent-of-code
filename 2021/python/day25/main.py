from aoc_utils import run_with_timer

data = [list(x.strip()) for x in open("input.txt").readlines()]


class Cucumber:
	def __init__(self, row, col, val):
		self.row = row
		self.col = col
		self.val = val

	def __str__(self):
		return "(" + str(self.row) + "," + str(self.col) + ")"

	def __repr__(self):
		return str(self)

	def __eq__(self, other):
		return self.row == other.row and self.col == other.col

	def __hash__(self):
		return hash(str(self))


def move(east_cukes, south_cukes, is_east):
	points_to_move = []
	points_to_remove = []
	cukes = east_cukes if is_east else south_cukes
	for ecuke in cukes:
		if is_east:
			m = Cucumber(ecuke.row, (ecuke.col + 1) % len(data[0]), ecuke.val)
		else:
			m = Cucumber((ecuke.row + 1) % len(data), ecuke.col, ecuke.val)
		if m not in east_cukes and m not in south_cukes:
			points_to_move.append(m)
			points_to_remove.append(ecuke)
	for p in points_to_remove:
		cukes.remove(p)
	for p in points_to_move:
		cukes.add(p)
	return len(points_to_move) > 0


def part_one():
	east_cukes = set()
	south_cukes = set()
	for i, row in enumerate(data):
		for j, col in enumerate(row):
			if col == '>':
				east_cukes.add(Cucumber(i, j, '>'))
			if col == 'v':
				south_cukes.add(Cucumber(i, j, 'v'))

	still_moving = True
	i = 0
	while still_moving:
		still_moving = False
		still_moving = move(east_cukes, south_cukes, True) or still_moving
		still_moving = move(east_cukes, south_cukes, False) or still_moving
		i += 1
	return i


def part_two():
	return


if __name__ == '__main__':
	run_with_timer(part_one)  # 563 -- took 31983 ms
	run_with_timer(part_two)  # None -- took 0 ms

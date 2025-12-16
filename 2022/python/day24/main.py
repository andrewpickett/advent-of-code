from aoc_utils import run_with_timer, Grid

data = [x.strip() for x in open("input.txt").readlines()]


dirs = {	">": (0, 1), "v": (1, 0), "<": (0, -1), "^": (-1, 0) }


def parse_input():
	# Use my Grid class, just to get the values, we don't actually need to use it, though...
	g = Grid(values=data)
	start = g.get_point(0, data[0].index("."))
	end = g.get_point(len(data)-1, data[-1].index("."))

	blizzards = {">": [], "v": [], "<": [], "^": []}
	for x in g.get_points():
		if x.get_value() not in [".", "#"]:
			blizzards[x.get_value()].append(x)
	return start, end, blizzards


def move_blizzards(blizzards):
	for x in blizzards:
		x.set_row(x.get_row()+dirs[x.get_value()][0], x.get_col()+dirs[x.get_value()][1])


def part_one():
	start, end, blizzards = parse_input()
	curr = start
	q = {start}
	while curr != end:
		# Block the start square, so we don't escape.
		if curr != start and start.get_value() != "#":
			start.set_value("#")
		if curr == start:
			# only allow them to move "down" from the start.
			pass
		# Alright, BFS TIME!!
	return


def part_two():
	return


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

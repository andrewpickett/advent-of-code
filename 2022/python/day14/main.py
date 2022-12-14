from aoc_utils import run_with_timer, Grid

data = [x.strip().split(" -> ") for x in open("input.txt").readlines()]


def get_floor_level():
	return max(int(y.split(",")[1]) for x in data for y in x) + 2


def build_world(start_x, add_floor=False):
	height = get_floor_level()
	g = Grid(height+1, start_x*2, default_value=".")
	g.get_point(0, start_x).set_value("+")
	if add_floor:
		for x in range(g.width):
			g.get_point(height, x).set_value("#")
	for x in data:
		for i in range(1, len(x)):
			dest = [int(y) for y in x[i].split(",")]
			src = [int(y) for y in x[i-1].split(",")]

			for row in range(min(dest[0], src[0]), max(dest[0], src[0])+1):
				p = g.get_point(dest[1], row-(500+start_x))
				p.set_value("#")
			for col in range(min(dest[1], src[1]), max(dest[1], src[1])+1):
				p = g.get_point(col, dest[0]-(500+start_x))
				p.set_value("#")
	return g


def drop_sand(g, start_x):
	total_sand = 0
	while True:
		sand_pos = g.get_point(0, start_x)
		if sand_pos.get_value() == "o":
			return total_sand
		at_rest = False
		while not at_rest:
			if sand_pos.get_row() + 1 >= g.get_height():
				return total_sand
			next_pos = g.get_point(sand_pos.get_row()+1, sand_pos.get_col())
			if next_pos.get_value() == ".":
				sand_pos = next_pos
			elif next_pos.get_value() in ["#", "o"]:
				next_pos = g.get_point(sand_pos.get_row()+1, sand_pos.get_col()-1)
				if next_pos.get_value() == ".":
					sand_pos = next_pos
				elif next_pos.get_value() in ["#", "o"]:
					next_pos = g.get_point(sand_pos.get_row()+1, sand_pos.get_col()+1)
					if next_pos.get_value() == ".":
						sand_pos = next_pos
					else:
						sand_pos.set_value("o")
						total_sand += 1
						at_rest = True


def part_one():
	return drop_sand(build_world(100), 100)


def part_two():
	return drop_sand(build_world(200, True), 200)


if __name__ == '__main__':
	run_with_timer(part_one)  # 692 -- took 207 ms
	run_with_timer(part_two)  # 31706 -- took 15189 ms

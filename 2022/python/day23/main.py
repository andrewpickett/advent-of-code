from aoc_utils import run_with_timer, Grid

data = [x.strip() for x in open("input.txt").readlines()]


def parse_data():
	g = Grid(values=data)
	g.set_neighbors_for_all(include_diagonals=True)
	return g


def get_proposed_points(elf, r, g):
	dirs = [{"f": elf.get_north_neighbors, "p": (-1, 0)}, {"f": elf.get_south_neighbors, "p": (1, 0)}, {"f": elf.get_west_neighbors, "p": (0, -1)}, {"f": elf.get_east_neighbors, "p": (0, 1)}]
	proposed_points = []
	for i in range(len(dirs)):
		d = dirs[((r % 4) + i) % 4]
		n = d["f"]()
		if len(n) > 0 and sum(1 for p in n if p.get_value() == "#") == 0:
			proposed_points.append(g.get_point(elf.get_row()+d["p"][0], elf.get_col()+d["p"][1]))
	return proposed_points


def part_one():
	g = parse_data()
	elves_moved = True
	r = 0
	while elves_moved and r < 5:
		print(g.output())
		elf_positions = [p for p in g.get_points() if p.get_value() == "#"]
		elves_moved = False
		# part 1: the proposal
		proposals = {}
		all_props = set()
		negated_props = set()
		for elf in elf_positions:
			proposals[elf] = []
			if sum(1 for p in elf.get_neighbors() if p.get_value() == "#") > 0:
				for i in get_proposed_points(elf, r, g):
					if i in all_props:
						negated_props.add(i)
					proposals[elf].append(i)
					all_props.add(i)

		# part 2 - actually move if possible:
		print(proposals)
		for e, p in proposals.items():
			if len(p) > 0 and p[0] not in negated_props:
				elves_moved = True
				p[0].set_value("#")
				e.set_value(".")
		r += 1
	return


def part_two():
	return


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

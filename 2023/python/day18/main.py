from utils.timers import run_with_timer


def get_data(filename):
	return [x.strip().split() for x in open(filename).readlines()]


dirs = {"R": (1, 0), "U": (0, -1), "L": (-1, 0), "D": (0, 1)}


def calc_area(points):
	curr_pos = (0, 0)
	all_pos = [curr_pos]
	p = 0
	for i, x in enumerate(points):
		curr_pos = (curr_pos[0]+(dirs[x[0]][0]*int(x[1])), curr_pos[1]+(dirs[x[0]][1]*int(x[1])))
		all_pos.append(curr_pos)
		p += abs((all_pos[i+1][1] - all_pos[i][1])) + abs((all_pos[i+1][0] - all_pos[i][0]))
	a = abs(sum((all_pos[i-1][1] * all_pos[i][0] - all_pos[i][1] * all_pos[i-1][0]) for i in range(len(all_pos)))) / 2  # Shoelace Theorem
	i = a + 1 - (p / 2)  # Pick's Theorem
	return int(i + p)


def part_one(d):
	return calc_area(d)


def part_two(d):
	dlookup = {"0": "R", "1": "D", "2": "L", "3": "U"}
	new_data = map(lambda x: (dlookup[x[2][-2]], int(x[2][2:-2], 16)), d)
	return calc_area(new_data)


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

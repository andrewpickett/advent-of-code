from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x for x in open(filename).readline().strip().split(",")]


dir_mapping = {
	"n": (0, 2), "s": (0, -2), "ne": (1, 1), "nw": (-1, 1), "se": (1, -1), "sw": (-1, -1)
}


def traverse(d):
	curr_pos = (0, 0)
	dists = []
	for x in d:
		curr_pos = (curr_pos[0] + dir_mapping[x][0], curr_pos[1] + dir_mapping[x][1])
		dists.append(get_dist(curr_pos))
	return dists


def get_dist(p):
	return (abs(p[1]) + abs(p[0])) // 2 if abs(p[1]) > abs(p[0]) else abs(p[0])


def part_one(d):
	return traverse(d)[-1]


def part_two(d):
	return max(traverse(d))


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

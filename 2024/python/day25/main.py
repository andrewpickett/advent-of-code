from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import rotate_matrix


def get_data(filename):
	keys = []
	locks = []
	for grid in [x for x in open(filename).read().split("\n\n")]:
		g = [x for x in grid.split("\n") if x != ""]
		tmp = [x.count("#") for x in rotate_matrix(g)]
		if "." in g[0]:
			keys.append(tmp)
		elif "#" in g[0]:
			locks.append(tmp)
	return keys, locks


def part_one(d):
	return sum(1 for key in d[0] for lock in d[1] if sum(1 for i in range(len(key)) if key[i] + lock[i] <= 7) == len(key))


def part_two(d):
	return


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

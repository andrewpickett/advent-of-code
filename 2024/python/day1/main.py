from utils.timers import run_with_timer, get_data_with_timer
from collections import defaultdict


def get_data(filename):
	lines = [list(map(int, x.strip().split())) for x in open(filename).readlines()]
	l1 = [x[0] for x in lines]
	l2 = [x[1] for x in lines]
	l1.sort()
	l2.sort()
	return [l1, l2]


def part_one(d):
	return sum(abs(d[0][x] - d[1][x]) for x in range(len(d[0])))


def part_two(d):
	counts = defaultdict(lambda: 0)
	for x in d[1]:
		counts[x] += 1
	return sum(x * (counts[x] if x in counts else 0) for x in d[0])


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

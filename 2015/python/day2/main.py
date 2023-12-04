from utils.timers import run_with_timer


def get_data(filename):
	return [tuple(map(int, x.split('x'))) for x in open(filename).readlines()]


def part_one(d):
	return sum(2*i[0]*i[1] + 2*i[0]*i[2] + 2*i[1]*i[2] + min(i[0]*i[1], i[0]*i[2], i[1]*i[2]) for i in d)


def part_two(d):
	return sum(2*min(i[0]+i[1], i[0]+i[2], i[1]+i[2]) + (i[0]*i[1]*i[2]) for i in d)


if __name__ == '__main__':
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

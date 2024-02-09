from utils.timers import run_with_timer


def get_data(filename):
	return [int(x.strip()) for x in open(filename).readlines()]


def run_prog(d, jump_code):
	p = 0
	counter = 0
	while 0 <= p < len(d):
		jump = d[p]
		d[p] += jump_code(jump)
		p += jump
		counter += 1
	return counter


def part_one(d):
	return run_prog(d, lambda a: 1)


def part_two(d):
	return run_prog(d, lambda a: -1 if a >= 3 else 1)


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data.copy())
	run_with_timer(part_two, data.copy())

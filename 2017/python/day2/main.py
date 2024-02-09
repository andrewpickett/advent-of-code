from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [[int(y) for y in x.split()] for x in open(filename).readlines()]


def part_one(d):
	return sum(max(x) - min(x) for x in d)


def part_two(d):
	return sum(sum(max(x[y], x[z]) // min(x[y], x[z]) for y in range(len(x)) for z in range(y+1, len(x)) if max(x[y], x[z]) % min(x[y], x[z]) == 0) for x in d)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip().split() for x in open(filename).readlines()]


def part_one(d):
	return sum(1 for x in d if len(x) == len(set(x)))


def part_two(d):
	c = 0
	for x in d:
		words = [''.join(sorted(y)) for y in x]
		if len(words) == len(set(words)):
			c += 1
	return c


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

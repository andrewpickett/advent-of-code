from utils.timers import run_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def part_one(d):
	return sum(1 for x in d if len(x.split()) == len(set(x.split())))


def part_two(d):
	c = 0
	for x in d:
		words = [''.join(sorted(y)) for y in x.split()]
		if len(words) == len(set(words)):
			c += 1
	return c


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data.copy())
	run_with_timer(part_two, data.copy())

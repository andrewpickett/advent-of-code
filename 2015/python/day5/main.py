from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def part_one(d):
	return sum(1 for x in d if sum(x.count(vowel) for vowel in 'aeiou') >= 3 and sum(x.count(f) for f in ['ab', 'cd', 'pq', 'xy']) == 0 and sum(x[i] == x[i+1] for i in range(len(x)-1)))


def part_two(d):
	return sum(1 for x in d if sum(x.count(x[i:i+2]) for i in range(len(x)-1)) > len(x)-1 and sum(x[i] == x[i+2] for i in range(len(x)-2)) > 0)


if __name__ == '__main__':
	data = get_data_with_timer(get_data, "input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


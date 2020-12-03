from aoc_utils import run_with_timer

data = [x.strip() for x in open('input.txt').readlines()]


def part_one():
	return sum(1 for x in data if sum(x.count(vowel) for vowel in 'aeiou') >= 3 and sum(x.count(f) for f in ['ab', 'cd', 'pq', 'xy']) == 0 and sum(x[i] == x[i+1] for i in range(len(x)-1)))


def part_two():
	return sum(1 for x in data if sum(x.count(x[i] + x[i+1]) for i in range(len(x)-1)) > len(x)-1 and sum(x[i] == x[i+2] for i in range(len(x)-2)) > 0)


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #


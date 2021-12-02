from aoc_utils import run_with_timer

data = [x.strip().split() for x in open("input.txt").readlines()]


def part_one():
	dist = sum(int(d[1]) for d in data if d[0] == 'forward')
	depth = sum(int(d[1]) for d in data if d[0] == 'down') - sum(int(d[1]) for d in data if d[0] == 'up')
	return dist * depth


def part_two():
	curr_depth = 0
	curr_dist = 0
	curr_aim = 0
	for d in data:
		match d[0]:
			case 'forward':
				curr_dist += int(d[1])
				curr_depth += curr_aim * int(d[1])
			case 'down':
				curr_aim += int(d[1])
			case 'up':
				curr_aim -= int(d[1])
	return curr_depth * curr_dist


if __name__ == '__main__':
	run_with_timer(part_one)  # 1660158 -- took 0 ms
	run_with_timer(part_two)  # 1604592846 -- took 0 ms

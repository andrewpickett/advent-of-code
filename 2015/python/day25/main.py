from aoc_utils import run_with_timer

data = open('input.txt').readline().strip().split(" ")


def get_fill_order(row, col):
	tmp = row + col - 2
	return (tmp * (tmp+1) // 2) + col


def part_one():
	fill_order = get_fill_order(int(data[16][:-1]), int(data[18][:-1]))
	val = 20151125
	for i in range(2, fill_order+1):
		val = (val * 252533) % 33554393
	return val


def part_two():
	return


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

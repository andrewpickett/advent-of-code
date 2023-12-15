from utils.timers import run_with_timer


def get_data(filename):
	return open(filename).readline().strip().split(" ")


def get_fill_order(row, col):
	tmp = row + col - 2
	return (tmp * (tmp+1) // 2) + col


def part_one(d):
	fill_order = get_fill_order(int(d[16][:-1]), int(d[18][:-1]))
	val = 20151125
	for i in range(2, fill_order+1):
		val = (val * 252533) % 33554393
	return val


def part_two(d):
	return True


if __name__ == '__main__':
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

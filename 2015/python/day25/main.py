from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	d = open(filename).readline().strip().split(" ")
	return int(d[16][:-1]), int(d[18][:-1])


def get_fill_order(d):
	tmp = d[0] + d[1] - 2
	return (tmp * (tmp+1) // 2) + d[1]


def part_one(d):
	fill_order = get_fill_order(d)
	val = 20151125
	for i in range(2, fill_order+1):
		val = (val * 252533) % 33554393
	return val


def part_two(d):
	return True


if __name__ == '__main__':
	data = get_data_with_timer(get_data, "input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

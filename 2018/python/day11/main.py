from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	grid_level = int(open(filename).readline())
	grid = [[0]*301 for i in range(301)]
	for y in range(301):
		for x in range(301):
			grid[y][x] = calc_power_level(x, y, grid_level)
	return grid


def part_one(d):
	best = calc_total_power(d, 3)
	return ','.join([str(x) for x in best[0:2]])


def part_two(d):
	abs_best = (0, 0, 0, float("-inf"))
	for i in range(1, 13): # TODO: figure out why this is the limit...?
		best = calc_total_power(d, i)
		if best[3] > abs_best[3]:
			abs_best = best
	return ','.join([str(x) for x in abs_best[0:3]])


def calc_total_power(grid, size):
	best = (0, 0, size, float("-inf"))
	for y in range(1, 302-size):
		for x in range(1, 302-size):
			s = sum(sum(grid[t][x:x+size]) for t in range(y, y+size))
			if s > best[3]:
				best = (x, y, size, s)
	return best


def calc_power_level(x, y, d):
	power_level = x**2*y + 20*x*y + 100*y + d*x + 10*d
	return -5 if power_level < 100 else ((power_level // 100) % 10) - 5


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

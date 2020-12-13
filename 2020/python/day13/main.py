from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def part_one():
	depart_time = int(data[0])
	bus_list = [int(x) for x in data[1].split(',') if x != 'x']
	next_dep_times = []
	bus_map = {}
	for x in bus_list:
		next_time = (((depart_time // x)+1) * x) - depart_time
		next_dep_times.append(next_time)
		bus_map[str(next_time)] = x

	my_bus = min(next_dep_times)
	return my_bus * bus_map[str(my_bus)]


def part_two():
	my_list = [(int(x), i) for i, x in enumerate(data[1].split(',')) if x != 'x']

	interval = my_list[0][0]
	t = 0
	for time, offset in my_list[1:]:
		while True:
			t += interval
			if (t + offset) % time == 0:
				break
		interval *= time
	return t


if __name__ == '__main__':
	run_with_timer(part_one)  # 2305 -- took 0 ms
	run_with_timer(part_two)  # 552612234243498 -- took 0 ms

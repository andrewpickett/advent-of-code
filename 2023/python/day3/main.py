from utils.timers import run_with_timer
from utils.grid import Grid


def get_data(filename):
	grid = Grid(values=[x.strip() for x in open(filename).readlines()])
	grid.set_neighbors_for_all(True)
	return grid


def add_and_reset(nums, curr_num, is_adj):
	if curr_num and is_adj:
		nums.append(curr_num)
	return 0, False


def part_one(d):
	nums = []
	curr_num = 0
	is_adj = False
	for pt in d.get_points():
		if pt.value.isdigit():
			if pt.get_west_neighbor() and pt.get_west_neighbor().value.isdigit():
				curr_num *= 10
			curr_num += int(pt.value)

			is_adj = is_adj or len([x for x in pt.get_neighbors() if not x.value.isdigit() and x.value != "."]) > 0

			if not pt.get_east_neighbor():
				curr_num, is_adj = add_and_reset(nums, curr_num, is_adj)
		else:
			curr_num, is_adj = add_and_reset(nums, curr_num, is_adj)
	return sum(nums)


def add_and_reset2(gear_number_counts, curr_num, adj_gear):
	if curr_num and adj_gear:
		if adj_gear not in gear_number_counts:
			gear_number_counts[adj_gear] = []
		gear_number_counts[adj_gear].append(curr_num)
	return 0, None


def part_two(d):
	gears = {}
	curr_num = 0
	curr_adj_gear = None
	for pts in d.get_points():
		if pts.value.isdigit():
			if pts.get_west_neighbor() and pts.get_west_neighbor().value.isdigit():
				curr_num *= 10
			curr_num += int(pts.value)

			if not curr_adj_gear and len([x for x in pts.get_neighbors() if x.value == "*"]) > 0:
				for y in [x for x in pts.get_neighbors() if x.value == "*"]:
					curr_adj_gear = y

			if not pts.get_east_neighbor():
				curr_num, curr_adj_gear = add_and_reset2(gears, curr_num, curr_adj_gear)
		else:
			curr_num, curr_adj_gear = add_and_reset2(gears, curr_num, curr_adj_gear)

	return sum(v[0] * v[1] for k, v in gears.items() if len(v) == 2)


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

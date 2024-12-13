from utils.timers import run_with_timer, get_data_with_timer
from utils.input import read_input_as_2d_str_grid
from utils.utils import tuple_add, NEIGHBOR_COORDS
from collections import deque


def get_data(filename):
	return {(y, x): col for y, row in enumerate(read_input_as_2d_str_grid(filename)) for x, col in enumerate(row)}


def part_one(d):
	return sum(len(region[1]) * get_perimeter(region[1]) for region in get_regions(d))


def part_two(d):
	return sum(len(region[1]) * get_sides(region[1]) for region in get_regions(d))


def get_regions(garden):
	regions = []
	points_to_assign = set(garden.keys())
	while len(points_to_assign) > 0:
		pt = points_to_assign.pop()
		r = find_region(garden, pt)
		points_to_assign -= r
		regions.append((garden[pt], r))
	return regions


def find_region(garden, pt):
	region = {pt}
	label = garden[pt]
	q = deque([pt])
	while q:
		p = q.popleft()
		for z in tuple_add(NEIGHBOR_COORDS["orthogonal"], (p[0], p[1])):
			if z in garden and z not in region and garden[z] == label:
				q.append(z)
				region.add(z)
	return region


def get_perimeter(region):
	return sum(1 for x in list(region) for z in tuple_add(NEIGHBOR_COORDS["orthogonal"], (x[0], x[1])) if z not in region)


def get_sides(region):
	corners = 0
	for pos in region:
		if all([x not in region for x in tuple_add([(-1, 0), (0, 1)], pos)]):
			corners += 1
		if all([x not in region for x in tuple_add([(-1, 0), (0, -1)], pos)]):
			corners += 1
		if all([x not in region for x in tuple_add([(1, 0), (0, -1)], pos)]):
			corners += 1
		if all([x not in region for x in tuple_add([(1, 0), (0, 1)], pos)]):
			corners += 1

		if (pos[0] - 1, pos[1]) in region and (pos[0], pos[1] + 1) in region and (pos[0] - 1, pos[1] + 1) not in region:
			corners += 1
		if (pos[0] - 1, pos[1]) in region and (pos[0], pos[1] - 1) in region and (pos[0] - 1, pos[1] - 1) not in region:
			corners += 1
		if (pos[0] + 1, pos[1]) in region and (pos[0], pos[1] - 1) in region and (pos[0] + 1, pos[1] - 1) not in region:
			corners += 1
		if (pos[0] + 1, pos[1]) in region and (pos[0], pos[1] + 1) in region and (pos[0] + 1, pos[1] + 1) not in region:
			corners += 1
	return corners


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

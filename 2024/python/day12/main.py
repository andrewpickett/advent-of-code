from utils.timers import run_with_timer, get_data_with_timer
from utils.input import read_input_as_2d_str_grid
from utils.utils import tuple_add, NEIGHBOR_COORDS
from collections import deque, defaultdict


def get_data(filename):
	return {(y, x): col for y, row in enumerate(read_input_as_2d_str_grid(filename)) for x, col in enumerate(row)}


def part_one(d):
	return sum(len(region[1]) * get_perimeter(region[1]) for region in get_regions(d))


def part_two(d):
	for region in get_regions(d):
		area = len(region[1])
		sides = get_sides(d, region[1])
		print(region, "has area", area, "and", sides, "sides")
	# return sum(len(region[1]) * get_sides(d, region[1]) for region in get_regions(d))
	return

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



def get_sides(garden, region):
	perimeter_objects = defaultdict(lambda: (0, True))
	for pos in region:
		neighbors = {z for z in tuple_add(NEIGHBOR_COORDS["orthogonal"], (pos[0], pos[1])) if z not in region}
		perimeter_objects[pos] = (len(neighbors), True)
	print("Found these perimeter objects:", perimeter_objects)
	# inside corner check
	for pos, vals in perimeter_objects.ite:

	for pos in region:
		neighbors = {z for z in tuple_add(NEIGHBOR_COORDS["diagonal"], (pos[0], pos[1])) if z not in region}
		if neighbors and perimeter_objects[pos] == 0:
			perimeter_objects[pos] = (len(neighbors), False)
	sides = 0
	for k, v in perimeter_objects.items():
		print(k, "has", 2**(v[0]-2) if v[1] and v[0] > 1 else v[0], "corners")
		sides += 2**(v[0]-2) if v[1] and v[0] > 1 else v[0]
	# print(region, sides)
	return sides
	# distinct_sides = 0
	# while len(perimeter_objects) > 0:
	# 	pos, d = perimeter_objects.pop()
	# 	distinct_sides += 1
	# 	next = pos + d * 1j
	# 	while (next, d) in perimeter_objects:
	# 		perimeter_objects.remove((next, d))
	# 		next += d * 1j
	# 	next = pos + d * -1j
	# 	while (next, d) in perimeter_objects:
	# 		perimeter_objects.remove((next, d))
	# 		next += d * -1j
	# return distinct_sides


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main("sample.txt")

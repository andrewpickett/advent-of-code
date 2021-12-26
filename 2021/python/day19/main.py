from aoc_utils import run_with_timer

data = [x.strip() for x in open("sample.txt").readlines()]

rx = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
ry = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]
rz = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]

# run through these rotations in order to hit all 24 cases.
# start, y, y, y, 	x, y, y, y, 		x, y, y, y, 		z', y, y, y			z, y, y, y			z, x, x, x
# 1t, 1r, 1b, 1l, 	4l, 4t, 4r, 4b 	5r, 5b, 5l, 5t		2l, 2t, 2r, 2b		3b, 3l, 3t, 3r		6l, 6t, 6r, 6b
rotation_sequence = ['y', 'y', 'y', 'x', 'y', 'y', 'y', 'x', 'y', 'y', 'y', '-z', 'y', 'y', 'y', 'z', 'y', 'y', 'y', 'z', 'y', 'y', 'y']


def map_scanners():
	scanner_map = []
	curr_scanner = None
	for x in data:
		if x != "":
			if x.startswith("---"):
				if curr_scanner is not None:
					scanner_map.append(curr_scanner)
				curr_scanner = []
			else:
				coords = x.split(",")
				curr_scanner.append((int(coords[0]), int(coords[1]), int(coords[2])))
	scanner_map.append(curr_scanner)
	return scanner_map


def rotate(space, axis):
	rot_mat = rx
	if axis == 'y':
		rot_mat = ry
	elif axis == 'z':
		rot_mat = rz
	new_points = []
	for p in space:
		new_points.append([sum((rot_mat[i][k] * p[k]) for k in range(len(rot_mat[0]))) for i in range(len(p))])
	return new_points


def check_for_match(ref_space, space):
	return False


def do_all_rotations_until_matched(ref_space, space):
	matched = check_for_match(ref_space, space)
	if not matched:
		for x in rotation_sequence:
			space = rotate(space, x)
			if x.startswith("-"):
				space = rotate(space, x)
				space = rotate(space, x)
			matched = check_for_match(ref_space, space)
			if matched:
				break
	if matched:
		print("Matched one!")
		return space


def part_one():
	scanner_map = map_scanners()
	for p in scanner_map:
		for q in scanner_map:
			if p != q:
				do_all_rotations_until_matched(p, q)
	return


def part_two():
	return


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #


# from itertools import permutations
# import numpy as np
#
#
# # Rotation matrices
# Rx = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
# Ry = [[0, 0, -1], [0, 1, 0], [1, 0, 0]]
# Rz = [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
# Mx = [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]
# My = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
# Mz = [[1, 0, 0], [0, 1, 0], [0, 0, -1]]
# transformations = ((Mx, Rx), (My, Ry), (Mz, Rz))
#
#
# def cloud_rotations(cloud):
# 	x = cloud
# 	for i in range(4):
# 		yield x
# 		y = list(map(lambda v: tuple(np.dot(Rz, v)), x))
# 		yield y
# 		y = list(map(lambda v: tuple(np.dot(Rz, v)), y))
# 		y = list(map(lambda v: tuple(np.dot(Rz, v)), y))
# 		yield y
# 		y = list(map(lambda v: tuple(np.dot(Rx, v)), x))
# 		yield y
# 		y = list(map(lambda v: tuple(np.dot(Rx, v)), y))
# 		yield y
# 		y = list(map(lambda v: tuple(np.dot(Rx, v)), y))
# 		yield y
# 		# print("==========================")
# 		if i < 4:
# 			x = list(map(lambda v: tuple(np.dot(Ry, v)), x))
#
#
# # I = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
# # for rot in cloud_rotations([I]):
# #     r = rot[0]
# #     print(f"{r[0]}\n{r[1]}\n{r[2]}\n")
#
#
# with open("input.txt") as f:
# 	scanner_data = [
# 		[tuple(map(int, l.split(","))) for l in block.splitlines()[1:]]
# 		for block in f.read().split("\n\n")
# 	]
#
#
# matched = [scanner_data[0]]
# scanners = [(0, 0, 0)]
# next_search = scanner_data[1:]
# fixed_points = set(scanner_data[0])
#
# i = 0
# while len(matched) < len(scanner_data):
# 	print(f"{len(matched):3} clouds matched so far", end="", flush=True)
# 	reference = matched[i]
# 	search_count = 0
# 	to_search = next_search
# 	next_search = []
# 	for search_cloud in to_search:
# 		found_match = False
# 		print(".", end="", flush=True)
# 		for anchor_point in reference:
# 			for transformed_cloud in cloud_rotations(search_cloud):
# 				for target_point in transformed_cloud:
# 					delta = np.subtract(target_point, anchor_point)
# 					moved_cloud = [
# 						tuple(np.subtract(v, delta)) for v in transformed_cloud
# 					]
# 					overlap = set.intersection(set(moved_cloud), set(reference))
# 					if len(overlap) == 12:
# 						matched.append(moved_cloud)
# 						scanners.append((-delta[0], -delta[1], -delta[2]))
# 						fixed_points |= set(moved_cloud)
# 						found_match = True
# 						break
# 				if found_match:
# 					break
# 			if found_match:
# 				break
# 		if not found_match:
# 			next_search.append(search_cloud)
# 		search_count += 1
# 	i += 1
# 	print()
#
# print(f"Part 1: {len(fixed_points)}")
#
#
# max_dist = 0
# for p, q in permutations(scanners, 2):
# 	d = abs(p[0] - q[0]) + abs(p[1] - q[1]) + abs(p[2] - q[2])
# 	if d > max_dist:
# 		max_dist = d
# print(f"Part 2: {max_dist}")

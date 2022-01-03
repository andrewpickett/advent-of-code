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

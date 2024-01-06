from aoc_utils import run_with_timer, Grid, Point
import hashlib

data = open("input.txt").readline().strip()

movements = {
	"U": (0, -1),
	"D": (0, 1),
	"L": (-1, 0),
	"R": (1, 0)
}


def traverse(curr_pos, passcode, path):
	open_doors = "bcdef"
	h = hashlib.md5((passcode + path).encode()).hexdigest()[:4]
	doors = ""
	if h[0] in open_doors and curr_pos[1] > 0:
		doors += "U"
	if h[1] in open_doors and curr_pos[1] < 3:
		doors += "D"
	if h[2] in open_doors and curr_pos[0] > 0:
		doors += "L"
	if h[3] in open_doors and curr_pos[0] < 3:
		doors += "R"
	return doors


def get_paths(passcode, curr_pos, path, valid_paths):
	open_doors = traverse(curr_pos, passcode, path)

	if len(open_doors) == 0:
		return

	for x in open_doors:
		next_pos = (curr_pos[0] + movements[x][0], curr_pos[1] + movements[x][1])
		if next_pos == (3, 3):
			valid_paths.append(path + x)
			return

		get_paths(passcode, next_pos, path + x, valid_paths)


def part_one():
	valid_paths = []
	get_paths(data, (0, 0), "", valid_paths)
	min_path = ""
	for x in valid_paths:
		if min_path == "" or len(x) < len(min_path):
			min_path = x
	return min_path


def part_two():
	passcode = "ihgpwlah"
	curr_pos = (0, 0)
	valid_paths = []
	get_paths(passcode, curr_pos, "", valid_paths)
	max_path = ""
	for x in valid_paths:
		if max_path == "" or len(x) >= len(max_path):
			max_path = x
	return max_path


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import DIRS
import hashlib


def get_data(filename):
	return open(filename).readline().strip()


def traverse(curr_pos, passcode, path):
	open_doors = "bcdef"
	h = hashlib.md5((passcode + path).encode()).hexdigest()[:4]
	doors = ""
	if h[0] in open_doors and curr_pos[0] > 0:
		doors += "U"
	if h[1] in open_doors and curr_pos[0] < 3:
		doors += "D"
	if h[2] in open_doors and curr_pos[1] > 0:
		doors += "L"
	if h[3] in open_doors and curr_pos[1] < 3:
		doors += "R"
	return doors


def bfs(start, end, path, passcode):
	valid_paths = []
	a = (start, path)
	q = [a]
	while len(q) > 0:
		p = q.pop(0)
		if p[0] == end:
			valid_paths.append(p[1])
		else:
			open_doors = traverse(p[0], passcode, p[1])
			for x in open_doors:
				next_pos = (p[0][0] + DIRS[x][0], p[0][1] + DIRS[x][1])
				a = (next_pos, p[1] + x)
				q.append(a)
	return valid_paths


def part_one(d):
	valid_paths = bfs((0, 0), (3, 3), "", d)
	min_path = ""
	for x in valid_paths:
		if min_path == "" or len(x) < len(min_path):
			min_path = x
	return min_path


def part_two(d):
	return max(map(lambda x: len(x), bfs((0, 0), (3, 3), "", d)))


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	all_data = {"starts": []}
	all_pts = [tuple(map(int, x.strip().split("/"))) for x in open(filename).readlines()]
	for x in all_pts:
		if 0 in x:
			all_data["starts"].append(x)
	all_data["points"] = all_pts
	return all_data


def part_one(d):
	return max(calc_weight(x) for x in get_all_paths(d))


def part_two(d):
	all_paths = get_all_paths(d)
	longest = []
	longest_len = 0
	for x in all_paths:
		if len(x) > longest_len:
			longest.clear()
			longest_len = len(x)
		if len(x) >= longest_len:
			longest.append(x)
	return max(calc_weight(x) for x in longest)


def get_all_paths(d):
	all_paths = []
	for x in d["starts"]:
		remaining_points = d["points"].copy()
		remaining_points.remove(x)
		find_path([], x, 0, remaining_points, all_paths)
	return all_paths


def find_path(curr_path, curr_point, last_in, remaining_points, all_paths):
	out_coord = curr_point[0] if curr_point[1] == last_in else curr_point[1]
	next_pts = get_next_available_points(out_coord, remaining_points)
	curr_path.append(curr_point)
	if not next_pts:
		all_paths.append(curr_path)
	else:
		for x in next_pts:
			r = remaining_points.copy()
			r.remove(x)
			find_path(curr_path.copy(), x, out_coord, r, all_paths)
	return curr_path


def get_next_available_points(out_coord, remaining_points):
	available = []
	for x in remaining_points:
		if out_coord in x:
			available.append(x)
	return available


def calc_weight(path):
	return sum(x[0] + x[1] for x in path)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

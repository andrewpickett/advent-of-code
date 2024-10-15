from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	ret_val = []
	for line in [x.strip() for x in open(filename).readlines()]:
		ret_val.append({x[0]: tuple([int(y) for y in x[3:-1].split(",")]) for x in line.split(", ")})
	return ret_val


def part_one(d):
	m = float("inf")
	mi = 0
	for i, x in enumerate(d):
		total_acceleration = abs(x["a"][0]) + abs(x["a"][1]) + abs(x["a"][2])
		if total_acceleration < m:
			m = total_acceleration
			mi = i
	return mi


def part_two(d):
	iterations = 1
	points = [x for x in d]
	while iterations < 40:
		positions = set()
		new_points = []
		points_to_remove = []
		for i, x in enumerate(points):
			x["v"] = tuple(map(sum, zip(x["v"], x["a"])))
			x["p"] = tuple(map(sum, zip(x["p"], x["v"])))
			if x["p"] in positions:
				points_to_remove.append(x["p"])
			else:
				positions.add(x["p"])
				new_points.append(x)
		points = [x for x in new_points if x["p"] not in points_to_remove]
		iterations += 1
	return len(points)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

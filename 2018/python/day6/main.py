from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	ret_val = {
		"d": 10000,
		"a": [tuple(map(int, x.strip().split(", "))) for x in open(filename).readlines()],
		"r": {
			"x": (float("inf"), 0),
			"y": (float("inf"), 0)
		}
	}
	for pt in ret_val["a"]:
		if pt[0] < ret_val["r"]["x"][0]:
			ret_val["r"]["x"] = (pt[0], ret_val["r"]["x"][1])
		elif pt[0] > ret_val["r"]["x"][1]:
			ret_val["r"]["x"] = (ret_val["r"]["x"][0], pt[0])

		if pt[1] < ret_val["r"]["y"][0]:
			ret_val["r"]["y"] = (pt[1], ret_val["r"]["y"][1])
		elif pt[1] > ret_val["r"]["y"][1]:
			ret_val["r"]["y"] = (ret_val["r"]["y"][0], pt[1])
	return ret_val


def part_one(d):
	distances = {}
	infinite = []
	for x in range(d["r"]["x"][0], d["r"]["x"][1] + 1):
		for y in range(d["r"]["y"][0], d["r"]["y"][1] + 1):
			closest = (0, 0)
			closest_dist = float("inf")
			for z in d["a"]:
				dist = abs(z[0]-x) + abs(z[1]-y)
				if dist < closest_dist:
					closest = z
					closest_dist = dist
				elif dist == closest_dist:
					closest = None
			if x == d["r"]["x"][0] or x == d["r"]["x"][1] or y == d["r"]["y"][0] or y == d["r"]["y"][1]:
				infinite.append(closest)
			distances[(x, y)] = closest
	counts = {x: list(distances.values()).count(x) for x in set(distances.values()) if x is not None and x not in infinite}
	return max(counts.values())


def part_two(d):
	return sum(1 for x in range(d["r"]["x"][0], d["r"]["x"][1] + 1) for y in range(d["r"]["y"][0], d["r"]["y"][1] + 1) if sum(abs(z[0]-x) + abs(z[1]-y) for z in d["a"]) < d["d"])


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

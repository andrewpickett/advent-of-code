from utils.timers import run_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


dirs = {
	0: (-1, 0),
	1: (0, 1),
	2: (1, 0),
	3: (0, -1)
}


def shine_light(d, start):
	lights = [start]
	visited_points = set()
	while len(lights) > 0:
		lights_to_remove = []
		lights_to_add = []
		for light in lights:
			curr_point = light["p"]
			next_str = str(curr_point) + "-" + str(light["d"])
			if next_str not in visited_points and 0 <= curr_point[0] < len(d) and 0 <= curr_point[1] < len(d[0]):
				visited_points.add(next_str)
				if d[curr_point[0]][curr_point[1]] == "-" and light["d"] in [0, 2]:
					lights_to_add.append({"d": 3, "p": (light["p"][0], light["p"][1]-1)})
					light["d"] = 1
				elif d[curr_point[0]][curr_point[1]] == "|" and light["d"] in [1, 3]:
					lights_to_add.append({"d": 0, "p": (light["p"][0]-1, light["p"][1])})
					light["d"] = 2
				elif d[curr_point[0]][curr_point[1]] == "\\":
					light["d"] = (light["d"] + (1 if light["d"] in [1, 3] else -1)) % len(dirs)
				elif d[curr_point[0]][curr_point[1]] == "/":
					light["d"] = (light["d"] + (1 if light["d"] in [0, 2] else -1)) % len(dirs)
				light["p"] = (light["p"][0]+dirs[light["d"]][0], light["p"][1]+dirs[light["d"]][1])
			else:
				lights_to_remove.append(light)

		lights.extend(lights_to_add)
		for light in lights_to_remove:
			lights.remove(light)
	return len(set(map(lambda x: x[:x.find("-")], list(visited_points))))


def part_one(d):
	return shine_light(d, {"d": 1, "p": (0, 0)})


def part_two(d):
	max_energy = 0
	for r, row in enumerate(d):
		max_energy = max(max_energy, shine_light(d, {"d": 1, "p": (r, 0)}), shine_light(d, {"d": 3, "p": (r, len(row)-1)}))
		if r == 0 or r == len(d) - 1:
			for c, col in enumerate(row):
				max_energy = max(max_energy, shine_light(d, {"d": 2 if r == 0 else 0, "p": (r, c)}))
	return max_energy


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

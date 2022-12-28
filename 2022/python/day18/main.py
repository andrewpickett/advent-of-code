from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def set_all_exterior_sides(d):
	for i, x in enumerate(d):
		for y in d[i+1:]:
			if sum(1 for k in range(len(x["coords"])) if y["coords"][k] == x["coords"][k]) == 2 and abs(sum(y["coords"]) - sum(x["coords"])) == 1:
				x["sides"] -= 1
				y["sides"] -= 1


def part_one():
	cubes = [{"sides": 6, "coords": [int(y) for y in x.strip().split(",")]} for x in data]
	set_all_exterior_sides(cubes)
	return sum(x["sides"] for x in cubes)


def part_two():
	cubes = set(tuple(int(y) for y in x.strip().split(",")) for x in data)
	out_flow_count = 0
	out_points = set()
	in_points = set()
	for p in cubes:
		out_flow_count += 1 if floods_out((p[0]+1, p[1], p[2]), out_points, in_points, cubes) else 0
		out_flow_count += 1 if floods_out((p[0]-1, p[1], p[2]), out_points, in_points, cubes) else 0
		out_flow_count += 1 if floods_out((p[0], p[1]+1, p[2]), out_points, in_points, cubes) else 0
		out_flow_count += 1 if floods_out((p[0], p[1]-1, p[2]), out_points, in_points, cubes) else 0
		out_flow_count += 1 if floods_out((p[0], p[1], p[2]+1), out_points, in_points, cubes) else 0
		out_flow_count += 1 if floods_out((p[0], p[1], p[2]-1), out_points, in_points, cubes) else 0
	return out_flow_count


def floods_out(p, out_points, in_points, all_points):
	if p in out_points:
		return True
	if p in in_points:
		return False
	visited_points = set()
	q = [p]
	while len(q) > 0:
		n = q.pop(0)
		if n in all_points or n in visited_points:
			continue
		visited_points.add(n)
		if len(visited_points) > 5000:
			for x in visited_points:
				out_points.add(x)
			return True
		q.extend([(n[0]+1, n[1], n[2]), (n[0]-1, n[1], n[2]), (n[0], n[1]+1, n[2]), (n[0], n[1]-1, n[2]), (n[0], n[1], n[2]+1), (n[0], n[1], n[2]-1)])
	for x in visited_points:
		in_points.add(x)
	return False


if __name__ == '__main__':
	run_with_timer(part_one)  # 3576 -- took 2138 ms
	run_with_timer(part_two)  # 2066 -- took 234 ms

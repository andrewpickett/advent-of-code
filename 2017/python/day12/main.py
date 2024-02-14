from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	ret_map = {}
	for line in lines:
		parts = line.split(" <-> ")
		dests = parts[1].split(", ")
		if parts[0] not in ret_map:
			ret_map[parts[0]] = set()
		for x in dests:
			ret_map[parts[0]].add(x)

	for x in ret_map:
		q = set(ret_map[x])
		visited = set()
		while len(q) > 0:
			next_elem = q.pop()
			if next_elem not in visited:
				visited.add(next_elem)
				q.update(ret_map[next_elem])
		ret_map[x] = visited
	return ret_map


def part_one(d):
	return len(d["0"])


def part_two(d):
	groups = set()
	for x in d:
		groups.add(''.join(list(sorted(d[x]))))
	return len(groups)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

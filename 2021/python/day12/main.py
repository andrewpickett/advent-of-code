from aoc_utils import run_with_timer
import copy

data = [x.strip().split("-") for x in open("input.txt").readlines()]


def build_map():
	m = {}
	for x in data:
		if x[0] not in m:
			m[x[0]] = []
		m[x[0]].append(x[1])
		if x[1] != 'end':
			if x[1] not in m:
				m[x[1]] = []
			if x[0] != 'start':
				m[x[1]].append(x[0])
	return m


def count_ways_to_node(m, current_path, full_paths, second_visit):
	last_node = current_path[-1]
	if last_node == 'end':
		full_paths.add('-'.join(current_path))
		return
	if last_node.islower():
		if not second_visit:
			if sum(1 for x in current_path if x == last_node) == 2 and last_node != 'start':
				second_visit = True
				for x in m:
					m[x] = list(filter(lambda y: y.isupper() or (y.islower() and y not in current_path), m[x]))
		else:
			for x in m:
				if last_node in m[x]:
					m[x].remove(last_node)
	if len(m[last_node]) > 0:
		for x in m[last_node]:
			next_path = current_path.copy()
			next_path.append(x)
			count_ways_to_node(copy.deepcopy(m), next_path, full_paths, second_visit)


def part_one():
	m = build_map()
	full_paths = set()
	count_ways_to_node(copy.deepcopy(m), ['start'], full_paths, True)
	return len(full_paths)


def part_two():
	m = build_map()
	full_paths = set()
	count_ways_to_node(copy.deepcopy(m), ['start'], full_paths, False)
	return len(full_paths)


if __name__ == '__main__':
	run_with_timer(part_one)  # 5252 -- took 433 ms
	run_with_timer(part_two)  # 147784 -- took 12627 ms

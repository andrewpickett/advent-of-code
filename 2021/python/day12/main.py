from aoc_utils import run_with_timer
import copy

data = [x.strip().split("-") for x in open("sample.txt").readlines()]


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


def count_ways_to_node(m, current_path, full_paths):
	last_node = current_path[-1]
	if last_node == 'end':
		full_paths.add('-'.join(current_path))
		return
	if last_node.islower():
		for x in m:
			if last_node in m[x]:
				m[x].remove(last_node)
	if len(m[last_node]) > 0:
		for x in m[last_node]:
			next_path = current_path.copy()
			next_path.append(x)
			count_ways_to_node(copy.deepcopy(m), next_path, full_paths)


def count_ways_to_node2(m, current_path, full_paths):
	# print(m, current_path, full_paths)
	last_node = current_path[-1]
	if last_node == 'end':
		full_paths.add('-'.join(current_path))
		return 1
	if last_node.islower():
		if sum(1 for x in current_path if x == last_node) == 2 and last_node != 'start':
			print("SECOND VISIT OF", last_node)
			for x in m:
				m[x] = list(filter(lambda y: y.isupper() or (y.islower() and y not in current_path), m[x]))
		# for x in m:
		# 	if node in m[x]:
		# 		m[x].remove(node)
	if len(m[last_node]) > 0:
		for x in m[last_node]:
			next_path = current_path.copy()
			next_path.append(x)
			count_ways_to_node2(copy.deepcopy(m), next_path, full_paths)


def part_one():
	m = build_map()
	full_paths = set()
	count_ways_to_node(copy.deepcopy(m), ['start'], full_paths)
	for x in sorted(full_paths):
		print(x)
	return len(full_paths)


def part_two():
	m = build_map()
	full_paths = set()
	# print(m)
	count_ways_to_node2(copy.deepcopy(m), ['start'], full_paths)
	for x in sorted(full_paths):
		print(x)
	return len(full_paths)


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

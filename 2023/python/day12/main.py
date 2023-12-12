from utils.timers import run_with_timer


def get_data(filename):
	return [x.strip().split() for x in open(filename).readlines()]


def count_spring_groups(spring_map, groupings, pos, group, m):
	m_key = str(pos) + "-" + str(group)
	if group == len(groupings):
		if pos < len(spring_map) and "#" in spring_map[pos:]:
			return 0
		return 1

	if pos >= len(spring_map):
		return 0

	if m_key in m:
		return m[m_key]

	ret_val = None
	n = groupings[group]
	if spring_map[pos] == ".":
		ret_val = count_spring_groups(spring_map, groupings, pos + 1, group, m)
	elif spring_map[pos] == "#":
		if "." not in spring_map[pos:pos + n] and spring_map[pos + n] != "#":
			ret_val = count_spring_groups(spring_map, groupings, pos + n + 1, group + 1, m)
		else:
			ret_val = 0
	elif spring_map[pos] == "?":
		if "." not in spring_map[pos:pos + n] and spring_map[pos + n] != "#":
			ret_val = count_spring_groups(spring_map, groupings, pos + 1, group, m) + count_spring_groups(spring_map, groupings, pos + n + 1, group + 1, m)
		else:
			ret_val = count_spring_groups(spring_map, groupings, pos + 1, group, m)

	m[m_key] = ret_val
	return ret_val


def part_one(d):
	return sum(count_spring_groups(x[0] + ".", [int(y) for y in x[1].split(",")], 0, 0, {}) for x in d)


def part_two(d):
	return sum(count_spring_groups("?".join([x[0]]*5) + ".", [int(y) for y in x[1].split(",")]*5, 0, 0, {}) for x in d)


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

from utils.timers import run_with_timer


def get_data(filename):
	lines = [x.strip().split(": ") for x in open(filename).readlines()]
	ret_map = {}
	for line in lines:
		if line[0] not in ret_map:
			ret_map[line[0]] = []
		for x in [y.strip() for y in line[1].split()]:
			ret_map[line[0]].append(x)
			if x not in ret_map:
				ret_map[x] = []
			ret_map[x].append(line[0])
	return ret_map

# hfx/pzl, the wire between bvb/cmg, and the wire between nvd/jqt


def part_one(d):
	print(d)
	return True


def part_two(d):
	return False


if __name__ == "__main__":
	data = get_data("sample.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

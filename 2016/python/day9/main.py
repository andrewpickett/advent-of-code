from aoc_utils import run_with_timer

data = open("input.txt").readline().strip()


def decompress(s, recurse, depth):
	sidx = s.find("(")
	eidx = s.find(")")
	if sidx < 0 or (not recurse and depth > 0):
		return len(s)

	prefix = s[0:sidx]
	parts = s[sidx + 1:eidx].split("x")
	next = s[eidx + 1:eidx + 1 + int(parts[0])]
	suffix = s[eidx+1+int(parts[0]):]
	return len(prefix) + int(parts[1]) * decompress(next, recurse, depth+1) + decompress(suffix, recurse, depth)


def part_one():
	return decompress(data, False, 0)


def part_two():
	return decompress(data, True, 0)


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return open(filename).readline().strip()


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


def part_one(d):
	return decompress(d, False, 0)


def part_two(d):
	return decompress(d, True, 0)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

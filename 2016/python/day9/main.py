from aoc_utils import run_with_timer

data = open("input.txt").readline().strip()


def part_one():
	return decompress(data, False)
	# new_str = ""
	# i = 0
	# while i < len(data):
	# 	if data[i] == "(":
	# 		close_idx = data[i:].find(")")
	# 		parts = data[i+1:i+close_idx].split("x")
	# 		new_str += data[i+close_idx+1:i+close_idx+1+int(parts[0])] * int(parts[1])
	# 		i += 1+close_idx+int(parts[0])
	# 	else:
	# 		new_str += data[i]
	# 		i += 1
	# return new_str


def decompress(s, recurse):
	if s.find("(") < 0:
		return len(s)

	prefix = s[0:s.find("(")]
	parts = s[s.find("(")+1:s.find(")")].split("x")

	next = s[s.find(")")+1:s.find(")")+1+int(parts[0])]

	suffix = s[s.find(")")+1+int(parts[0]):]

	if recurse:
		return len(prefix) + int(parts[1]) * decompress(next, True) + decompress(suffix, True)
	else:
		return len(prefix + int(parts[1])) * len(next) + decompress(suffix, False)


def part_two():
	return decompress(data, True)


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

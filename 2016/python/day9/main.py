from aoc_utils import run_with_timer

data = open("input.txt").readline().strip()


def part_one():
	new_str = ""
	i = 0
	while i < len(data):
		if data[i] == "(":
			close_idx = data[i:].find(")")
			parts = data[i+1:i+close_idx].split("x")
			new_str += data[i+close_idx+1:i+close_idx+1+int(parts[0])] * int(parts[1])
			i += 1+close_idx+int(parts[0])
		else:
			new_str += data[i]
			i += 1
	return new_str


def decompress(s):
	if s.find("(") < 0:
		return len(s)

	total_len = 0

	i = 0
	while i < len(s) or s.find("(") < 0:
		if data[i] == "(":
			close_idx = data[i:].find(")")
			parts = data[i+1:i+close_idx].split("x")

			new_str += data[i+close_idx+1:i+close_idx+1+int(parts[0])] * int(parts[1])
			i += 1+close_idx+int(parts[0])
		else:
			new_str += data[i]
			i += 1
	return total_len



def part_two():
	new_str = data
	while new_str.find("(") >= 0:
		new_str = decompress(new_str)
	return len(new_str)


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

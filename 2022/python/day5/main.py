from aoc_utils import run_with_timer

data = [x for x in open("input.txt").readlines()]


def parse_input():
	s = []
	m = []
	in_moves = False
	for x in data:
		if x.strip() == "" or x.strip().startswith("1"):
			in_moves = True
		if in_moves and x.strip() != "" and not x.strip().startswith("1"):
			m.append(x)
		else:
			for y in range(0, len(x), 4):
				if y//4 >= len(s):
					s.append([])
				if x[y] == "[":
					s[y//4].append(x[y+1])
	for x in s:
		x.reverse()
	return s, m


def move_crates(f):
	s, m = parse_input()
	for x in m:
		parts = x.split(" ")
		f(s, int(parts[3])-1, int(parts[5])-1, int(parts[1]))
	ret_str = ""
	for x in s:
		ret_str += x.pop()
	return ret_str


def single_move(s, orig, dest, amt):
	for y in range(amt):
		s[dest].append(s[orig].pop())


def multiple_move(s, orig, dest, amt):
	s[dest].extend(s[orig][-amt:])
	for y in range(amt):
		s[orig].pop()


def part_one():
	return move_crates(single_move)


def part_two():
	return move_crates(multiple_move)


if __name__ == '__main__':
	run_with_timer(part_one)  # RTGWZTHLD -- took 5 ms
	run_with_timer(part_two)  # STHGRZZFR -- took 5 ms

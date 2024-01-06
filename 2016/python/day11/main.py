from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def parse_input():
	floors = [[], [], [], []]
	for i, x in enumerate(data):
		if "nothing relevant" not in x:
			parts = x.split(" ")
			for j, y in enumerate(parts):
				if y == "a":
					part = (parts[j+1][0:3] + " " + parts[j+2][0:3]).upper()
					if part.endswith(".") or part.endswith(","):
						part = part[:-1]
					floors[i].append(part)
	return floors


def part_one():
	floors = parse_input()
	print(floors)
	curr_floor = 0
	move_count = 0
	while len(floors[0]) != 0 or len(floors[1]) != 0 or len(floors[2]) != 0:
		move_count += 1
	return move_count


def part_two():
	return


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

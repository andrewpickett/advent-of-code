from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def parse_input(d):
	floors = [[], [], [], []]
	for i, x in enumerate(d):
		if "nothing relevant" not in x:
			parts = x.split(" ")
			for j, y in enumerate(parts):
				if y == "a":
					part = (parts[j+1][0:3] + " " + parts[j+2][0:3]).upper()
					if part.endswith(".") or part.endswith(","):
						part = part[:-1]
					floors[i].append(part)
	return floors


def part_one(d):
	floors = parse_input(d)
	print(floors)
	curr_floor = 0
	move_count = 0
	while len(floors[0]) != 0 or len(floors[1]) != 0 or len(floors[2]) != 0:
		move_count += 1
	return move_count


def part_two(d):
	return


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

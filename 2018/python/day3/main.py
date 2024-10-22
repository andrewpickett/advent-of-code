from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def part_one(d):
	fabric = populate_fabric(d)
	return sum(i.count(-1) for i in fabric)


def part_two(d):
	fabric = populate_fabric(d)
	for line in d:
		parts = line.split(' ')
		claim, left, top, width, height = parse_line_data(parts)

		good_claim = True
		for i in range(left, left + width):
			for j in range(top, top + height):
				if fabric[i][j] == -1:
					good_claim = False
					break
			if not good_claim:
				break
		if good_claim:
			return claim


def populate_fabric(d):
	fabric = [[0] * 1000 for _ in range(1000)]
	for line in d:
		parts = line.split(' ')
		claim, left, top, width, height = parse_line_data(parts)

		for i in range(left, left + width):
			for j in range(top, top + height):
				if fabric[i][j] == 0:
					fabric[i][j] = claim
				else:
					fabric[i][j] = -1
	return fabric


def parse_line_data(parts):
	return int(parts[0][1:]), int(parts[2].split(',')[0]), int(parts[2].split(',')[1][:-1]), int(parts[3].split('x')[0]), int(parts[3].split('x')[1])


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

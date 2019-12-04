data = [x.strip() for x in open("input.txt").readlines()]


def part_one():
	fabric = populate_fabric()
	return sum(i.count(-1) for i in fabric)


def part_two():
	fabric = populate_fabric()
	for line in data:
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


def populate_fabric():
	fabric = [[0] * 1000 for i in range(1000)]
	for line in data:
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


if __name__ == '__main__':
	print(part_one())
	print(part_two())

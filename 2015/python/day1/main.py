data = [x for x in open('input.txt').readline()]


def part_one():
	return data.count('(') - data.count(')')


def part_two():
	floor = 0
	for i, direction in enumerate(data):
		floor += 1 if direction == '(' else -1
		if floor < 0:
			return i + 1
	return 0


if __name__ == '__main__':
	print(part_one())  # 138
	print(part_two())  # 1771

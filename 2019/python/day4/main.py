data = [int(x) for x in open("input.txt").readline().split('-')]


def part_one():
	return sum(check_number_for_validity(str(i)) for i in range(data[0], data[1]))


def part_two():
	return sum(check_number_for_validity(str(i), True) for i in range(data[0], data[1]))


def check_number_for_validity(num, additional_check=False):
	consecutive = False
	increasing = True
	for j in range(len(num) - 1):
		if int(num[j + 1]) < int(num[j]):
			increasing = False
			break
		if int(num[j + 1]) == int(num[j]) and (not additional_check or (additional_check and num.count(num[j]) == 2)):
			consecutive = True
	return 1 if consecutive and increasing else 0


if __name__ == '__main__':
	print(part_one())  # 2081
	print(part_two())  # 1411

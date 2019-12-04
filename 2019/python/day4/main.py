data = [int(x) for x in open("input.txt").readline().split('-')]


def part_one():
	counter = 0
	for i in range(data[0], data[1]):
		if check_number_for_validity(str(i)):
			counter += 1
	return counter


def part_two():
	counter = 0
	for i in range(data[0], data[1]):
		if check_number_for_validity(str(i), True):
			counter += 1
	return counter


def check_number_for_validity(num, additional_check=False):
	consecutive = False
	increasing = True
	for j in range(len(num) - 1):
		if int(num[j + 1]) < int(num[j]):
			increasing = False
			break
		if int(num[j + 1]) == int(num[j]) and (not additional_check or (additional_check and num.count(num[j]) == 2)):
			consecutive = True
	return consecutive and increasing


if __name__ == '__main__':
	print(part_one())  # 2081
	print(part_two())  # 1411

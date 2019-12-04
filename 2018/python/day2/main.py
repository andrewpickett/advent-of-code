data = [x.strip() for x in open("input.txt").readlines()]


def part_one():
	total_twos = 0
	total_threes = 0
	for line in data:
		twos = 0
		threes = 0
		for letter in line:
			if line.count(letter) == 2:
				twos = 1
			elif line.count(letter) == 3:
				threes = 1
		total_twos += twos
		total_threes += threes
	return total_twos * total_threes


def part_two():
	sorted_data = sorted(data)
	for i in range(len(sorted_data) - 1):
		for j in range(i + 1, len(sorted_data)):
			diff_count = 0
			diff_idx = -1
			for k in range(len(sorted_data[i])):
				if sorted_data[i][k] != sorted_data[j][k]:
					diff_count += 1
					diff_idx = k
				if diff_count > 1:
					break
			if diff_count == 1:
				return sorted_data[i][0:diff_idx] + sorted_data[i][diff_idx + 1:]


if __name__ == '__main__':
	print(part_one())
	print(part_two())

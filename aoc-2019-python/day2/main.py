import ir


def part_one():
	nums = ir.lines[0].split(',')
	for i in range(len(nums)):
		nums[i] = int(nums[i])

	nums[1] = 12
	nums[2] = 2

	return calc_answer(nums)


def part_two():
	nums = ir.lines[0].split(',')
	test_nums = []
	for i in range(len(nums)):
		nums[i] = int(nums[i])
		test_nums.append(nums[i])

	for i in range(100):
		for j in range(100):
			for k in range(len(nums)):
				test_nums[k] = nums[k]
			test_nums[1] = i
			test_nums[2] = j

			if calc_answer(test_nums) == 19690720:
				return (test_nums[1] * 100) + test_nums[2]
	return


def calc_answer(test_arr):
	i = 0
	while True:
		if test_arr[i] == 1:
			test_arr[test_arr[i+3]] = test_arr[test_arr[i+1]] + test_arr[test_arr[i+2]]
		elif test_arr[i] == 2:
			test_arr[test_arr[i+3]] = test_arr[test_arr[i+1]] * test_arr[test_arr[i+2]]
		elif test_arr[i] == 99:
			break
		i += 4
	return test_arr[0]


if __name__ == '__main__':
	ir.read_lines('./input.txt')
	print(part_one())  # 3716293
	print(part_two())  # 6429

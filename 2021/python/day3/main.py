from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def part_one():
	gamma_rate = ''
	epsilon_rate = ''
	for i in range(len(data[0])):
		num_ones = sum(1 for d in data if d[i] == '1')
		gamma_rate += '1' if num_ones >= len(data) / 2 else '0'
		epsilon_rate += '0' if num_ones >= len(data) / 2 else '1'

	return int(gamma_rate, 2) * int(epsilon_rate, 2)


def calculate_rating(bit_check):
	rating_val = ''
	for i in range(len(data[0])):
		rems = list(filter(lambda x: x.startswith(rating_val), data))
		if len(rems) == 1:
			return rems[0]
		bit_count = sum(1 for d in rems if d[i] == bit_check)
		rating_val += '1' if bit_count > len(rems) / 2 or (bit_check == '1' and bit_count == len(rems) / 2) else '0'
	return rating_val


def part_two():
	return int(calculate_rating('1'), 2) * int(calculate_rating('0'), 2)


if __name__ == '__main__':
	run_with_timer(part_one)  # 2595824 -- took 0 ms
	run_with_timer(part_two)  # 2135254 -- took 2 ms

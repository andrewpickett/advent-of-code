from aoc_utils import run_with_timer

data = [int(x) for x in open('input.txt').readline().strip()]


def part_one():
	num_phases = 100
	input_signal = list(data)
	for i in range(num_phases):
		input_signal = [calculate_output_value(input_signal, i) for i in range(len(input_signal))]
	return int(''.join(str(x) for x in input_signal[0:8]))


def part_two():
	num_phases = 100
	input_signal = list(data)
	offset = int(''.join(str(x) for x in input_signal[0:7]))
	input_signal = list(input_signal * 10000)
	result = [0] * len(input_signal)
	for _ in range(num_phases):
		result[-1] = input_signal[-1]
		for j in range(len(input_signal) - 2, len(input_signal) // 2, -1):
			result[j] = (input_signal[j] + result[j + 1]) % 10
		input_signal = list(result)
		result = [0] * len(input_signal)
	return int(''.join(str(x) for x in input_signal[offset:offset + 8]))


def calculate_output_value(input_signal, row_num):
	if row_num >= len(input_signal) // 2:
		return abs(sum(int(x) for x in input_signal[row_num - len(input_signal):])) % 10
	else:
		i = row_num
		total = 0
		multiplier = 1
		while i < len(input_signal):
			for j in range(row_num + 1):
				if i + j < len(input_signal):
					total += input_signal[i + j] * multiplier
				else:
					break
			i += 2 * (row_num + 1)
			multiplier *= -1
		return abs(total) % 10


if __name__ == '__main__':
	run_with_timer(part_one)  # 58100105
	run_with_timer(part_two)  # 41781287

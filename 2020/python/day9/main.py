from aoc_utils import run_with_timer

data = [int(x.strip()) for x in open("input.txt").readlines()]


def find_invalid_number(preamble_len):
	for i in range(preamble_len, len(data)):
		prior_set = data[i-preamble_len:i]

		match_found = None
		for j in range(len(prior_set) - 1):
			for k in range(j, len(prior_set)):
				if prior_set[j] + prior_set[k] == data[i]:
					match_found = (j, k)
		if not match_found:
			return data[i]


def part_one():
	return find_invalid_number(25)


def part_two():
	invalid_num = find_invalid_number(25)

	for i in range(data.index(invalid_num)):
		curr_sum = data[i]
		next_idx = i+1
		while curr_sum < invalid_num:
			curr_sum += data[next_idx]
			next_idx += 1
		if curr_sum == invalid_num:
			return min(data[i:next_idx]) + max(data[i:next_idx])


if __name__ == '__main__':
	run_with_timer(part_one)  # 1038347917 -- took 35 ms
	run_with_timer(part_two)  # 137394018 -- took 47 ms

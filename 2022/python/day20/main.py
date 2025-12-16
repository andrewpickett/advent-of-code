from aoc_utils import run_with_timer

data = [(i, int(x.strip())) for i, x in enumerate(open("input.txt").readlines())]


def decrypt(multiplier=1, repeats=1):
	ref_list = [(i, x*multiplier) for i, x in data]
	new_list = [x for x in ref_list]
	print("Initial")
	for j in range(repeats):
		print(new_list)
		print("running", j)
		for i in range(len(ref_list)):
			next_num = ref_list[i]
			curr_idx = new_list.index((i, next_num[1]))
			tmp = next_num[1] % len(new_list)
			new_idx = curr_idx + (next_num[1] % len(new_list))
			print("new", new_idx)
			# while new_idx > len(new_list):
			# 	new_idx = (new_idx % len(new_list)) + (new_idx // len(new_list))
			# new_idx = len(new_list) - 1 if new_idx == 0 else new_idx
			# new_idx = 0 if new_idx == len(new_list) else new_idx
			new_list.remove(next_num)
			new_list.insert(new_idx, next_num)

	print(new_list)
	idx = [x[1] for x in new_list].index(0)
	return new_list[(idx + 1000) % len(new_list)][1] + new_list[(idx + 2000) % len(new_list)][1] + new_list[(idx + 3000) % len(new_list)][1]


def part_one():
	return decrypt()


def part_two():
	return decrypt(811589153, 10)


if __name__ == '__main__':
	run_with_timer(part_one)  # 15297 -- took 416 ms
	# run_with_timer(part_two)  #
# 4685 incorrect...
# -392 incorrect


# 2897373276210

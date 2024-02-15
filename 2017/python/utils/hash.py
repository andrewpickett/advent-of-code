import functools


def knot_hash(s, knot=None, rounds=64):
	if knot is None:
		knot = [x for x in range(256)]
	return to_hex(dense_hash(sparse_hash(get_ascii_vals(s), knot, rounds)))


def get_ascii_vals(s):
	return [ord(x) for x in s] + [17, 31, 73, 47, 23]


def single_knot_hash(in_val, knot=None, pos=0, skip=0):
	if knot is None:
		knot = [x for x in range(256)]
	curr_nums = knot * 2
	skip_size = skip
	curr_pos = pos

	for x in in_val:
		reversed_section = list(reversed(curr_nums[curr_pos:curr_pos + x]))
		new_nums = curr_nums[:curr_pos] + reversed_section + curr_nums[curr_pos + x:]
		new_nums = new_nums[len(knot):len(knot)+curr_pos] + new_nums[curr_pos:len(knot)]
		curr_pos = (curr_pos + x + skip_size) % len(knot)
		skip_size += 1
		curr_nums = new_nums * 2
	return curr_nums[:len(knot)], curr_pos, skip_size


def sparse_hash(in_val, s, rounds):
	knot = s
	pos = 0
	skip = 0
	for _ in range(rounds):
		knot, pos, skip = single_knot_hash(in_val, knot, pos, skip)
	return knot


def dense_hash(nums):
	d = []
	for i in range(0, len(nums), 16):
		d.append(functools.reduce(lambda a, b: a ^ b, nums[i:i+16]))
	return d


def to_hex(nums):
	return ''.join(map(lambda x: hex(x)[2:].rjust(2, "0"), nums))

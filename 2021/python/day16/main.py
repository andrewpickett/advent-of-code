import math

from aoc_utils import run_with_timer

data = open("input.txt").readline().strip()


def parse_literal(literal_str):
	ret_val = ""
	a = 0
	while literal_str[a*5] == '1':
		ret_val += literal_str[a*5+1:(a+1)*5]
		a += 1
	ret_val += literal_str[a*5+1:(a+1)*5]
	return int(ret_val, 2), literal_str[(a+1)*5:]


def parse_operator(operator_str, v_total):
	length_type_id = operator_str[6]
	literal_vals = []
	if length_type_id == '0':
		sub_len = int(operator_str[7:22], 2)
		rem_str = operator_str[22:22+sub_len]
		while rem_str != '':
			rem_str, v, ls = parse_packet(rem_str)
			v_total += v
			literal_vals.append(ls)
		return operator_str[22+sub_len:], v_total, literal_vals
	else:
		num_subs = int(operator_str[7:18], 2)
		rem_str = operator_str[18:]
		for i in range(num_subs):
			rem_str, v, ls = parse_packet(rem_str)
			v_total += v
			literal_vals.append(ls)
		return rem_str, v_total, literal_vals


def parse_packet(packet_str):
	version = int(packet_str[:3], 2)
	type_id = int(packet_str[3:6], 2)
	if type_id == 4:
		literal_val, rem_str = parse_literal(packet_str[6:])
		return rem_str, version, literal_val
	else:
		rem_str, v_total, literals = parse_operator(packet_str, version)
		if type_id == 0:
			return rem_str, v_total, sum(literals)
		elif type_id == 1:
			return rem_str, v_total, math.prod(literals)
		elif type_id == 2:
			return rem_str, v_total, min(literals)
		elif type_id == 3:
			return rem_str, v_total, max(literals)
		elif type_id == 5:
			return rem_str, v_total, 1 if literals[0] > literals[1] else 0
		elif type_id == 6:
			return rem_str, v_total, 1 if literals[0] < literals[1] else 0
		elif type_id == 7:
			return rem_str, v_total, 1 if literals[0] == literals[1] else 0


def convert_hex_to_bin_str(hex_str):
	return "".join(bin(int(x, 16))[2:].zfill(4) for x in list(hex_str))


def part_one():
	return parse_packet(convert_hex_to_bin_str(data))[1]


def part_two():
	return parse_packet(convert_hex_to_bin_str(data))[2]


if __name__ == '__main__':
	run_with_timer(part_one)  # 852 -- took 1 ms
	run_with_timer(part_two)  # 19348959966392 -- took 0 ms

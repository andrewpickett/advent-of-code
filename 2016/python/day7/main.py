from aoc_utils import run_with_timer
import re

data = [re.split("(\W)", x.strip()) for x in open("input.txt").readlines()]


def find_abbas_in_str(s):
	for x in range(0, len(s)-3):
		if s[x] == s[x+3] and s[x+1] == s[x+2] and s[x] != s[x+1]:
			return str(s[x:x+4])
	return False


def get_net_parts(s):
	parts = {'subnets': [], 'hypernets': []}
	in_hypernet = False
	for y in s:
		if y == '[':
			in_hypernet = True
		elif y == ']':
			in_hypernet = False
		else:
			parts['hypernets' if in_hypernet else 'subnets'].append(y)
	return parts


def part_one():
	total_count = 0
	for x in data:
		in_hypernet = False
		is_valid = False
		for y in x:
			if y == '[':
				in_hypernet = True
			elif y == ']':
				in_hypernet = False
			else:
				found_abba = find_abbas_in_str(y)
				if in_hypernet and found_abba:
					is_valid = False
					break
				is_valid = is_valid or found_abba
		if is_valid:
			total_count += 1
	return total_count


def part_two():
	total_count = 0
	for x in data:
		parts = get_net_parts(x)
		done = False
		for subnet in parts['subnets']:
			for y in range(0, len(subnet)-2):
				if subnet[y] == subnet[y+2] and subnet[y] != subnet[y+1]:
					for hypernet in parts['hypernets']:
						if subnet[y+1] + subnet[y] + subnet[y+1] in hypernet:
							total_count += 1
							done = True
							break
				if done:
					break
			if done:
				break
	return total_count


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

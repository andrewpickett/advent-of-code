from utils.timers import run_with_timer, get_data_with_timer
import re


def get_data(filename):
	return [
		{"subnets": re.split("[\[\]]", x.strip())[::2], "hypernets": re.split("[\[\]]", x.strip())[1::2]}
		for x in open(filename).readlines()
	]


def find_abbas_in_str(s):
	return [str(s[x:x+4]) for x in range(0, len(s)-3) if s[x] == s[x+3] and s[x+1] == s[x+2] and s[x] != s[x+1]]


def part_one(d):
	return sum(1 for x in d if len([y for y in x["subnets"] if find_abbas_in_str(y)]) > 0 and len([y for y in x["hypernets"] if find_abbas_in_str(y)]) == 0)


def part_two(d):
	total_count = 0
	for x in d:
		done = False
		for subnet in x['subnets']:
			for y in range(0, len(subnet)-2):
				if subnet[y] == subnet[y+2] and subnet[y] != subnet[y+1]:
					for hypernet in x['hypernets']:
						if subnet[y+1] + subnet[y] + subnet[y+1] in hypernet:
							total_count += 1
							done = True
							break
				if done:
					break
			if done:
				break
	return total_count


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

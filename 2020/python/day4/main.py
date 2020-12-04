import re
from aoc_utils import run_with_timer

data = open("input.txt").read().split('\n\n')

date_match = re.compile('^\d{4}$')
hgt_match = re.compile('^\d+(cm|in)$')
pid_match = re.compile('^\d{9}$')
hex_match = re.compile('^[#][0-9a-f]{6}$')


def validate_presence(pport):
	return all(x in pport for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])


def validate_data(pport):
	fields = [x for x in pport.split() if x[0:3] != 'cid']
	fields.sort()
	for x in fields:
		y = x.split(':')
		if y[0] == 'byr' and (not date_match.match(y[1]) or not int(y[1]) in range(1920, 2003)):
			return False
		elif y[0] == 'iyr' and (not date_match.match(y[1]) or not int(y[1]) in range(2010, 2021)):
			return False
		elif y[0] == 'eyr' and (not date_match.match(y[1]) or not int(y[1]) in range(2020, 2031)):
			return False
		elif y[0] == 'hgt':
			if hgt_match.match(y[1]):
				hgt = y[1][0:-2]
				if ('cm' in y[1] and int(hgt) not in range(150, 194)) or ('in' in y[1] and int(hgt) not in range(59, 77)):
					return False
			else:
				return False
		elif y[0] == 'hcl' and not hex_match.match(y[1]):
			return False
		elif y[0] == 'ecl' and y[1] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
			return False
		elif y[0] == 'pid' and not pid_match.match(y[1]):
			return False
	return True


def part_one():
	return sum(1 for x in data if validate_presence(x))


def part_two():
	return sum(1 for x in data if validate_presence(x) and validate_data(x))


if __name__ == '__main__':
	run_with_timer(part_one)  # 170 -- took 0 ms
	run_with_timer(part_two)  # 103 -- took 1 ms

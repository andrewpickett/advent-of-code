import re
from aoc_utils import run_with_timer

data = open("input.txt").read().split('\n\n')

date_match = re.compile('^\d{4}$')
hgt_match = re.compile('^\d+(cm|in)$')
pid_match = re.compile('^\d{9}$')
hex_match = re.compile('^[#][\da-f]{6}$')


def validate_presence(pport):
	return all(x in pport for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])


def validate_data(pport):
	f = dict(x.split(':') for x in pport.split())
	if not date_match.match(f['byr']) or not int(f['byr']) in range(1920, 2003):
		return False
	if not date_match.match(f['iyr']) or not int(f['iyr']) in range(2010, 2021):
		return False
	if not date_match.match(f['eyr']) or not int(f['eyr']) in range(2020, 2031):
		return False
	if not hgt_match.match(f['hgt']) or ('cm' in f['hgt'] and int(f['hgt'][:-2]) not in range(150, 194)) or ('in' in f['hgt'] and int(f['hgt'][:-2]) not in range(59, 77)):
		return False
	if not hex_match.match(f['hcl']):
		return False
	if f['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
		return False
	if not pid_match.match(f['pid']):
		return False
	return True


def part_one():
	return sum(1 for x in data if validate_presence(x))


def part_two():
	return sum(1 for x in data if validate_presence(x) and validate_data(x))


if __name__ == '__main__':
	run_with_timer(part_one)  # 170 -- took 0 ms
	run_with_timer(part_two)  # 103 -- took 1 ms

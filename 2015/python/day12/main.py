import json
import re

from aoc_utils import run_with_timer

data = open('input.txt').readline().strip()

matcher = re.compile('[ a-zA-Z:,}{"\]\[]')


def part_one():
	return sum([int(x) for x in matcher.split(data) if x != ''])


def contains_red(root_obj):
	if type(root_obj) is dict:
		for k, v in root_obj.items():
			if k == 'red':
				return True
			if type(v) in (list, dict) and contains_red(v):
				root_obj[k] = ''
			elif v == 'red':
				return True
	elif type(root_obj) is list:
		for y in [x for x in root_obj if type(x) in (list, dict) and contains_red(x)]:
			root_obj.remove(y)
	else:
		return False


def part_two():
	json_data = json.loads(data)
	if contains_red(json_data):
		json_data.clear()
	return sum([int(x) for x in matcher.split(json.dumps(json_data)) if x != ''])


if __name__ == '__main__':
	run_with_timer(part_one)  # 119433 -- took 6 ms
	run_with_timer(part_two)  # 68466 -- took 6 ms

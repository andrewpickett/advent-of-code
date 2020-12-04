import re
import json
from aoc_utils import run_with_timer

data = open('input.txt').readline().strip()


def part_one():
	return sum([int(x) for x in re.split('[a-zA-Z:,}{"\]\[]', data) if x != ''])


def remove_red(root_obj):
	for (k,v) in root_obj.items():
		if type(v) is dict:
			remove_red(v)
		# elif type(v) is str and v == 'red'
		# print(str(k) + ' -- ' + str(v))

def part_two():
	json_data = json.loads(data)
	for (k,v) in json_data.items():
		print(str(k) + ' -- ' + str(type(v)))
	return


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

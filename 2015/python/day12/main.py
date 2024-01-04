from utils.timers import run_with_timer, get_data_with_timer
import json
import re


def get_data(filename):
	return open(filename).readline().strip()


def part_one(d):
	matcher = re.compile('[^-0-9]')
	return sum([int(x) for x in matcher.split(d) if x != ''])


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


def part_two(d):
	json_data = json.loads(d)
	if contains_red(json_data):
		json_data.clear()
	matcher = re.compile('[^-0-9]')
	return sum([int(x) for x in matcher.split(json.dumps(json_data)) if x != ''])


if __name__ == '__main__':
	data = get_data_with_timer(get_data, "input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

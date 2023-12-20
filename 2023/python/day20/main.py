from utils.timers import run_with_timer
from copy import deepcopy
import math

LOW = 0
HIGH = 1


def get_data(filename):
	lines = [x.strip().split(" -> ") for x in open(filename).readlines()]
	ret_val = {}
	for line in lines:
		if line[0] == "broadcaster":
			ret_val["broadcaster"] = {"name": "broadcaster", "type": None, "output": [x.strip() for x in line[1].split(",")], "on": False, "last": {}}
		else:
			ret_val[line[0][1:]] = {"name": line[0][1:], "type": line[0][0], "output": [x.strip() for x in line[1].split(",")], "on": False, "last": {}}
	ret_val["rx"] = {"name": "rx", "type": "&", "output": [], "on": False, "last": {}}

	for conj in [k for k, v in ret_val.items() if v["type"] == "&"]:
		last_map = {}
		for k, v in ret_val.items():
			if conj in v["output"]:
				last_map[k] = LOW
		ret_val[conj]["last"] = last_map
	return ret_val


def broadcast(module, pulse):
	return module, pulse, module["output"]


def flip_flop(module, pulse, _=None):
	if pulse == LOW:
		if module["on"]:
			module["on"] = False
			return module, LOW, module["output"]
		else:
			module["on"] = True
			return module, HIGH, module["output"]


def conjunction(module, pulse, src=None):
	module["last"][src["name"]] = pulse
	return module, LOW if all(module["last"].values()) else HIGH, module["output"]


def push_button(d, press_num, part2=False):
	call_queue = [broadcast(d["broadcaster"], LOW)]
	pulse_counts = {HIGH: 0, LOW: 1, "idx": {"k": "", "i": 0}}
	while len(call_queue) > 0:
		src, pulse, dests = call_queue.pop(0)
		for dest in dests:
			pulse_counts[pulse] += 1
			if dest in d:
				f = flip_flop if d[dest]["type"] == "%" else conjunction
				next_val = f(d[dest], pulse, src)
				if part2 and dest == "rx" and any(src["last"].values()):
					pulse_counts["idx"] = {"k": [k for k, v in src["last"].items() if v == HIGH][0], "i": press_num}
				if next_val:
					call_queue.append(next_val)
	return pulse_counts


def part_one(d):
	pulse_totals = {HIGH: 0, LOW: 0, "idx": {}}
	for i in range(1000):
		p = push_button(d, i)
		pulse_totals[HIGH] += p[HIGH]
		pulse_totals[LOW] += p[LOW]
	return pulse_totals[HIGH] * pulse_totals[LOW]


def part_two(d):
	i = 0
	# in analyzing the data, manually, there is only ONE node feeding our end goal of rx, which is dt -- so we'll just start from there...
	feeders = {}
	for y in d["dt"]["last"].keys():
		feeders[y] = -1
	while len([k for k, v in feeders.items() if v < 0]) > 0:
		i += 1
		p = push_button(d, i, True)
		if p["idx"]["k"]:
			feeders[p["idx"]["k"]] = p["idx"]["i"]
	return math.lcm(*feeders.values())


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, deepcopy(data))
	run_with_timer(part_two, deepcopy(data))

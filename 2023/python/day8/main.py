from utils.timers import run_with_timer
import math


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	instructions = {"steps": lines[0]}
	for x in lines[2:]:
		parts = x.split(" = ")
		lrs = parts[1].split(", ")
		instructions[parts[0]] = {"L": lrs[0][1:], "R": lrs[1][:-1]}
	return instructions


def run_to_end(d, curr_node, comp_func):
	i = 0
	while comp_func(curr_node):
		next_dir = d["steps"][i % len(d["steps"])]
		curr_node = d[curr_node][next_dir]
		i += 1
	return i


def part_one(d):
	return run_to_end(d, "AAA", lambda x: x != "ZZZ")


def part_two(d):
	curr_nodes = [x for x in d.keys() if x[-1] == "A"]
	end_counts = [run_to_end(d, x, lambda x: x[-1] != "Z") for x in curr_nodes]
	return math.lcm(*end_counts)


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

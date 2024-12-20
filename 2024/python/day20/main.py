from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid
from utils.algorithms import astar
from collections import defaultdict


def get_data(filename):
	return {"grid": Grid(file=filename), "savings": 100}


def part_one(d):
	return sum(v for v in run_shortcuts(d["grid"], 2, d["savings"]).values())


def part_two(d):
	return sum(v for v in run_shortcuts(d["grid"], 20, d["savings"]).values())


def run_shortcuts(d, size, min_savings):
	start = [x for x in d.get_points() if x.get_value() == "S"][0]
	end = [x for x in d.get_points() if x.get_value() == "E"][0]
	orig_path = astar(d, start, end)
	savings = defaultdict(int)
	for i in range(len(orig_path)-1):
		for j in range(i+1, len(orig_path)):
			taxi_dist = abs(orig_path[i].get_row() - orig_path[j].get_row()) + abs(orig_path[i].get_col() - orig_path[j].get_col())
			if taxi_dist <= size:
				s = j-i-taxi_dist
				if s >= min_savings:
					savings[s] += 1
	return savings


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

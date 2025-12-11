import functools

from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import HashableDict


def get_data(f):
	dg = {}
	for x in f.readlines():
		parts = x.strip().split(":")
		if parts[0] not in dg:
			dg[parts[0]] = tuple()
		dg[parts[0]] = dg[parts[0]] + tuple(parts[1].strip().split(" "))
	return HashableDict(dg)


def part_one(d):
	nodes_to_visit = list(d["you"])
	counter = 0

	while nodes_to_visit:
		next_node = nodes_to_visit.pop(0)
		if next_node == "out":
			counter += 1
		else:
			nodes_to_visit.extend(list(d[next_node]))
	return counter


@functools.cache
def count_paths(d, f, dac, fft):
	if f == "out":
		return 1 if dac and fft else 0
	return sum(count_paths(d, v, dac or (f == "dac"), fft or (f == "fft")) for v in d[f])


def part_two(d):
	return count_paths(d, "svr", False, False)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

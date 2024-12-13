from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import DIRS

def get_data(filename):
	return [x.strip().split(",") for x in open(filename).readlines()]


def part_one(d):
	return min(abs(x[0]) + abs(x[1]) for x in set(get_wire_positions(d[0])).intersection(set(get_wire_positions(d[1]))))


def part_two(d):
	wire1 = get_wire_positions(d[0])
	wire2 = get_wire_positions(d[1])
	return min(wire1.index(x) + wire2.index(x) + 2 for x in set(wire1).intersection(set(wire2)))


def get_wire_positions(wire):
	cur_pos = (0, 0)
	all_pos = []
	for x in wire:
		for _ in range(int(x[1:])):
			cur_pos = (cur_pos[0] + DIRS[x[0]][0], cur_pos[1] + DIRS[x[0]][1])
			all_pos.append(cur_pos)
	return all_pos


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

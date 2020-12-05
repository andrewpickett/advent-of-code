from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def calc_seat_id(t):
	return (int(t[:7].replace('F', '0').replace('B', '1'), 2))*8 + int(t[-3:].replace('L', '0').replace('R', '1'), 2)


def part_one():
	return max(calc_seat_id(x) for x in data)


def part_two():
	seat_ids = [-1] * (128*8)
	for x in data:
		seat_ids[calc_seat_id(x)] = 1

	for i in range(1, len(seat_ids)-1):
		if seat_ids[i] == -1 and seat_ids[i-1] == 1 and seat_ids[i+1] == 1:
			return i
	return None


if __name__ == '__main__':
	run_with_timer(part_one)  # 911 -- took 1 ms
	run_with_timer(part_two)  # 629 -- took 1 ms

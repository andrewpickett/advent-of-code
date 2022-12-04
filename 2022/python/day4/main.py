from aoc_utils import run_with_timer

data = [x.strip().split(",") for x in open("input.txt").readlines()]


def encomped(p1, p2):
	return (p1[0] <= p2[0] and p1[1] >= p2[1]) or (p2[0] <= p1[0] and p2[1] >= p1[1])


def overlapped(p1, p2):
	return p2[0] <= p1[0] <= p2[1] or p2[0] <= p1[1] <= p2[0] or p1[0] <= p2[0] <= p1[1] or p1[0] <= p2[1] <= p1[0]


def part_one():
	return sum(1 for x in data if encomped(list(map(int, x[0].split("-"))), list(map(int, x[1].split("-")))))


def part_two():
	return sum(1 for x in data if overlapped(list(map(int, x[0].split("-"))), list(map(int, x[1].split("-")))))


if __name__ == '__main__':
	run_with_timer(part_one)  # 441 -- took 5 ms
	run_with_timer(part_two)  # 861 -- took 6 ms

from aoc_utils import run_with_timer

data = [int(x) for x in open("input.txt").readline().strip().split(",")]


def calculate_total_fish(days):
	fish = [data.count(x) for x in range(9)]
	for x in range(days):
		next_day_fish = [0]*9
		for i, e in enumerate(fish):
			if i > 0:
				next_day_fish[i - 1] += e
			else:
				next_day_fish[6] += e
				next_day_fish[8] += e
		fish = next_day_fish
	return sum(x for x in fish)


def part_one():
	return calculate_total_fish(80)


def part_two():
	return calculate_total_fish(256)


if __name__ == '__main__':
	run_with_timer(part_one)  # 386536 -- took 0 ms
	run_with_timer(part_two)  # 1732821262171 -- took 0 ms

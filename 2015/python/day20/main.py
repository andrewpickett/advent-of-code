from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return int(open(filename).readline())


def deliver(d, num_deliveries, num_houses):
	houses = {}
	for elf in range(1, d):
		for house in range(elf, min(elf*num_houses+1, 750000), elf):
			if house not in houses:
				houses[house] = 0
			houses[house] += elf*num_deliveries

		if elf not in houses:
			houses[elf] = 0
		if houses[elf] >= d:
			return elf


def part_one(d):
	return deliver(d, 10, float("inf"))


def part_two(d):
	return deliver(d, 11, 50)


if __name__ == '__main__':
	data = get_data_with_timer(get_data, "input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def get_cals():
	elf_cals = []
	elf_total = 0
	for x in data:
		if x == "":
			elf_cals.append(elf_total)
			elf_total = 0
		else:
			elf_total += int(x)
	return elf_cals


def part_one():
	return max(get_cals())


def part_two():
	return sum(sorted(get_cals())[-3:])


if __name__ == '__main__':
	run_with_timer(part_one)  # 69501 -- took 1 ms
	run_with_timer(part_two)  # 202346 -- took 0 ms

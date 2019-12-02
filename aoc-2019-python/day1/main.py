import ir
import math


def calc_mass(val):
	return math.floor(int(val) / 3) - 2


def calc_total(start):
	if start <= 0:
		return 0
	else:
		return start + calc_total(calc_mass(start))


def part_one():
	total = 0
	for line in ir.lines:
		total += calc_mass(line)
	return total


def part_two():
	total = 0
	for line in ir.lines:
		total += calc_total(calc_mass(line))
	return total


if __name__ == '__main__':
	ir.read_lines('./input.txt')
	print(part_one())  # 3382284
	print(part_two())  # 5070541

from aoc_utils import run_with_timer

data = [x.strip().split(" ") for x in open('input.txt').readlines()]


def run_code(registers):
	inst_idx = 0
	while inst_idx < len(data):
		inst = data[inst_idx][0]
		if inst == 'hlf':
			registers[data[inst_idx][1]] //= 2
			inst_idx += 1
		elif inst == 'tpl':
			registers[data[inst_idx][1]] *= 3
			inst_idx += 1
		elif inst == 'inc':
			registers[data[inst_idx][1]] += 1
			inst_idx += 1
		elif inst == 'jmp':
			inst_idx += int(data[inst_idx][1])
		elif inst == 'jie':
			if registers[data[inst_idx][1][:-1]] % 2 == 0:
				inst_idx += int(data[inst_idx][2])
			else:
				inst_idx += 1
		elif inst == 'jio':
			if registers[data[inst_idx][1][:-1]] == 1:
				inst_idx += int(data[inst_idx][2])
			else:
				inst_idx += 1


def part_one():
	registers = {"a": 0, "b": 0}
	run_code(registers)
	return registers["b"]


def part_two():
	registers = {"a": 1, "b": 0}
	run_code(registers)
	return registers["b"]


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

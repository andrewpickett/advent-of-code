from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip().split(" ") for x in open(filename).readlines()]


def run_code(d, registers):
	inst_idx = 0
	while inst_idx < len(d):
		inst = d[inst_idx][0]
		if inst == 'hlf':
			registers[d[inst_idx][1]] //= 2
			inst_idx += 1
		elif inst == 'tpl':
			registers[d[inst_idx][1]] *= 3
			inst_idx += 1
		elif inst == 'inc':
			registers[d[inst_idx][1]] += 1
			inst_idx += 1
		elif inst == 'jmp':
			inst_idx += int(d[inst_idx][1])
		elif inst == 'jie':
			if registers[d[inst_idx][1][:-1]] % 2 == 0:
				inst_idx += int(d[inst_idx][2])
			else:
				inst_idx += 1
		elif inst == 'jio':
			if registers[d[inst_idx][1][:-1]] == 1:
				inst_idx += int(d[inst_idx][2])
			else:
				inst_idx += 1


def part_one(d):
	registers = {"a": 0, "b": 0}
	run_code(d, registers)
	return registers["b"]


def part_two(d):
	registers = {"a": 1, "b": 0}
	run_code(d, registers)
	return registers["b"]


if __name__ == '__main__':
	data = get_data_with_timer(get_data, "input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

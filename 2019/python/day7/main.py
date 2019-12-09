from intcode import IntcodeOpMachine
from itertools import permutations, cycle

data = [int(x) for x in open("input.txt").readline().split(',')]


def part_one():
	phases = [''.join(p) for p in permutations('01234')]
	max_input = 0
	for series in phases:
		next_input = 0
		machines = []
		for phase in series:
			machines.append(IntcodeOpMachine(list(data), in_val = next_input, phase_setting=int(phase)))

		for machine in machines:
			machine.in_val = next_input
			machine.run_until_halt()
			next_input = machine.output[-1]

		if next_input > max_input:
			max_input = next_input
	return max_input


def part_two():
	phases = [''.join(p) for p in permutations('56789')]
	max_input = 0
	for series in phases:
		next_input = 0
		machines = []
		for phase in series:
			machines.append(IntcodeOpMachine(list(data), in_val=next_input, phase_setting=int(phase)))

		active_machines = []
		for machine in cycle(machines):
			if machine not in active_machines and not machine.halted:
				active_machines.append(machine)
			machine.in_val = next_input
			exit_code = machine.run()
			next_input = machine.output[-1]

			if exit_code == 99:
				active_machines.remove(machine)
			if not active_machines:
				break

		if next_input > max_input:
			max_input = next_input
	return max_input


if __name__ == '__main__':
	print(part_one())  # 38834
	print(part_two())  # 69113332

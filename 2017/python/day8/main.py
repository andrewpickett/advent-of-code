from utils.timers import run_with_timer, get_data_with_timer


class Instruction:
	def __init__(self, target, operation, amount):
		self.target = target
		self.operation = operation
		self.amount = amount


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def get_operands(registers, lh, rh):
	a = int(lh) if str(lh).lstrip("-").isnumeric() else registers[lh]
	b = int(rh) if str(rh).lstrip("-").isnumeric() else registers[rh]
	return a, b


def init_registers(registers, inst):
	if inst[0] not in registers:
		registers[inst[0]] = 0
	if inst[4] not in registers:
		registers[inst[4]] = 0


def get_maximums(d):
	registers = {}
	old_max = 0
	for inst in d:
		parts = inst.split()
		init_registers(registers, parts)
		instruction = Instruction(parts[0], parts[1], int(parts[2]))
		operands = get_operands(registers, parts[4], parts[6])

		operation = None
		match parts[5]:
			case "==":
				operation = lambda x: x[0] == x[1]
			case "!=":
				operation = lambda x: x[0] != x[1]
			case ">":
				operation = lambda x: x[0] > x[1]
			case "<":
				operation = lambda x: x[0] < x[1]
			case ">=":
				operation = lambda x: x[0] >= x[1]
			case "<=":
				operation = lambda x: x[0] <= x[1]
		if operation(operands):
			registers[instruction.target] += instruction.amount if instruction.operation == "inc" else -instruction.amount
			old_max = max(old_max, registers[instruction.target])
	return registers, old_max


def part_one(d):
	registers, _ = get_maximums(d)
	return max(registers.values())


def part_two(d):
	_, old_max = get_maximums(d)
	return old_max


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

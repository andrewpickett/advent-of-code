from utils.timers import run_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


class Instruction:
	def __init__(self, target, operation, amount):
		self.target = target
		self.operation = operation
		self.amount = amount


def get_operands(registers, lh, rh):
	a = int(lh) if str(lh).lstrip("-").isnumeric() else registers[lh]
	b = int(rh) if str(rh).lstrip("-").isnumeric() else registers[rh]
	return a, b


def comp_eq(operands):
	return operands[0] == operands[1]


def comp_ne(operands):
	return operands[0] != operands[1]


def comp_lt(operands):
	return operands[0] < operands[1]


def comp_gt(operands):
	return operands[0] > operands[1]


def comp_le(operands):
	return operands[0] <= operands[1]


def comp_ge(operands):
	return operands[0] >= operands[1]


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
				operation = comp_eq
			case "!=":
				operation = comp_ne
			case ">":
				operation = comp_gt
			case "<":
				operation = comp_lt
			case ">=":
				operation = comp_ge
			case "<=":
				operation = comp_le
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


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

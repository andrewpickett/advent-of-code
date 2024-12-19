from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	return {"registers": {"a": int(lines[0].split()[-1]), "b": int(lines[1].split()[-1]), "c": int(lines[2].split()[-1])}, "inst": list(map(int, lines[4].split()[-1].split(",")))}


def part_one(d):
	return ','.join(list(map(str, run(d["registers"], d["inst"]))))


def part_two(d):
	i = 0
	for x in range(1, len(d["inst"])+1):
		while True:
			registers = {"a": i, "b": 0, "c": 0}
			outputs = run(registers, d["inst"])
			if outputs[-x:] == d["inst"][-x:]:
				break
			i += 8**(len(d["inst"])-x)
	return i


def run(registers, instructions):
	outputs = []
	inst_pointer = 0
	while inst_pointer < len(instructions):
		inst = instructions[inst_pointer]
		operand = instructions[inst_pointer+1]
		if inst == 3 and registers["a"] != 0:
			inst_pointer = operand
		else:
			if inst == 1:
				registers["b"] ^= operand
			elif inst == 2:
				registers["b"] = combo(registers, operand) % 8
			elif inst == 4:
				registers["b"] ^= registers["c"]
			elif inst == 5:
				outputs.append(combo(registers, operand) % 8)
			elif inst == 0:
				registers["a"] = registers["a"] // 2**combo(registers, operand)
			elif inst == 6:
				registers["b"] = registers["a"] // 2**combo(registers, operand)
			elif inst == 7:
				registers["c"] = registers["a"] // 2**combo(registers, operand)
			inst_pointer += 2
	return outputs


def combo(registers, operand):
	if 0 <= operand <= 3:
		return operand
	if operand == 4:
		return registers["a"]
	if operand == 5:
		return registers["b"]
	if operand == 6:
		return registers["c"]


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

from utils.timers import run_with_timer, get_data_with_timer
from utils.opcode import OpCodeOperation, OP_CODES


def get_data(filename):
	ret_val = {"examples": [], "program": []}
	lines = [x.strip() for x in open(filename).readlines()]
	in_program = False
	i = 0
	while i < len(lines):
		line = lines[i]
		if not line.startswith("Before:"):
			in_program = True
		if not in_program:
			ret_val["examples"].append({
				"b": [int(x) for x in lines[i].replace("[", "_").replace("]", "_").split("_")[1].split(",")],
				"i": [int(x) for x in lines[i+1].split()],
				"a": [int(x) for x in lines[i+2].replace("[", "_").replace("]", "_").split("_")[1].split(",")]
			})
		if in_program and line != "":
			ret_val["program"].append([int(x) for x in line.split()])
		i += 1 if in_program else 4
	return ret_val


def part_one(d):
	return sum(1 for x in d["examples"].copy() if sum(1 for y in OP_CODES if OP_CODES[y].eval(x["i"], x["b"].copy()) == x["a"]) >= 3)


def part_two(d):
	opcode_map = get_opcode_map(d["examples"].copy())
	registers = run_program(d["program"], opcode_map)
	return registers[0]


def get_opcode_map(examples):
	opcode_map = {i: [] for i in range(16)}
	for x in examples:
		opcode_map[x["i"][0]].append(x)
	new_map = {i: [] for i in range(16)}
	for k, v in opcode_map.items():
		for name, op in OP_CODES.items():
			match = True
			for example in v:
				if op.eval(example["i"], example["b"].copy()) != example["a"]:
					match = False
					break
			if match:
				new_map[k].append(name)

	i = 0
	while i < len(new_map):
		removed = False
		if len(new_map[i]) == 1:
			for x in new_map:
				if x != i and new_map[i][0] in new_map[x]:
					removed = True
					new_map[x].remove(new_map[i][0])
		i += -i if removed else 1
	return new_map


def run_program(program, opcode_map):
	registers = [0, 0, 0, 0]
	for line in program:
		registers = OpCodeOperation.get_instance(opcode_map[line[0]][0]).eval(line, registers)
	return registers


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

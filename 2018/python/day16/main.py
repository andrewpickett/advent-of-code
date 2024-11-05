from utils.timers import run_with_timer, get_data_with_timer


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


ops = {
	"addi": lambda a, b: add(a.copy(), b, True),
	"addr": lambda a, b: add(a.copy(), b, False),
	"muli": lambda a, b: mul(a.copy(), b, True),
	"mulr": lambda a, b: mul(a.copy(), b, False),
	"bani": lambda a, b: ban(a.copy(), b, True),
	"banr": lambda a, b: ban(a.copy(), b, False),
	"bori": lambda a, b: bor(a.copy(), b, True),
	"borr": lambda a, b: bor(a.copy(), b, False),
	"seti": lambda a, b: setop(a.copy(), b, True),
	"setr": lambda a, b: setop(a.copy(), b, False),
	"gtir": lambda a, b: gti(a.copy(), b, False),
	"gtri": lambda a, b: gtr(a.copy(), b, True),
	"gtrr": lambda a, b: gtr(a.copy(), b, False),
	"eqir": lambda a, b: eqi(a.copy(), b, False),
	"eqri": lambda a, b: eqr(a.copy(), b, True),
	"eqrr": lambda a, b: eqr(a.copy(), b, False)
}


def part_one(d):
	return sum(1 for x in d["examples"].copy() if sum(1 for y in ops if ops[y](x["b"], x["i"]) == x["a"]) >= 3)


def add(reg, inst, immediate):
	reg[inst[3]] = reg[inst[1]] + (inst[2] if immediate else reg[inst[2]])
	return reg


def mul(reg, inst, immediate):
	reg[inst[3]] = reg[inst[1]] * (inst[2] if immediate else reg[inst[2]])
	return reg


def ban(reg, inst, immediate):
	reg[inst[3]] = reg[inst[1]] & (inst[2] if immediate else reg[inst[2]])
	return reg


def bor(reg, inst, immediate):
	reg[inst[3]] = reg[inst[1]] | (inst[2] if immediate else reg[inst[2]])
	return reg


def setop(reg, inst, immediate):
	reg[inst[3]] = inst[1] if immediate else reg[inst[1]]
	return reg


def gti(reg, inst, immediate=True):
	reg[inst[3]] = 1 if inst[1] > reg[inst[2]] else 0
	return reg


def gtr(reg, inst, immediate):
	reg[inst[3]] = 1 if reg[inst[1]] > (inst[2] if immediate else reg[inst[2]]) else 0
	return reg


def eqi(reg, inst, immediate=True):
	reg[inst[3]] = 1 if inst[1] == reg[inst[2]] else 0
	return reg


def eqr(reg, inst, immediate):
	reg[inst[3]] = 1 if reg[inst[1]] == (inst[2] if immediate else reg[inst[2]]) else 0
	return reg


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
		for name, op in ops.items():
			match = True
			for example in v:
				if op(example["b"].copy(), example["i"]) != example["a"]:
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
		registers = ops[opcode_map[line[0]][0]](registers, line)
	return registers


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

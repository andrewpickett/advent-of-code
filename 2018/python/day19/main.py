from utils.timers import run_with_timer, get_data_with_timer
from utils.opcode import OpCodeOperation


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	ret_val = {"program": [], "ip": int(lines[0].split()[1])}
	for line in lines[1:]:
		ret_val["program"].append([line.split()[0]] + [int(x) for x in line.split()[1:]])
	return ret_val


def part_one(d):
	registers = [0, 0, 0, 0, 0, 0]
	run_program(registers, d)
	return registers[0]


def part_two(d):
	registers = [1, 0, 0, 0, 0, 0]
	run_program(registers, d)
	return registers[0]


def run_program(registers, d):
	ip = 0
	ops = {}
	while 0 <= ip < len(d["program"]):
		if ip == 2 and registers[3] != 0:
			registers[0] = sum(x for x in range(1, registers[5]+1) if registers[5] % x == 0)
			break
		registers[d["ip"]] = ip
		inst = d["program"][ip]
		if inst[0] not in ops:
			ops[inst[0]] = OpCodeOperation.get_instance(inst[0])
		registers = ops[inst[0]].eval(inst, registers)
		ip = registers[d["ip"]] + 1


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

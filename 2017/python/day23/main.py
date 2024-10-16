from utils.timers import run_with_timer, get_data_with_timer
from utils.duet import DuetProgram, DuetMultiply


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def part_one(d):
	p = DuetProgram(code=d, sound=True)
	p.run()
	return p.debug_calls[DuetMultiply.OP_NAME]


def part_two(d):
	init_instructions = d[:11].copy()
	p = DuetProgram(code=init_instructions, sound=True)
	p.registers["a"] = 1
	p.run()
	step = -int(d[-2].split()[-1])
	h = 0
	for x in range(p.registers["b"], p.registers["c"]+1, step):
		for i in range(2, x):
			if x % i == 0:
				h += 1
				break
	return h


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main("input.txt")

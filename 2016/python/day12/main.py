from utils.timers import run_with_timer, get_data_with_timer
from utils.assembunny import AssembunnyProgram


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def run_input(d, registers, out_val):
	p = AssembunnyProgram(code=d, registers=registers)
	p.run()
	return p.registers[out_val]


def part_one(d):
	return run_input(d, None, "a")


def part_two(d):
	return run_input(d, {"a": 0, "b": 0, "c": 1, "d": 0}, "a")


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

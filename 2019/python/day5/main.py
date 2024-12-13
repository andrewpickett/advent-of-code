from utils.timers import run_with_timer, get_data_with_timer
from utils.intcode import IntcodeMachine


def get_data(filename):
	return [int(x) for x in open(filename).readline().split(',')]


def part_one(d):
	machine = IntcodeMachine(d)
	machine.set_inputs([1])
	machine.run()
	return machine.outputs[-1]


def part_two(d):
	machine = IntcodeMachine(d)
	machine.set_inputs([5])
	machine.run()
	return machine.outputs[-1]


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data.copy())
	run_with_timer(part_two, data.copy())


if __name__ == '__main__':
	main()

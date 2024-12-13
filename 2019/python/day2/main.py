from utils.timers import run_with_timer, get_data_with_timer
from utils.intcode import IntcodeMachine


def get_data(filename):
	return {"input": [12,2], "instructions": [int(x) for x in open(filename).readline().split(',')], "target": 19690720}


def part_one(d):
	machine = IntcodeMachine([d["instructions"][0]] + d["input"] + d["instructions"][3:])
	machine.run()
	return machine.instructions[0]


def part_two(d):
	for noun in range(100):
		for verb in range(100):
			machine = IntcodeMachine([d["instructions"][0]] + [noun, verb] + d["instructions"][3:])
			machine.run()
			if machine.instructions[0] == d["target"]:
				return noun*100+verb
	return None


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data.copy())
	run_with_timer(part_two, data.copy())


if __name__ == '__main__':
	main()

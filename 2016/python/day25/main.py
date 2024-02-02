from utils.timers import run_with_timer, get_data_with_timer
from utils.assembunny import AssembunnyProgram


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def part_one(d):
	counter = 0
	valid = False
	while not valid:
		p = AssembunnyProgram(code=d, registers={"a": counter, "b": 0, "c": 1, "d": 0})
		valid = p.run(limit=40000)
		counter += 1
	return counter - 1


def part_two(d):
	return


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

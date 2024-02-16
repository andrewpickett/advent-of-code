from utils.timers import run_with_timer, get_data_with_timer
from utils.duet import DuetProgram


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def part_one(d):
	return DuetProgram(code=d, sound=True).run()


def part_two(d):
	a = DuetProgram(code=d, sound=False)
	a.registers["p"] = 0
	b = DuetProgram(code=d, sound=False)
	b.registers["p"] = 1
	all_sends = []
	while not a.waiting or not b.waiting:
		a.run()
		a.send(b)

		b.run()
		all_sends.extend(b.registers["snd"])
		b.send(a)
	return len(all_sends)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip().split(" ") for x in open(filename).readlines()]


def run_input(d, registers, output_val):
	p = 0
	while p < len(d):
		inst = d[p][0]
		v = int(d[p][1]) if d[p][1].isnumeric() else registers[d[p][1]]
		if inst == "cpy":
			registers[d[p][2]] = v
			p += 1
		elif inst == "jnz":
			p += 1 if v == 0 else int(d[p][2])
		else:
			registers[d[p][1]] += 1 if inst == "inc" else -1
			p += 1
	return registers[output_val]


def part_one(d):
	return run_input(d, {"a": 0, "b": 0, "c": 0, "d": 0}, "a")


def part_two(d):
	return run_input(d, {"a": 0, "b": 0, "c": 1, "d": 0}, "a")


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

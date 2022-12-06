from aoc_utils import run_with_timer

data = [x.strip().split(" ") for x in open("input.txt").readlines()]


def run_input(registers, output_val):
	p = 0
	while p < len(data):
		match data[p][0]:
			case "cpy":
				registers[data[p][2]] = int(data[p][1]) if data[p][1].isnumeric() else registers[data[p][1]]
				p += 1
			case "inc":
				registers[data[p][1]] += 1
				p += 1
			case "dec":
				registers[data[p][1]] -= 1
				p += 1
			case "jnz":
				p += 1 if (data[p][1].isnumeric() and int(data[p][1]) == 0) or (not data[p][1].isnumeric() and registers[data[p][1]] == 0) else int(data[p][2])
	return registers[output_val]


def part_one():
	return run_input({"a": 0, "b": 0, "c": 0, "d": 0}, "a")


def part_two():
	return run_input({"a": 0, "b": 0, "c": 1, "d": 0}, "a")


if __name__ == '__main__':
	run_with_timer(part_one)  # 318003 -- took 663 ms
	run_with_timer(part_two)  # 9227657 -- took 19928 ms

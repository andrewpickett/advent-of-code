from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [int(x.strip()) for x in open(filename).readlines()]


def part_one(d):
	return sum(calc_spec_fuel(i) for i in d)


def part_two(d):
	return sum(calc_total_fuel(i) for i in d)


def calc_spec_fuel(val):
	return (val // 3) - 2


def calc_total_fuel(start):
	n = calc_spec_fuel(start)
	return 0 if n <= 0 else n + calc_total_fuel(n)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

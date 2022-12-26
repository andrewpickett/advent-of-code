from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


mapping = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}


def snafu_to_decimal(snafu):
	return sum(mapping[x] * pow(5, len(snafu) - i - 1) for i, x in enumerate(snafu))


def decimal_to_snafu(decimal):
	if decimal > 0:
		d, m = divmod(decimal+2, 5)
		return decimal_to_snafu(d) + list(mapping.keys())[m]
	return ""


def part_one():
	return decimal_to_snafu(sum(snafu_to_decimal(x) for x in data))


def part_two():
	# Nothing! Merry Christmas!!
	return


if __name__ == '__main__':
	run_with_timer(part_one)  # 2-0=11=-0-2-1==1=-22 -- took 3 ms
	run_with_timer(part_two)  # None!

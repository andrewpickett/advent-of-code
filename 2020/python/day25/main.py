from aoc_utils import run_with_timer

data = [int(x.strip()) for x in open("input.txt").readlines()]


def part_one():
	subject_number = 7

	card_public_key = data[0]
	door_public_key = data[1]

	door_loop_size = 0

	val = 1
	while val != door_public_key:
		val *= subject_number
		val %= 20201227
		door_loop_size += 1

	val = 1
	for i in range(door_loop_size):
		val *= card_public_key
		val %= 20201227
	return val


def part_two():
	return 0


if __name__ == '__main__':
	run_with_timer(part_one)  # 18329280 -- took 4313 ms
	run_with_timer(part_two)  # 0 -- took 0 ms

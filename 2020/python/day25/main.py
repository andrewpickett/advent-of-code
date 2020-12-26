from aoc_utils import run_with_timer

card_public_key, door_public_key = [int(x.strip()) for x in open("input.txt").readlines()]


def transform_val(val, subject_number):
	return (val * subject_number) % 20201227


def part_one():
	subject_number = 7
	door_loop_size = 0
	val = 1
	while val != door_public_key:
		val = transform_val(val, subject_number)
		door_loop_size += 1

	val = 1
	for _ in range(door_loop_size):
		val = transform_val(val, card_public_key)
	return val


def part_two():
	return 0


if __name__ == '__main__':
	run_with_timer(part_one)  # 18329280 -- took 4313 ms
	run_with_timer(part_two)  # 0 -- took 0 ms

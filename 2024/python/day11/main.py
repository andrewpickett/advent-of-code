from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	data = [int(x) for x in open(filename).readline().strip().split()]
	return {num:data.count(num) for num in set(data)}


def part_one(d):
	return blink_a_bunch(d, 25)


def part_two(d):
	return blink_a_bunch(d, 75)


def blink_a_bunch(d, num):
	for _ in range(num):
		d = blink(d)
	return sum(x for x in d.values())

def blink(d):
	new_counts = {}
	for s, c in d.items():
		if s == 0:
			single_move = [1]
		elif len(str(s)) % 2 == 0:
			single_move = [int(str(s)[:len(str(s))//2]), int(str(s)[len(str(s))//2:])]
		else:
			single_move = [2024 * s]

		for stone in single_move:
			if stone not in new_counts:
				new_counts[stone] = 0
			new_counts[stone] += c
	return new_counts


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data.copy())
	run_with_timer(part_two, data.copy())


if __name__ == '__main__':
	main("input.txt")

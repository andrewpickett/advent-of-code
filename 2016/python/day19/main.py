from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return int(open(filename).readline())


def part_one(d):
	return (2*d) - 2**(len("{0:b}".format(2*d))-1) | 1


def part_two(d):
	s = 2
	while s < d:
		s = s * 3 - 2
	s = (s + 2) // 3

	winner = d - s + 1
	if winner >= d:
		winner = winner * 2 - 9
	return winner


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

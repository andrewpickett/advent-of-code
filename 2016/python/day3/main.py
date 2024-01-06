from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [tuple([int(y.strip()) for y in x.strip().split(' ') if y.strip() != '']) for x in open(filename).readlines()]


def part_one(d):
	return sum(1 for x in d if 2 * max(x) < sum(x))


def part_two(d):
	possible = 0
	for i in range(0, len(d), 3):
		for j in range(0, 3):
			t = (d[i][j], d[i+1][j], d[i+2][j])
			possible += 1 if 2 * max(t) < sum(t) else 0
	return possible


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()


from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [int(x) for x in open(filename).readline().split('-')]


def part_one(d):
	return sum(check_number_for_validity(str(i)) for i in range(d[0], d[1]))


def part_two(d):
	return sum(check_number_for_validity(str(i), True) for i in range(d[0], d[1]))


def check_number_for_validity(num, additional_check=False):
	consecutive = False
	increasing = num == ''.join(list(sorted(list(num))))
	if increasing:
		for j in range(len(num) - 1):
			if int(num[j + 1]) == int(num[j]) and (not additional_check or (additional_check and num.count(num[j]) == 2)):
				consecutive = True
				break
	return 1 if consecutive and increasing else 0


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

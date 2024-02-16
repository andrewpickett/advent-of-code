from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return int(open(filename).readline().strip())


def spin(d, insertions, target_pos=None):
	spinlock = [0]
	curr_pos = 0
	end_val = 0
	for i in range(1, insertions+1):
		curr_pos = (curr_pos + d) % i + 1
		if not target_pos:
			spinlock.insert(curr_pos, i)
		if curr_pos == target_pos:
			end_val = i
	return spinlock, curr_pos, end_val


def part_one(d):
	spinlock, curr_pos, _ = spin(d, 2017)
	return spinlock[curr_pos+1]


def part_two(d):
	_, _, end_val = spin(d, 50000000, 1)
	return end_val


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

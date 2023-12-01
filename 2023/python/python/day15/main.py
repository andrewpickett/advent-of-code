from utils.timers import run_with_timer


def get_data(filename):
	return open(filename).readline().strip()


def part_one(d):
	return True


def part_two(d):
	return False


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return open(filename).readline().strip()


ALPHA = "abcdefghijklmnopqrstuvwxyyz"


def part_one(d):
	return len(react(d))


def part_two(d):
	min_len = float("inf")
	for r in ALPHA:
		if r in d:
			polymer = d.replace(r, "").replace(r.upper(), "")
			new_len = len(react(polymer))
			if new_len < min_len:
				min_len = new_len
	return min_len


def react(polymer):
	found = True
	while found:
		found = False
		for r in ALPHA:
			if r+r.upper() in polymer or r.upper()+r in polymer:
				polymer = polymer.replace(r+r.upper(), "").replace(r.upper()+r, "")
				found = True
	return polymer


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

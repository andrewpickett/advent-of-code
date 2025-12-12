from utils.timers import run_with_timer, get_data_with_timer


def get_data(f):
	parts = f.read().split("\n\n")
	return {"d": [present.count('#') for present in parts[:-1]], "r": parts[-1].strip().split('\n')}


def part_one(d):
	counter = 0
	for region in d["r"]:
		parts = region.split(": ")
		x, y = list(map(int, parts[0].split("x")))
		counts = list(map(int, parts[1].split(" ")))
		total_presents = sum(counts)
		if total_presents <= (x // 3) * (y // 3):
			counter += 1
	return counter


def part_two(d):
	return


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

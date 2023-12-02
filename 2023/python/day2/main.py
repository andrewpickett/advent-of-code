from utils.timers import run_with_timer


def get_data(filename):
	return [x[x.find(":")+1:].strip() for x in open(filename).readlines()]


def part_one(d):
	max_amounts = {
		"red": 12,
		"green": 13,
		"blue": 14
	}
	s = 0
	for i, x in enumerate(d):
		hands = x.split(";")
		possible = True
		for hand in hands:
			parts = hand.replace(",", "").split()
			for j in range(0, len(parts), 2):
				if int(parts[j]) > max_amounts[parts[j+1]]:
					possible = False
					break
			if not possible:
				break
		if possible:
			s += i+1
	return s


def part_two(d):
	s = 0
	for i, x in enumerate(d):
		hands = x.split(";")
		mins = {
			"red": 0,
			"blue": 0,
			"green": 0
		}
		for hand in hands:
			parts = hand.replace(",", "").split()
			for j in range(0, len(parts), 2):
				mins[parts[j+1]] = max(mins[parts[j+1]], int(parts[j]))
		s += mins["red"] * mins["blue"] * mins["green"]
	return s


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

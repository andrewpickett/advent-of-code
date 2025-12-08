from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import get_overlapping_ranges


def get_data(f):
	parts = [x.strip() for x in f.read().split("\n\n")]
	ranges = [x.strip() for x in parts[0].split("\n")]
	ids = [int(x.strip()) for x in parts[1].split("\n")]
	rs = []
	for r in ranges:
		k = r.split("-")
		rs.append(range(int(k[0]), int(k[1])+1))
	return {"r": get_overlapping_ranges(rs), "ids": ids}


def part_one(d):
	count = 0
	for x in d["ids"]:
		for y in d["r"]:
			if x in y:
				count += 1
				break
	return count


def part_two(d):
	return sum(len(x) for x in d["r"])


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

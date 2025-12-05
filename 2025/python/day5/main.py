from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import get_overlapping_ranges


def get_data(filename):
	parts = [x.strip() for x in open(filename).read().split("\n\n")]
	ranges = [x.strip() for x in parts[0].split("\n")]
	ids = [int(x.strip()) for x in parts[1].split("\n")]
	rs = []
	for r in ranges:
		k = r.split("-")
		rs.append(range(int(k[0]), int(k[1])+1))
	return {"r": get_overlapping_ranges(rs), "ids": ids}


def part_one(d):
	fresh = []
	for x in d["ids"]:
		spoiled = True
		for y in d["r"]:
			if x in y:
				spoiled = False
				break
		if not spoiled:
			fresh.append(x)
	return len(fresh)


def part_two(d):
	return sum(len(x) + 1 for x in d["r"])


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

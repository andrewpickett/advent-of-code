from utils.timers import run_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


ticker = {
	"children": 3,
	"cats": 7,
	"samoyeds": 2,
	"pomeranians": 3,
	"akitas": 0,
	"vizslas": 0,
	"goldfish": 5,
	"trees": 3,
	"cars": 2,
	"perfumes": 1
}


def get_sues_list(d):
	return [{parts[i*2+2][:-1]: int(parts[i*2+3].replace(',', '')) for i in range(len(parts)//2 - 1)} for parts in [x.split() for x in d]]


def part_one(d):
	sues = get_sues_list(d)
	return [sues.index(sue)+1 for sue in sues if sum(1 if sue[x] == ticker[x] else 0 for x in sue.keys() & ticker.keys()) == len(sue)][0]


def part_two(d):
	sues = get_sues_list(d)
	for sue in sues:
		match_found = True
		for prop in ticker.keys():
			if prop in sue.keys():
				if prop in ('cats', 'trees'):
					if ticker[prop] >= sue[prop]:
						match_found = False
				elif prop in ('pomeranians', 'goldfish'):
					if ticker[prop] <= sue[prop]:
						match_found = False
				elif ticker[prop] != sue[prop]:
					match_found = False
		if match_found:
			return sues.index(sue) + 1
	return


if __name__ == '__main__':
	data = get_data("input.txt")
	run_with_timer(part_one, data)  # 40 -- took 2 ms
	run_with_timer(part_two, data)  # 241 -- took 1 ms

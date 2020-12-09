from aoc_utils import run_with_timer

data = [x.strip() for x in open('input.txt').readlines()]
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


def get_sues_list():
	return [{parts[i*2+2][:-1]: int(parts[i*2+3].replace(',', '')) for i in range(len(parts)//2 - 1)} for parts in [x.split() for x in data]]


def part_one():
	sues = get_sues_list()
	for sue in get_sues_list():
		match_found = True
		for prop in ticker.keys():
			if prop in sue.keys() and ticker[prop] != sue[prop]:
				match_found = False
		if match_found:
			return sues.index(sue) + 1
	return


def part_two():
	sues = get_sues_list()
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
	run_with_timer(part_one)  # 40 -- took 2 ms
	run_with_timer(part_two)  # 241 -- took 1 ms

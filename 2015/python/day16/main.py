from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [{parts[i*2+2][:-1]: int(parts[i*2+3].replace(',', '')) for i in range(len(parts)//2 - 1)} for parts in [x.split() for x in [y.strip() for y in open(filename).readlines()]]]


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


def part_one(d):
	return [d.index(sue)+1 for sue in d if sum(1 if sue[x] == ticker[x] else 0 for x in sue.keys() & ticker.keys()) == len(sue)][0]


def part_two(d):
	for sue in d:
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
			return d.index(sue) + 1
	return


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

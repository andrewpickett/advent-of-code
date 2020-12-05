from aoc_utils import run_with_timer

data = [x.strip() for x in open('input.txt').readlines()]


def calc_distance(r, time):
	x = time // (r['r']+r['t'])
	y = time % (r['r']+r['t'])
	return (x * r['s'] * r['t']) + (r['s']*r['t'] if y >= r['t'] else r['s']*y)


def part_one():
	r = dict([(x[0], {"s":int(x[3]),"t":int(x[6]),"r":int(x[13])}) for x in [y.split() for y in data]])
	return max(calc_distance(r[x], 2503) for x in r)


def part_two():
	r = dict([(x[0], {"s":int(x[3]),"t":int(x[6]),"r":int(x[13]),"p":0}) for x in [y.split() for y in data]])
	for i in range(1, 2504):
		max_dist = 0
		r_in_lead = None
		for reindeer in r:
			d = calc_distance(r[reindeer], i)
			if d > max_dist:
				r_in_lead = reindeer
				max_dist = d
		r[r_in_lead]['p'] += 1
	return max(r[x]['p'] for x in r)


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

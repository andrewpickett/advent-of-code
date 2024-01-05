from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return dict([(x[0], {"s": int(x[3]), "t": int(x[6]), "r": int(x[13]), "p": 0}) for x in [y.split() for y in [x.strip() for x in open(filename).readlines()]]])


def calc_distance(r, time):
	x, y = divmod(time, (r['r']+r['t']))
	return (x * r['s'] * r['t']) + (r['s'] * r['t'] if y >= r['t'] else r['s'] * y)


def part_one(d):
	return max(calc_distance(d[x], 2503) for x in d)


def part_two(d):
	for i in range(1, 2504):
		max_dist = 0
		r_in_lead = None
		for reindeer in d:
			dist = calc_distance(d[reindeer], i)
			if dist > max_dist:
				r_in_lead = reindeer
				max_dist = dist
		d[r_in_lead]['p'] += 1
	return max(d[x]['p'] for x in d)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

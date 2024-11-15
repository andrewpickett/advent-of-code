from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [tuple([int(y) for y in x.strip().split(",")]) for x in open(filename).readlines()]


def part_one(d):
	dists = {}
	for i, x in enumerate(d):
		if x not in dists:
			dists[x] = set()
		for j, y in enumerate(d[i+1:]):
			if abs(x[0]-y[0]) + abs(x[1]-y[1]) + abs(x[2]-y[2]) + abs(x[3]-y[3]) <= 3:
				dists[x].add(y)
	expanded = True
	while expanded:
		expanded = False
		key_to_remove = None
		for k, v in dists.items():
			for k2, v2 in dists.items():
				if k != k2 and k in v2:
					v.update(v2)
					expanded = True
					key_to_remove = k2
					break
			if expanded:
				break
		if key_to_remove in dists:
			del dists[key_to_remove]
	return len(dists)


def part_two(d):
	return


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

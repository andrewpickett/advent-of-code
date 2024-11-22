from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	ret_val = []
	for x in lines:
		parts = x.split(", ")
		ret_val.append(tuple([int(y) for y in parts[0][parts[0].find("<")+1:parts[0].find(">")].split(",")] + [int(parts[1].split("=")[1])]))

	ret_val.sort(key=lambda x: x[-1], reverse=True)
	return ret_val


def part_one(d):
	return sum(1 for x in d if abs(x[0]-d[0][0]) + abs(x[1]-d[0][1]) + abs(x[2]-d[0][2]) <= d[0][3])


def part_two(d):
	vals = [[x[0] for x in d], [x[1] for x in d], [x[2] for x in d]]
	offsets = [-min(vals[0]), -min(vals[1]), -min(vals[2])]

	dist = 1
	while dist < max(vals[0]) - min(vals[0]) or dist < max(vals[1]) - min(vals[1]) or dist < max(vals[2]) - min(vals[2]):
		dist *= 2

	span = 1
	while span < len(d):
		span *= 2

	forced_check = 1
	tried = {}
	best_val, best_count = None, None

	while True:
		if forced_check not in tried:
			tried[forced_check] = find(set(), d, vals, dist, offsets, forced_check)
		test_val, test_count = tried[forced_check]
		if test_val is None:
			if span > 1:
				span = span // 2
			forced_check = max(1, forced_check - span)
		else:
			if best_count is None or test_count > best_count:
				best_val, best_count = test_val, test_count
			if span == 1:
				break
			forced_check += span
	return best_val


def find(done, bots, vals, dist, offsets, forced_count):
	at_target = []
	for x in range(min(vals[0]), max(vals[0])+1, dist):
		for y in range(min(vals[1]), max(vals[1])+1, dist):
			for z in range(min(vals[2]), max(vals[2])+1, dist):
				count = 0
				for bx, by, bz, bdist in bots:
					if dist == 1:
						calc = abs(x - bx) + abs(y - by) + abs(z - bz)
						if calc <= bdist:
							count += 1
					else:
						calc =  abs((offsets[0]+x) - (offsets[0]+bx))
						calc += abs((offsets[1]+y) - (offsets[1]+by))
						calc += abs((offsets[2]+z) - (offsets[2]+bz))
						if calc //dist - 3 <= bdist // dist:
							count += 1
				if count >= forced_count:
					at_target.append((x, y, z, count, abs(x) + abs(y) + abs(z)))

	while len(at_target) > 0:
		best = []
		best_i = None
		for i in range(len(at_target)):
			if best_i is None or at_target[i][4] < best[4]:
				best = at_target[i]
				best_i = i

		if dist == 1:
			return best[4], best[3]
		else:
			xs = [best[0], best[0] + dist//2]
			ys = [best[1], best[1] + dist//2]
			zs = [best[2], best[2] + dist//2]
			a, b = find(done, bots, [xs, ys, zs], dist // 2, offsets, forced_count)
			if a is None:
				at_target.pop(best_i)
			else:
				return a, b
	return None, None


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data.copy())
	run_with_timer(part_two, data.copy())


if __name__ == '__main__':
	main()

from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	ret_val = {"p": [], "v": []}
	for x in lines:
		parts = x.replace("<", "_").replace(">", "_").replace(",", "_").split("_")
		ret_val["p"].append((int(parts[1].strip()), int(parts[2].strip())))
		ret_val["v"].append((int(parts[4].strip()), int(parts[5].strip())))
	return ret_val


def part_one(d):
	p, _ = run(d["p"].copy(), d["v"].copy())
	return write_out(p)


def part_two(d):
	_, i = run(d["p"].copy(), d["v"].copy())
	return i


def run(p, v):
	i = 0
	while not should_stop(p):
		for x in range(len(p)):
			p[x] = (p[x][0] + v[x][0], p[x][1] + v[x][1])
		i += 1
	return p, i


def should_stop(p):
	ys = [x[1] for x in p]
	miny, maxy, minx, maxx = get_range(p)

	for y in range(miny, maxy+1):
		if y not in ys:
			return False
	for x in range(minx, maxx+1):
		full_col = True
		for y in range(miny, maxy+1):
			if (x, y) not in p:
				full_col = False
				break
		if full_col:
			return True
	return False


def write_out(p):
	miny, maxy, minx, maxx = get_range(p)
	s = "\n"
	for y in range(miny, maxy+1):
		row = ""
		for x in range(minx, maxx+1):
			row += "#" if (x, y) in p else " "
		s += row + "\n"
	return s


def get_range(p):
	ys = [x[1] for x in p]
	xs = [x[0] for x in p]
	return min(ys), max(ys), min(xs), max(xs)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

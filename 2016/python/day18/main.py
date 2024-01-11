from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return {"d": [x for x in open(filename).readline().strip()], "r": 40}


def count_safe_tiles(d):
	c = d["d"].count(".")
	r = d["d"]
	for i in range(d["r"]-1):
		new_row = ""
		for j in range(len(r)):
			tl, t, tr = '.' if j == 0 else r[j-1], r[j], '.' if j == len(r)-1 else r[j+1]
			new_row += ("^" if (tl == t == "^" and tr == ".") or (t == tr == "^" and tl == ".") or (t == tr == "." and tl == "^") or (t == tl == "." and tr == "^") else ".")
		r = new_row
		c += new_row.count(".")
	return c


def part_one(d):
	return count_safe_tiles(d)


def part_two(d):
	d["r"] = 400000
	return count_safe_tiles(d)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

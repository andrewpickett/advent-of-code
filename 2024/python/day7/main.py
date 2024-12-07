from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	ret_val = {"vals": {}, "valids": []}
	lines = [x.strip() for x in open(filename).readlines()]
	for line in lines:
		parts = line.split(":")
		ret_val["vals"][int(parts[0])] = [int(x) for x in parts[1].strip().split()]
	return ret_val


def part_one(d):
	c, valids = check_validity(d, 2)
	d["valids"] = valids
	d["total"] = c
	return c


def part_two(d):
	return d["total"] + check_validity(d, 3)[0]


def to_str(n, base):
	convert_string = "012"
	if n < base:
		return convert_string[n]
	else:
		return to_str(n // base, base) + convert_string[n % base]


def check_validity(d, ops):
	c = 0
	valids = set()
	for k, v in d["vals"].items():
		if k not in d["valids"]:
			nums = len(v) - 1
			valid = False
			for j in range(ops**nums):
				code = str(to_str(j, ops)).rjust(nums, "0")
				val = v[0]
				for i, x in enumerate(v[1:]):
					if code[i] == "0":
						val += x
					elif code[i] == "1":
						val *= x
					else:
						val = int(str(val) + str(x))
				if val == k:
					valid = True
					valids.add(k)
					break
			if valid:
				c += k
	return c, valids

def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

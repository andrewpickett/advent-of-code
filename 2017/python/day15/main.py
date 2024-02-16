from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return {"ab"[i]: int(x.strip().split()[-1]) for i, x in enumerate(open(filename).readlines())}


def gen(seed, multiplier, strict=None):
	while True:
		seed = (seed * multiplier) % 2147483647
		if not strict or seed % strict == 0:
			yield seed


def judge(d, r, strict=False):
	a_gen = gen(d["a"], 16807, 4 if strict else None)
	b_gen = gen(d["b"], 48271, 8 if strict else None)
	return sum(1 for i in range(r) if next(a_gen) & 0xffff == next(b_gen) & 0xffff)


def part_one(d):
	return judge(d, 40000000)


def part_two(d):
	return judge(d, 5000000, True)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

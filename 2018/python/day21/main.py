from utils.timers import run_with_timer, get_data_with_timer
from utils.opcode import OpCodeOperation


def get_data(filename):
	z = []
	lines = open(filename).readlines()
	for x in lines[1:]:
		y = x.strip().split()
		z.append([y[0], int(y[1]), int(y[2]), int(y[3])])
	return {"inst": z, "ip": int(lines[0].split()[-1])}


def part_one(d):
	r = [0, 0, 0, 0, 65536, 13431073]

	while True:
		r[3] = int(r[4] % 256)
		r[5] += r[3]
		r[5] = int((r[5] % 16777216 * 65899) % 16777216)
		if r[4] < 256:
			return r[5]
		r[4] /= 256


def part_two(d):
	r = [0, 0, 0, 0, 65536, 13431073]
	previously_seen = set()
	vals = set()
	last_val = None

	while True:
		r[3] = int(r[4] % 256)
		r[5] += r[3]
		r[5] = int((r[5] % 16777216 * 65899) % 16777216)
		if r[4] < 256:
			if r[5] not in vals:
				last_val = r[5]
			vals.add(r[5])
			r[4] = r[5] | 65536
			if r[4] in previously_seen:
				return last_val
			previously_seen.add(r[4])
			r[5] = 13431073
		else:
			r[4] /= 256


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

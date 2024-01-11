from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return open(filename).readline().strip()


def generate_data(a, disc_size):
	d = a
	while len(d) < disc_size:
		d = d + "0" + "{0:b}".format(int(d[::-1], 2) ^ int("1" * len(d), 2)).rjust(len(d), "0")
	return d[:disc_size]


def generate_checksum(s):
	checksum = s
	while len(checksum) % 2 == 0:
		new_checksum = ""
		for i in range(0, len(checksum), 2):
			new_checksum += "1" if checksum[i:i+2] in ["00", "11"] else "0"
		checksum = new_checksum
	return checksum


def part_one(d):
	return generate_checksum(generate_data(d, 272))


def part_two(d):
	return generate_checksum(generate_data(d, 35651584))


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

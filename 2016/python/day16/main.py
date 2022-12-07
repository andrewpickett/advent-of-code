from aoc_utils import run_with_timer

data = open("input.txt").readline().strip()


def generate_data(a, disc_size):
	d = a
	while len(d) < disc_size:
		d = d + "0" + d[::-1].replace("0", "2").replace("1", "0").replace("2", "1")
	return d[:disc_size]


def generate_checksum(s):
	checksum = s
	while len(checksum) % 2 == 0:
		new_checksum = ""
		for i in range(0, len(checksum), 2):
			new_checksum += "1" if checksum[i:i+2] in ["00", "11"] else "0"
		checksum = new_checksum
	return checksum


def part_one():
	return generate_checksum(generate_data(data, 272))


def part_two():
	return generate_checksum(generate_data(data, 35651584))


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

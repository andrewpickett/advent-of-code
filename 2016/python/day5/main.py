from aoc_utils import run_with_timer
import hashlib

data = open("input.txt").readline().strip()


def part_one():
	idx = 0
	password = ""
	while True:
		h = hashlib.md5((data + str(idx)).encode()).hexdigest()
		if h.startswith("00000"):
			password += h[5]
		if len(password) == 8:
			break
		idx += 1
	return password


def part_two():
	idx = 0
	password = ['_'] * 8
	while True:
		h = hashlib.md5((data + str(idx)).encode()).hexdigest()
		if h.startswith("00000"):
			pos = int(h[5], 16)
			if pos < len(password) and password[pos] == '_':
				password[pos] = h[6]
		if '_' not in password:
			break
		idx += 1
	return ''.join(password)


if __name__ == '__main__':
	run_with_timer(part_one)  # f97c354d -- took 12129 ms
	run_with_timer(part_two)  # 863dde27 -- took 41195 ms

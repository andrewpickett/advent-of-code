from utils.timers import run_with_timer, get_data_with_timer
import hashlib


def get_data(filename):
	return open(filename).readline().strip()


def part_one(d):
	i = 0
	password = ""
	while len(password) < 8:
		h = hashlib.md5((d + str(i)).encode()).hexdigest()
		if h[:5] == "00000":
			password += h[5]
		i += 1
	return password


def part_two(d):
	i = 0
	password = ['_'] * 8
	while '_' in password:
		h = hashlib.md5((d + str(i)).encode()).hexdigest()
		if h[:5] == "00000":
			pos = int(h[5], 16)
			if pos < len(password) and password[pos] == '_':
				password[pos] = h[6]
		i += 1
	return ''.join(password)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

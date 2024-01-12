from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return {"d": [x.strip() for x in open(filename).readlines()], "k": "abcdefgh", "r": "fbgdceah"}


def swap(password, i, j):
	tmp = password[i]
	password[i] = password[j]
	password[j] = tmp


def rotate(password, direction, amt):
	v = (direction * amt) % len(password)
	return password[v:] + password[:v]


def part_one(d):
	password = list(d["k"])
	for x in d["d"]:
		password = perform_action(password, x)
	return ''.join(password)


rotation_lookup = [1, 1, 6, 2, 7, 3, 0, 4]


def perform_action(password, x, reverse=False):
	parts = x.split()
	if x.startswith("swap position"):
		swap(password, int(parts[2]), int(parts[5]))
	elif x.startswith("swap letter"):
		swap(password, password.index(parts[2]), password.index(parts[5]))
	elif x.startswith("rotate based on"):
		v = password.index(parts[6])
		if reverse:
			#  TODO...make this not specific to size 8 inputs...
			password = rotate(password, 1, rotation_lookup[v])
		else:
			password = rotate(password, -1, 1+v if v < 4 else 2+v)
	elif x.startswith("rotate"):
		password = rotate(password, (1 if parts[1] == "left" else -1)*(-1 if reverse else 1), int(parts[2]))
	elif x.startswith("reverse"):
		s = int(parts[2])
		e = int(parts[4])
		password = password[:s] + list(reversed(password[s:e+1])) + password[e+1:]
	elif x.startswith("move"):
		if reverse:
			password.insert(int(parts[2]), password.pop(int(parts[5])))
		else:
			password.insert(int(parts[5]), password.pop(int(parts[2])))
	return password


def part_two(d):
	password = list(d["r"])
	for x in d["d"][::-1]:
		password = perform_action(password, x, True)
	return ''.join(password)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

from collections import defaultdict

from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [int(x.strip()) for x in open(filename).readlines()]


def part_one(d):
	secrets = defaultdict(int)
	for x in d:
		calc_secret(x, secrets)
	return sum(x for x in secrets.values())


def calc_secret(x, secrets):
	last = x % 10
	pattern = []
	i = x
	for _ in range(2000):
		i = ((i*64) ^ i) % 16777216
		i = ((i // 32) ^ i) % 16777216
		i = ((i * 2048) ^ i) % 16777216
		temp = i % 10
		pattern.append((temp - last, temp))
		last = temp
	secrets[x] = i
	return pattern


def part_two(d):
	secrets = defaultdict(int)
	for x in d:
		pattern = calc_secret(x, {})
		seen = set()
		for i in range(len(pattern)-4):
			pat = tuple(x[0] for x in pattern[i:i+4])
			val = pattern[i+3][1]
			if pat not in seen:
				seen.add(pat)
				secrets[pat] += val
	return max(secrets.values())


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

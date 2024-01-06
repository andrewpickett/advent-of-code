from utils.timers import run_with_timer, get_data_with_timer
import re


def get_data(filename):
	return [re.split('[\[\]\-]', x.strip())[:-1] for x in open(filename).readlines()]


def get_character_counts(d):
	counts = {}
	for x in d:
		if x != "-":
			if x not in counts.keys():
				counts[x] = 0
			counts[x] = counts[x] + 1
	return dict(sorted(counts.items(), key=lambda item: item[1]))


def calculate_checksum(counts):
	count_str = [''] * max(counts.values())
	for k, v in counts.items():
		count_str[v-1] += k
	for i, x in enumerate(count_str):
		count_str[i] = sorted(x)
	fstr = ""
	for x in reversed(count_str):
		fstr += ''.join(x)
	return fstr[0:5]


def part_one(d):
	return sum(int(x[-2]) for x in d if x[-1] == calculate_checksum(get_character_counts(''.join(x[:-2]))))


def part_two(d):
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	target = "northpole"
	for x in d:
		for y in x[:-2]:
			if len(y) == len(target):
				sector = int(x[-2])
				name = ''.join(list(map(lambda z: alpha[(alpha.index(z) + sector) % 26], y)))
				if name == target:
					return sector


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

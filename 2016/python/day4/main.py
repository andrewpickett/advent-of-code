from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def get_character_counts(d):
	counts = {}
	for x in d:
		if x != '-':
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


def part_one():
	total = 0
	for x in data:
		name = x[0:x.index("[")]
		sector = int(name[name.rindex("-")+1:])
		name = name[0:name.rindex("-")]
		checksum = x[x.index("[")+1:-1]

		if checksum == calculate_checksum(get_character_counts(name)):
			total += sector
	return total


def part_two():
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	total = 0
	for x in data:
		name = x[0:x.index("[")]
		sector = int(name[name.rindex("-")+1:])
		shift = sector % 26
		name = name[0:name.rindex("-")]
		checksum = x[x.index("[")+1:-1]

		if checksum == calculate_checksum(get_character_counts(name)):
			real_name = ""
			for i, y in enumerate(name):
				if y != '-':
					real_name += alpha[(alpha.index(y) + shift) % 26]
				else:
					real_name += " "
			if "northpole" in real_name:
				return sector


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

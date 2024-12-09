from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	vals = list(map(int, list(open(filename).readline().strip())))
	blocks = []
	identifier = 0
	for i, x in enumerate(vals):
		if i % 2 == 0:
			blocks.append((identifier, x, False))
		else:
			identifier += 1
			blocks.append((".", x, False))
	return blocks


def part_one(d):
	curr_pos = -1
	min_idx = 1
	while len(d) + curr_pos > 1:
		min_idx, curr_pos = move_blocks(d, curr_pos, min_idx, True, 0)
		curr_pos -= 1
	return get_checksum(d)


def part_two(d):
	curr_pos = -1
	min_idx = 1
	while len(d) + curr_pos > 1:
		min_idx, _ = move_blocks(d, curr_pos, min_idx, False, d[curr_pos][1]-1)
		curr_pos -= 1
	return get_checksum(d)


def move_blocks(d, curr_pos, min_idx, p1, s):
	cur_block = d[curr_pos]
	if cur_block[0] != "." and not cur_block[2]:
		for y in range(min_idx, len(d) + curr_pos):
			if d[y][0] == "." and d[y][1] > s:
				if not p1:
					d[y] = (d[y][0], d[y][1] - cur_block[1], d[y][2])
					d.insert(y, (cur_block[0], cur_block[1], True))
					d[curr_pos] = (".", cur_block[1], False)
					for i in range(min_idx, len(d)+curr_pos):
						if d[i][0] == "." and d[i][1] > 0:
							return i, curr_pos
				else:
					if d[y][1] >= cur_block[1]:
						if d[y][1] == cur_block[1]:
							d.pop(y)
						else:
							d[y] = (d[y][0], d[y][1] - cur_block[1], d[y][2])
						d.insert(y, (cur_block[0], cur_block[1], True))
						d[curr_pos] = (".", cur_block[1], False)
					else:
						d[y] = (d[curr_pos][0], d[y][1], True)
						d[curr_pos] = (d[curr_pos][0], d[curr_pos][1] - d[y][1], d[curr_pos][2])
						curr_pos += 1
					return y + 1, curr_pos
				break
	return min_idx, curr_pos


def get_checksum(d):
	s = 0
	counter = 0
	for i, x in enumerate(d):
		for j in range(x[1]):
			s += (0 if x[0] == "." else x[0]) * counter
			counter += 1
	return s


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data.copy())
	run_with_timer(part_two, data.copy())


if __name__ == '__main__':
	main()

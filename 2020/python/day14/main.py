from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def apply_mask(binary_string, repls, c):
	ret_val = binary_string
	for x in repls:
		ret_val = ret_val[:x] + c + ret_val[x+1:]
	return ret_val


def part_one():
	mem_addresses = {}
	zeros = []
	ones = []
	for datum in data:
		if 'mask' in datum:
			bitmask = datum.split(' = ')[1]
			zeros = [i for i, letter in enumerate(bitmask) if letter == '0']
			ones = [i for i, letter in enumerate(bitmask) if letter == '1']
		else:
			parts = datum.split(' = ')
			binary_string = f'{int(parts[1]):036b}'
			binary_string = apply_mask(binary_string, ones, '1')
			binary_string = apply_mask(binary_string, zeros, '0')
			mem_addresses[parts[0]] = int(binary_string, 2)
	return sum(mem_addresses[x] for x in mem_addresses.keys())


def part_two():
	mem_addresses = {}
	ones = []
	floating = []
	for datum in data:
		if 'mask' in datum:
			bitmask = datum.split(' = ')[1]
			ones = [i for i, letter in enumerate(bitmask) if letter == '1']
			floating = [i for i, letter in enumerate(bitmask) if letter == 'X']
		else:
			parts = datum.split(' = ')
			binary_string = f'{int(parts[0][4:-1]):036b}'
			binary_string = apply_mask(binary_string, ones, '1')
			binary_string = apply_mask(binary_string, floating, 'X')

			for i in range(2**len(floating)):
				next_repl = binary_string
				binary_subs = ('{0:0' + str(len(floating)) + 'b}').format(i)
				for j in binary_subs:
					next_repl = next_repl.replace('X', j, 1)
				mem_addresses[int(next_repl, 2)] = int(parts[1])
	return sum(mem_addresses[x] for x in mem_addresses.keys())


if __name__ == '__main__':
	run_with_timer(part_one)  # 15919415426101 -- took 6 ms
	run_with_timer(part_two)  # 3443997590975 -- took 198 ms

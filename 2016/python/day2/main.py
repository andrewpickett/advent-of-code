from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


keypad1 = [
	['1', '2', '3'],
	['4', '5', '6'],
	['7', '8', '9']
]
keypad2 = [
	[' ', ' ', '1', ' ', ' '],
	[' ', '2', '3', '4', ' '],
	['5', '6', '7', '8', '9'],
	[' ', 'A', 'B', 'C', ' '],
	[' ', ' ', 'D', ' ', ' ']
]


def get_code_digit(keypad, line, start_point):
	r = start_point[0]
	c = start_point[1]
	for y in line:
		match y:
			case 'U':
				r = r - 1 if r > 0 and keypad[r-1][c] != ' ' else r
			case 'D':
				r = r + 1 if r < len(keypad)-1 and keypad[r+1][c] != ' ' else r
			case 'L':
				c = c - 1 if c > 0 and keypad[r][c-1] != ' ' else c
			case 'R':
				c = c + 1 if c < len(keypad)-1 and keypad[r][c+1] != ' ' else c
	return keypad[r][c], (r, c)


def get_code(d, start_pos, keypad):
	curr_pos = start_pos
	code = ""
	for x in d:
		digit, curr_pos = get_code_digit(keypad, x, curr_pos)
		code += digit
	return code


def part_one(d):
	return get_code(d, (1, 1), keypad1)


def part_two(d):
	return get_code(d, (2, 0), keypad2)


if __name__ == '__main__':
	data = get_data_with_timer(get_data, "input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

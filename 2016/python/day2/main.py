from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]

keypad1 = [
	['1', '2', '3'],
	['4', '5', '6'],
	['7', '8', '9']
]
keypad2 = [
	['0', '0', '1', '0', '0'],
	['0', '2', '3', '4', '0'],
	['5', '6', '7', '8', '9'],
	['0', 'A', 'B', 'C', '0'],
	['0', '0', 'D', '0', '0']
]


def get_code_digit(keypad, line, start_point):
	curr_row = start_point[0]
	curr_col = start_point[1]
	for y in line:
		match y:
			case 'U':
				curr_row = curr_row - 1 if curr_row > 0 and keypad[curr_row-1][curr_col] != '0' else curr_row
			case 'D':
				curr_row = curr_row + 1 if curr_row < len(keypad)-1 and keypad[curr_row+1][curr_col] != '0' else curr_row
			case 'L':
				curr_col = curr_col - 1 if curr_col > 0 and keypad[curr_row][curr_col-1] != '0' else curr_col
			case 'R':
				curr_col = curr_col + 1 if curr_col < len(keypad)-1 and keypad[curr_row][curr_col+1] != '0' else curr_col
	return keypad[curr_row][curr_col], (curr_row, curr_col)


def part_one():
	curr_pos = (1, 1)
	code = ""
	for x in data:
		digit, curr_pos = get_code_digit(keypad1, x, curr_pos)
		code += digit
	return code


def part_two():
	curr_pos = (2, 0)
	code = ""
	for x in data:
		digit, curr_pos = get_code_digit(keypad2, x, curr_pos)
		code += digit
	return code


if __name__ == '__main__':
	run_with_timer(part_one)  # 84452 -- took 0 ms
	run_with_timer(part_two)  # D65C3 -- took 0 ms

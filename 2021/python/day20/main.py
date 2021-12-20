from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]

algo = data[0]
in_val = [list(x) for x in data[2:]]


def extend_board(board):
	for x in board:
		for _ in range(3):
			x.insert(0, ".")
			x.append(".")
	for _ in range(3):
		board.insert(0, [])
		for i in range(len(board[1])):
			board[0].append(".")
		board.append([])
		for i in range(len(board[1])):
			board[-1].append(".")


def enhance(b):
	new_board = [list("."*len(b[0]))]
	for i in range(1, len(b) - 1):
		new_row = ["."]
		for j in range(1, len(b[i]) - 1):
			# bin_str = ''.join(b[i-1][j-1:j+1]) + ''.join(b[i][j-1:j+1]) + ''.join(b[i+1][j-1:j+1])
			bin_str = b[i-1][j-1] + b[i-1][j] + b[i-1][j+1] + b[i][j-1] + b[i][j] + b[i][j+1] + b[i+1][j-1] + b[i+1][j] + b[i+1][j+1]
			new_pixel = algo[int(bin_str.replace(".", "0").replace("#", "1"), 2)]
			# print("bin_str", i, j, bin_str, int(bin_str.replace(".", "0").replace("#", "1"), 2), new_pixel)
			new_row.append(new_pixel)
		new_row.append(".")
		new_board.append(new_row)
	return new_board


def part_one():
	extend_board(in_val)
	new_board = enhance(in_val)
	extend_board(new_board)
	final_board = enhance(new_board)
	for x in final_board:
		print(''.join(x))
	total_lit = sum(x.count("#") for x in final_board)
	return total_lit


def part_two():
	new_board = in_val
	for _ in range(50):
		extend_board(new_board)
		new_board = enhance(new_board)

	return sum(x.count("#") for x in new_board)


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #
# 7680 not right
# 6000 not right

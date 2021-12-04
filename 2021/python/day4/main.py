import math

from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]
called_nums = data[0].split(",")


def create_boards():
	bs = []
	b = []
	for line in data[2:]:
		if len(line) <= 1:
			bs.append(b)
			b = []
		else:
			b.extend(line.split())
	bs.append(b)
	return bs


def check_for_win(board, size):
	for row in range(len(board) // size):
		if board[row*size] == 'x' and board[row*size+1] == 'x' and board[row*size+2] == 'x' and board[row*size+3] == 'x' and board[row*size+4] == 'x':
			return True
		if board[row] == 'x' and board[row+size*1] == 'x' and board[row+size*2] == 'x' and board[row+size*3] == 'x' and board[row+size*4] == 'x':
			return True
	return False


def mark_boards(boards, val):
	winning_board = False
	boards_to_remove = []
	for i, board in enumerate(boards):
		if val in board:
			board[board.index(val)] = 'x'
			if check_for_win(board, int(math.sqrt(len(board)))):
				boards_to_remove.append(i)
				if not winning_board:
					winning_board = board
	new_boards = []
	for i in range(len(boards)):
		if i not in boards_to_remove:
			new_boards.append(boards[i])
	boards.clear()
	boards.extend(new_boards)
	return winning_board


def part_one():
	boards = create_boards()
	for called_num in called_nums:
		winning_board = mark_boards(boards, called_num)
		if winning_board:
			return sum(int(square) for square in winning_board if square != 'x') * int(called_num)


def part_two():
	boards = create_boards()
	for called_num in called_nums:
		winning_board = mark_boards(boards, called_num)
		if winning_board:
			if len(boards) == 0:
				return sum(int(square) for square in winning_board if square != 'x') * int(called_num)


if __name__ == '__main__':
	run_with_timer(part_one)  # 41503 -- took 2 ms
	run_with_timer(part_two)  # 3178 -- took 6 ms

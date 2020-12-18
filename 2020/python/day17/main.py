from aoc_utils import run_with_timer

data = [y for y in [x.strip() for x in open("input.txt").readlines()]]


def get_active_neighbor_count(board, p):
	is4d = len(p) == 4
	count = 0
	for x in (-1, 0, 1):
		if 0 <= p[0]+x < len(board):
			for y in (-1, 0, 1):
				if 0 <= p[1]+y < len(board[0]):
					for z in (-1, 0, 1):
						if 0 <= p[2]+z < len(board[0][0]):
							if is4d:
								for w in (-1, 0, 1):
									if (x, y, z, w) != (0, 0, 0, 0) and 0 <= p[3]+w < len(board[0][0][0]):
										if board[p[0] + x][p[1] + y][p[2] + z][p[3] + w] == '#':
											count += 1
							else:
								if (x, y, z) != (0, 0, 0) and board[p[0] + x][p[1] + y][p[2] + z] == '#':
									count += 1
	return count


def run_cycle(board, is4d):
	points_to_swap = []
	for x in range(len(board)):
		for y in range(len(board[x])):
			for z in range(len(board[x][y])):
				if is4d:
					for w in range(len(board[x][y][z])):
						cnt = get_active_neighbor_count(board, (x, y, z, w))
						if board[x][y][z][w] == '.' and cnt == 3:
							points_to_swap.append((x, y, z, w))
						elif board[x][y][z][w] == '#' and cnt not in (2, 3):
							points_to_swap.append((x, y, z, w))
				else:
					cnt = get_active_neighbor_count(board, (x, y, z))
					if board[x][y][z] == '.' and cnt == 3:
						points_to_swap.append((x, y, z))
					elif board[x][y][z] == '#' and cnt not in (2, 3):
						points_to_swap.append((x, y, z))
	for p in points_to_swap:
		if is4d:
			board[p[0]][p[1]][p[2]][p[3]] = '#' if board[p[0]][p[1]][p[2]][p[3]] == '.' else '.'
		else:
			board[p[0]][p[1]][p[2]] = '#' if board[p[0]][p[1]][p[2]] == '.' else '.'
	return board


def count_active(board, is4d):
	return sum((sum((y.count('#') if not is4d else sum(z.count('#') for z in y)) for y in x)) for x in board)


def initialize_board(steps, is4d):
	size = 2*steps
	if is4d:
		board = [[[['.' for k in range(len(data)+size)] for j in range(len(data)+size)] for i in range(len(data)+size)] for l in range(len(data)+size)]
		initial_point = (steps+1, steps+1, steps+1, steps+1)
	else:
		board = [[['.' for k in range(len(data)+size)] for j in range(len(data)+size)] for i in range(len(data)+size)]
		initial_point = (steps+1, steps+1, steps+1)

	depth = initial_point[2]
	for x in range(len(data)):
		for y in range(len(data[0])):
			if is4d:
				board[initial_point[0] + x][initial_point[1] + y][depth][depth] = data[x][y]
			else:
				board[initial_point[0] + x][initial_point[1] + y][depth] = data[x][y]
	return board


def part_one():
	steps = 6
	board = initialize_board(steps, False)

	for i in range(steps):
		board = run_cycle(board, False)
	return count_active(board, False)


def part_two():
	steps = 6
	board = initialize_board(steps, True)

	for i in range(steps):
		board = run_cycle(board, True)
	return count_active(board, True)


if __name__ == '__main__':
	run_with_timer(part_one)  # 384 -- took 744 ms
	run_with_timer(part_two)  # 2012 -- took 45906 ms

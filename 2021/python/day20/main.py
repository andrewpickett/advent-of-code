from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]

algo = data[0]
in_val = [list(x) for x in data[2:]]


def extend_board(board, fill_pattern):
    extension = 2
    for x in board:
        for _ in range(extension):
            x.insert(0, fill_pattern)
            x.append(fill_pattern)
    for _ in range(extension):
        board.insert(0, [fill_pattern]*len(board[1]))
        board.append([fill_pattern]*len(board[1]))


def enhance(b):
    new_board = []
    for row in range(1, len(b) - 1):
        new_row = []
        for col in range(1, len(b[row]) - 1):
            bin_str = b[row-1][col-1] + b[row-1][col] + b[row-1][col+1] + b[row][col-1] + b[row][col] + b[row][col+1] + b[row+1][col-1] + b[row+1][col] + b[row+1][col+1]
            new_pixel = algo[int(bin_str.replace(".", "0").replace("#", "1"), 2)]
            new_row.append(new_pixel)
        new_board.append(new_row)
    return new_board


def run_steps(board, n):
    for i in range(n):
        extend_board(board, "." if i % 2 == 0 or algo[0] == "." else "#")
        board = enhance(board)
    return board


def part_one():
    return sum(x.count("#") for x in run_steps(in_val, 2))


def part_two():
    return sum(x.count("#") for x in run_steps(in_val, 50))


if __name__ == '__main__':
    run_with_timer(part_one)  # 5432 -- took 33 ms
    run_with_timer(part_two)  # 16016 -- took 2010 ms

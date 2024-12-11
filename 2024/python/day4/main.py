from utils.timers import run_with_timer, get_data_with_timer
from utils.input import read_input_as_2d_str_grid


def get_data(filename):
	return read_input_as_2d_str_grid(filename, pad_size=3, pad_val=".")


def part_one(d):
	return sum(get_vals(d, i, j).count("XMAS") for i in range(len(d)) for j in range(len(d[i])) if d[i][j] == "X")


def get_vals(d, i, j):
	return [
		d[i][j] + d[i-1][j-1] + d[i-2][j-2] + d[i-3][j-3],
		d[i][j] + d[i-1][j] + d[i-2][j] + d[i-3][j],
		d[i][j] + d[i-1][j+1] + d[i-2][j+2] + d[i-3][j+3],
		d[i][j] + d[i][j-1] + d[i][j-2] + d[i][j-3],
		''.join(d[i][j:j+4]),
		d[i][j] + d[i+1][j-1] + d[i+2][j-2] + d[i+3][j-3],
		d[i][j] + d[i+1][j] + d[i+2][j] + d[i+3][j],
		d[i][j] + d[i+1][j+1] + d[i+2][j+2] + d[i+3][j+3]
	]


def part_two(d):
	return sum(1 for i in range(4, len(d)-4) for j in range(4, len(d[i])-4) if d[i][j] == "A" and get_square(d, i, j))


def get_square(d, i, j):
	vals = [
		d[i-1][j-1] + d[i][j] + d[i+1][j+1],
		d[i-1][j+1] + d[i][j] + d[i+1][j-1],
		d[i+1][j-1] + d[i][j] + d[i-1][j+1],
		d[i+1][j+1] + d[i][j] + d[i-1][j-1]]
	return vals.count("MAS") == 2


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

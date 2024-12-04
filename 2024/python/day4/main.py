from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def part_one(d):
	return sum(get_vals(d, i, j).count("XMAS") for i in range(len(d)) for j in range(len(d[i])) if d[i][j] == "X")


def get_vals(d, i, j):
	vals = []
	if i > 2 and j > 2:
		vals.append(d[i][j] + d[i-1][j-1] + d[i-2][j-2] + d[i-3][j-3])
	if i > 2:
		vals.append(d[i][j] + d[i-1][j] + d[i-2][j] + d[i-3][j])
	if i > 2 and j < len(d[i]) - 3:
		vals.append(d[i][j] + d[i-1][j+1] + d[i-2][j+2] + d[i-3][j+3])
	if j > 2:
		vals.append(d[i][j] + d[i][j-1] + d[i][j-2] + d[i][j-3])
	if j < len(d[i]) - 3:
		vals.append(d[i][j:j+4])
	if i < len(d) - 3 and j > 2:
		vals.append(d[i][j] + d[i+1][j-1] + d[i+2][j-2] + d[i+3][j-3])
	if i < len(d) - 3:
		vals.append(d[i][j] + d[i+1][j] + d[i+2][j] + d[i+3][j])
	if i < len(d) - 3 and j < len(d[i]) - 3:
		vals.append(d[i][j] + d[i+1][j+1] + d[i+2][j+2] + d[i+3][j+3])
	return vals


def part_two(d):
	return sum(1 for i in range(1, len(d)-1) for j in range(1, len(d[i])-1) if d[i][j] == "A" and get_square(d, i, j))


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

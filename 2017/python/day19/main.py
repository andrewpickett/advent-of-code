from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid


def get_data(filename):
	lines = [x[:-1] for x in open(filename).readlines()]
	m = max(len(x) for x in lines)
	lines = map(lambda x: x.ljust(m), lines)
	g = Grid(values=[list(line) for line in lines])
	g.set_neighbors_for_all()
	return g


def traverse(d):
	curr_pos = [x for x in d.get_row(0) if x.value != " "][0]
	path = [curr_pos, curr_pos]
	letters = []
	valid_moves = True
	last_dir = curr_pos.value
	while valid_moves:
		if curr_pos.value not in ["+", "-", "|"] and curr_pos.value not in letters:
			letters.append(curr_pos.value)
		possible_next_moves = [x for x in curr_pos.get_neighbors() if x.value != " " and x != path[-2]]
		if curr_pos.value == "+":
			last_dir = "|" if last_dir == "-" else "-"

		if len(possible_next_moves) == 1:
			curr_pos = possible_next_moves[0]
			path.append(curr_pos)
		else:
			logical_next = [x for x in possible_next_moves if x.value == last_dir and x ]
			if len(logical_next) == 1:
				curr_pos = logical_next[0]
				path.append(curr_pos)
			else:
				p = d.get_point(curr_pos.row + (curr_pos.row - path[-2].row), curr_pos.col + (curr_pos.col - path[-2].col))
				if p in possible_next_moves:
					curr_pos = p
					path.append(curr_pos)
				else:
					valid_moves = False
	return letters, path[1:]


def part_one(d):
	return ''.join(traverse(d)[0])


def part_two(d):
	return len(traverse(d)[1])


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def calc_tree_count(vert, horiz):
	curr_pos = (0, 0)
	tree_count = 0
	while curr_pos[0] < len(data):
		tree_count = tree_count + 1 if data[curr_pos[0]][curr_pos[1]] == '#' else tree_count
		curr_pos = (curr_pos[0] + vert, (curr_pos[1] + horiz) % len(data[0]))
	return tree_count


def part_one():
	return calc_tree_count(1, 3)


def part_two():
	return calc_tree_count(1, 1) * calc_tree_count(1, 3) * calc_tree_count(1, 5) * calc_tree_count(1, 7) * calc_tree_count(2, 1)


if __name__ == '__main__':
	run_with_timer(part_one)  # 250 -- took 1 ms
	run_with_timer(part_two)  # 1592662500 -- took 1 ms

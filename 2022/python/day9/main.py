from aoc_utils import run_with_timer

data = [x.strip().split(" ") for x in open("input.txt").readlines()]

movements = {
	"U": (0, 1),
	"D": (0, -1),
	"L": (-1, 0),
	"R": (1, 0)
}


def get_new_tail_pos(prev_head_pos, head_pos, tail_pos):
	# Cases we don't have to move our tail
	if head_pos == tail_pos or (abs(head_pos[0] - tail_pos[0]) == 1 and abs(head_pos[1] - tail_pos[1]) == 1):
		return tail_pos

	# X movement
	if head_pos[1] == tail_pos[1]:
		if head_pos[0] - tail_pos[0] > 1:
			return head_pos[0] - 1, head_pos[1], tail_pos[2]
		elif head_pos[0] - tail_pos[0] < -1:
			return head_pos[0] + 1, head_pos[1], tail_pos[2]
		return tail_pos

	if head_pos[0] == tail_pos[0]:
		if head_pos[1] - tail_pos[1] > 1:
			return head_pos[0], head_pos[1] - 1, tail_pos[2]
		elif head_pos[1] - tail_pos[1] < -1:
			return head_pos[0], head_pos[1] + 1, tail_pos[2]
		return tail_pos

	# Diagonal movement
	if abs(head_pos[0] - prev_head_pos[0]) > 0 and abs(head_pos[1] - prev_head_pos[1]) > 0:
		return tail_pos[0] + (head_pos[0] - prev_head_pos[0]), tail_pos[1] + head_pos[1] - prev_head_pos[1], tail_pos[2]

	return prev_head_pos[0], prev_head_pos[1], tail_pos[2]


def run(length):
	visited_tail_pos = set()
	knot_positions = [(0, 0, "H" if x == 0 else str(x)) for x in range(length)]

	for x in data:
		for y in range(int(x[1])):
			prev_pos = knot_positions[0]
			knot_positions[0] = (knot_positions[0][0] + movements[x[0]][0], knot_positions[0][1] + movements[x[0]][1], knot_positions[0][2])
			for z in range(1, len(knot_positions)):
				next_pos = get_new_tail_pos(prev_pos, knot_positions[z-1], knot_positions[z])
				prev_pos = knot_positions[z]
				knot_positions[z] = (next_pos[0], next_pos[1], next_pos[2])
				if z == len(knot_positions) - 1:
					visited_tail_pos.add(knot_positions[z])
	return visited_tail_pos


def part_one():
	return len(run(2))


def part_two():
	return len(run(10))


if __name__ == '__main__':
	run_with_timer(part_one)  # 6256
	run_with_timer(part_two)  # 2665

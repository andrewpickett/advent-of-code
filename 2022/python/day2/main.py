from aoc_utils import run_with_timer

data = [x.strip().split(" ") for x in open("input.txt").readlines()]

outcome_map = {"X": {"A": "Z", "B": "X", "C": "Y"}, "Y": {"A": "X", "B": "Y", "C": "Z"}, "Z": {"A": "Y", "B": "Z", "C": "X"}}


def calc_hand_score(them, me):
	score = 3 if me == 'Z' else (2 if me == 'Y' else 1)
	if (them == 'A' and me == 'Y') or (them == 'B' and me == 'Z') or (them == 'C' and me == 'X'):
		score += 6
	elif (them == 'A' and me == 'X') or (them == 'B' and me == 'Y') or (them == 'C' and me == 'Z'):
		score += 3
	return score


def part_one():
	return sum(calc_hand_score(x[0], x[1]) for x in data)


def part_two():
	return sum(calc_hand_score(x[0], outcome_map[x[1]][x[0]]) for x in data)


if __name__ == '__main__':
	run_with_timer(part_one)  # 14264 -- took 0 ms
	run_with_timer(part_two)  # 12382 -- took 0 ms

# 2   00:07:46  1614      0   00:11:12  1133      0

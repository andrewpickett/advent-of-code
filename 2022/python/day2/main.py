from aoc_utils import run_with_timer

data = [x.strip().split(" ") for x in open("input.txt").readlines()]

outcome_map = {"X": {"A": "Z", "B": "X", "C": "Y"}, "Y": {"A": "X", "B": "Y", "C": "Z"}, "Z": {"A": "Y", "B": "Z", "C": "X"}}


def calc_hand_score(them, me):
	hand = them + me
	score = 3 if me == 'Z' else (2 if me == 'Y' else 1)
	if hand == 'AY' or hand == 'BZ' or hand == 'CX':
		score += 6
	elif hand == 'AX' or hand == 'BY' or hand == 'CZ':
		score += 3
	return score


def part_one():
	return sum(calc_hand_score(x[0], x[1]) for x in data)


def part_two():
	return sum(calc_hand_score(x[0], outcome_map[x[1]][x[0]]) for x in data)


if __name__ == '__main__':
	run_with_timer(part_one)  # 14264 -- took 0 ms
	run_with_timer(part_two)  # 12382 -- took 0 ms

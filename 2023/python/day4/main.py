from utils.timers import run_with_timer
import math


def get_data(filename):
	return [x[x.find(":")+1:].strip() for x in open(filename).readlines()]


def get_winners(card):
	parts = card.strip().split("|")
	winners = set([x for x in parts[0].strip().split(" ") if x != ""])
	mine = set([x for x in parts[1].strip().split(" ") if x != ""])
	return len(mine.intersection(winners))


def part_one(d):
	s = 0
	for card in d:
		num_win = get_winners(card)
		if num_win > 0:
			s += int(math.pow(2, num_win-1))
	return s


def part_two(d):
	all_cards = [1] * len(d)
	for i, card in enumerate(d):
		num_win = get_winners(card)
		for j in range(num_win):
			all_cards[i+j+1] += all_cards[i]
	return sum(all_cards)


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

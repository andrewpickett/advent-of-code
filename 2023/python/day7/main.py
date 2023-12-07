from utils.timers import run_with_timer
from functools import cmp_to_key


def get_data(filename):
	return [x.strip().split() for x in open(filename).readlines()]


hand_types = [[1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1], [5]]


def rank_hands(hands, cards):
	hand_type_map = [[] for _ in range(len(hand_types))]
	for k, v in hands.items():
		hand_type_map[v["type"]].append(v)
	hand_type_map = map(lambda z: sorted(z, key=cmp_to_key(lambda x, y: hand_comparator(x, y, cards))), hand_type_map)
	all_ranked_hands = []
	for ht in hand_type_map:
		if len(ht) > 0:
			all_ranked_hands.extend([x for x in ht])
	return all_ranked_hands


def hand_comparator(h1, h2, cards):
	for i in range(len(h1["cards"])):
		if cards.find(h1["cards"][i]) < cards.find(h2["cards"][i]):
			return 1
		elif cards.find(h1["cards"][i]) > cards.find(h2["cards"][i]):
			return -1
	return 0


def part_one(d):
	hands = {}
	for hand in d:
		cs = {c: hand[0].count(c) for c in set(hand[0])}
		hand_type = (list(reversed(sorted(cs.values()))))
		hands[hand[0]] = {"cards": hand[0], "bid": int(hand[1]), "type": hand_types.index(hand_type)}
	return sum((i+1)*hand["bid"] for i, hand in enumerate(rank_hands(hands, "AKQJT98765432")))


def part_two(d):
	hands = {}
	for hand in d:
		cs = {c: hand[0].count(c) for c in set(hand[0])}
		jokers = 0 if "J" not in cs or cs["J"] == 5 else cs.pop("J")
		if 0 < jokers < 5:
			cs[max(cs, key=cs.get)] += jokers
		hand_type = (list(reversed(sorted(cs.values()))))
		hands[hand[0]] = {"cards": hand[0], "bid": int(hand[1]), "type": hand_types.index(hand_type)}
	return sum((i+1)*hand["bid"] for i, hand in enumerate(rank_hands(hands, "AKQT98765432J")))


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def get_decks():
	return [int(x) for x in data[1:data.index('')]], [int(x) for x in data[data.index('')+2:]]


def part_one():
	player1, player2 = get_decks()
	while len(player1) > 0 and len(player2) > 0:
		one_card = player1.pop(0)
		two_card = player2.pop(0)

		if one_card > two_card:
			player1.append(one_card)
			player1.append(two_card)
		else:
			player2.append(two_card)
			player2.append(one_card)
	winning_hand = player1 if len(player1) > 0 else player2
	return sum(i*winning_hand[-i] for i in range(1, len(winning_hand)+1))


def play_round(player1, player2, game_num):
	one_card = player1.pop(0)
	two_card = player2.pop(0)
	if one_card <= len(player1) and two_card <= len(player2):
		sub_winner = play_game(player1[:one_card].copy(), player2[:two_card].copy(), game_num+1)
		if sub_winner == 1:
			player1.append(one_card)
			player1.append(two_card)
		else:
			player2.append(two_card)
			player2.append(one_card)
	else:
		if one_card > two_card:
			player1.append(one_card)
			player1.append(two_card)
		else:
			player2.append(two_card)
			player2.append(one_card)
	return False


def play_game(player1, player2, game_num):
	round_num = 0
	game_hands = []
	while len(player1) > 0 and len(player2) > 0:
		round_num += 1
		if (player1, player2) in game_hands:
			return 1
		game_hands.append((player1.copy(), player2.copy()))
		play_round(player1, player2, game_num)
	return 1 if len(player1) > 0 else 2


def part_two():
	player1, player2 = get_decks()

	winner = play_game(player1, player2, 1)

	winning_hand = player1 if winner == 1 else player2
	return sum(i*winning_hand[-i] for i in range(1, len(winning_hand)+1))


if __name__ == '__main__':
	run_with_timer(part_one)  # 33434 -- took 0 ms
	run_with_timer(part_two)  # 31657 -- took 24304 ms

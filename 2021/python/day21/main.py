# from aoc_utils import run_with_timer
#
# data = [int(x.split(": ")[1]) for x in open("input.txt").readlines()]
#
#
# def deterministic_die(state):
# 	roll_val = 3 * state["die"] + 3
# 	state["die"] = ((state["die"] + 2) % 100) + 1
# 	return roll_val
#
#
# def make_move(state, die_func):
# 	player = state["p1"] if state["turn"] % 2 == 1 else state["p2"]
# 	player["pos"] = ((player["pos"] + die_func(state) - 1) % 10) + 1
# 	player["score"] += player["pos"]
# 	state["turn"] += 1
#
#
# def part_one():
# 	state = {"die": 1, "turn": 1, "p1": {"num": 1, "score": 0, "pos": data[0]}, "p2": {"num": 2, "score": 0, "pos": data[1]}}
# 	while state["p1"]["score"] < 1000 and state["p2"]["score"] < 1000:
# 		make_move(state, deterministic_die)
# 	return min(state["p1"]["score"], state["p2"]["score"]) * ((state["turn"]-1)*3)
#
#
# def part_two():
# 	state = {"die": 1, "turn": 1, "p1": {"num": 1, "score": 0, "pos": data[0]}, "p2": {"num": 2, "score": 0, "pos": data[1]}}
# 	while state["p1"]["score"] < 1000 and state["p2"]["score"] < 1000:
# 		make_move(state, deterministic_die)
# 	return min(state["p1"]["score"], state["p2"]["score"]) * ((state["turn"]-1)*3)
#
#
# if __name__ == '__main__':
# 	run_with_timer(part_one)  # 512442 -- took 0 ms
# 	run_with_timer(part_two)  #

from functools import cache


@cache
def play_dice(
	p1_position,
	p2_position,
	dice_roll_n=0,
	dice_sum=0,
	p1_score=0,
	p2_score=0,
	next_player=1,
	winning_score=21,
	board_size=10,
):
	p1_wins = 0
	p2_wins = 0
	if next_player == 1:
		if dice_roll_n < 3:
			for i in range(1, 4):
				next_dice_sum = dice_sum + i
				next_dice_roll_n = dice_roll_n + 1
				wins = play_dice(
					p1_position,
					p2_position,
					next_dice_roll_n,
					next_dice_sum,
					p1_score,
					p2_score,
					next_player,
				)
				p1_wins += wins[0]
				p2_wins += wins[1]
		else:
			dice_roll_n = 0
			next_p1_position = p1_position + dice_sum
			if next_p1_position > board_size:
				next_p1_position %= board_size
				if next_p1_position == 0:
					next_p1_position = board_size
			next_p1_score = p1_score + next_p1_position
			if next_p1_score >= winning_score:
				p1_wins += 1
			else:
				wins = play_dice(
					next_p1_position,
					p2_position,
					dice_roll_n,
					dice_sum=0,
					p1_score=next_p1_score,
					p2_score=p2_score,
					next_player=2,
				)
				p1_wins += wins[0]
				p2_wins += wins[1]

	if next_player == 2:
		if dice_roll_n < 3:
			for i in range(1, 4):
				next_dice_sum = dice_sum + i
				next_dice_roll_n = dice_roll_n + 1
				wins = play_dice(
					p1_position,
					p2_position,
					next_dice_roll_n,
					next_dice_sum,
					p1_score,
					p2_score,
					next_player,
				)
				p1_wins += wins[0]
				p2_wins += wins[1]
		else:
			dice_roll_n = 0
			next_p2_position = p2_position + dice_sum
			if next_p2_position > board_size:
				next_p2_position %= board_size
				if next_p2_position == 0:
					next_p2_position = board_size
			next_p2_score = p2_score + next_p2_position
			if next_p2_score >= winning_score:
				p2_wins += 1
			else:
				wins = play_dice(
					p1_position,
					next_p2_position,
					dice_roll_n,
					dice_sum=0,
					p1_score=p1_score,
					p2_score=next_p2_score,
					next_player=1,
				)
				p1_wins += wins[0]
				p2_wins += wins[1]

	return p1_wins, p2_wins


p1_pos = 8
p2_pos = 9
p1_wins, p2_wins = play_dice(p1_pos, p2_pos)
print(max(p1_wins, p2_wins))

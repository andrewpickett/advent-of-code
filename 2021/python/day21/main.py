from aoc_utils import run_with_timer

data = [int(x.split(": ")[1]) for x in open("input.txt").readlines()]


def deterministic_die(state):
	roll_val = 3 * state["die"] + 3
	state["die"] = ((state["die"] + 2) % 100) + 1
	return roll_val


def make_move(state, die_func):
	player = state["p1"] if state["turn"] % 2 == 1 else state["p2"]
	player["pos"] = ((player["pos"] + die_func(state) - 1) % 10) + 1
	player["score"] += player["pos"]
	state["turn"] += 1


def part_one():
	state = {"die": 1, "turn": 1, "p1": {"num": 1, "score": 0, "pos": data[0]}, "p2": {"num": 2, "score": 0, "pos": data[1]}}
	while state["p1"]["score"] < 1000 and state["p2"]["score"] < 1000:
		make_move(state, deterministic_die)
	return min(state["p1"]["score"], state["p2"]["score"]) * ((state["turn"]-1)*3)


def part_two():
	# state = {"die": 1, "turn": 1, "p1": {"num": 1, "score": 0, "pos": data[0]}, "p2": {"num": 2, "score": 0, "pos": data[1]}}
	# while state["p1"]["score"] < 1000 and state["p2"]["score"] < 1000:
	# 	make_move(state, deterministic_die)
	# return min(state["p1"]["score"], state["p2"]["score"]) * ((state["turn"]-1)*3)
	return


if __name__ == '__main__':
	run_with_timer(part_one)  # 512442 -- took 0 ms
	run_with_timer(part_two)  #

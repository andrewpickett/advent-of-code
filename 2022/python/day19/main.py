import copy

from aoc_utils import run_with_timer

data = [x.strip().split(" ") for x in open("input.txt").readlines()]


# ore, clay, obsidian, geode
blueprints = {
	1: {
		"none": [0, 0, 0, 0],
		"ore": [4, 0, 0, 0],
		"clay": [2, 0, 0, 0],
		"obsidian": [3, 14, 0, 0],
		"geode": [2, 0, 7, 0]
	},
	2: {
		"none": [0, 0, 0, 0],
		"ore": [2, 0, 0, 0],
		"clay": [3, 0, 0, 0],
		"obsidian": [3, 8, 0, 0],
		"geode": [3, 0, 12, 0]
	}
}

resources = ["ore", "clay", "obsidian", "geode", "none"]
max_hit = 0


# { "blueprint": 0, "resources": [], "robots": [] }
def move(state, depth, seen_combos):
	global max_hit
	if depth == 24:
		if state["resources"][3] > max_hit:
			print("Hit endstate: ", state["resources"])
			max_hit = state["resources"][3]
		return state["resources"][3]
	if (depth, '-'.join([str(x) for x in state["resources"]]), '-'.join([str(x) for x in state["robots"]])) in seen_combos:
		return -1
	seen_combos.add((depth, '-'.join([str(x) for x in state["resources"]]), '-'.join([str(x) for x in state["robots"]])))

	next_valid_moves = get_move_options(state)
	if "geode" in [x[0] for x in next_valid_moves]:
		next_valid_moves = [x for x in next_valid_moves if x[0] == "geode"]
	most_geodes = 0
	while next_valid_moves:
		next_move = next_valid_moves.pop(0)
		# lower resources to build next robot
		new_state = copy.deepcopy(state)
		new_state["resources"] = [t[0] - t[1] for t in zip(new_state["resources"], blueprints[new_state["blueprint"]][next_move[0]])]
		new_state["resources"] = [sum(t) for t in zip(state["robots"], new_state["resources"])]
		# add robot
		if next_move[0] != "none":
			new_state["robots"][resources.index(next_move[0])] += 1
		most_geodes = max(most_geodes, move(new_state, depth + 1, seen_combos))
	return max(most_geodes, move(state, depth + 1, seen_combos))


def get_move_options(state):
	moves = [("none", [0, 0, 0, 0])]
	for k, v in blueprints[state["blueprint"]].items():
		if sum(1 for i, x in enumerate(v) if state["resources"][i] >= x) == 4:
			moves.insert(0, (k, v))
	return moves


def part_one():
	quality_levels = []
	for blueprint in blueprints:
		max_geodes = move({"blueprint": blueprint, "resources": [0, 0, 0, 0], "robots": [1, 0, 0, 0]}, 1, set())
		quality_levels.append(blueprint * max_geodes)
	return sum(quality_levels)


def part_two():
	return


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #
# Part1Answer = 2341
# Part2Answer = 3689

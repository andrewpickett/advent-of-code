from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid, Point
from utils.algorithms import bfs


example1 = """#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######"""

example2 = """#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######"""

example3 = """#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######"""

example4 = """#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######"""

example5 = """#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######"""

example6 = """#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########"""

example7 = """#######
#######
#.E..G#
#.#####
#G#####
#######
#######"""

example8 = """####
#GG#
#.E#
####"""

example9 = """########
#..E..G#
#G######
########"""


def get_data(filename):
	grid = Grid(file=filename)
	# grid = Grid(values=[list(x) for x in example1.split("\n")])  # 47 * 590 = 27730
	# grid = Grid(values=[list(x) for x in example2.split("\n")])  # 37 * 982 = 36334
	# grid = Grid(values=[list(x) for x in example3.split("\n")])  # 46 * 859 = 39514
	# grid = Grid(values=[list(x) for x in example4.split("\n")])  # 35 * 793 = 27755
	# grid = Grid(values=[list(x) for x in example5.split("\n")])  # 54 * 536 = 28944
	# grid = Grid(values=[list(x) for x in example6.split("\n")])  # 20 * 937 = 18740
	# grid = Grid(values=[list(x) for x in example7.split("\n")])  # Move right
	# grid = Grid(values=[list(x) for x in example8.split("\n")])  # Attack up
	# grid = Grid(values=[list(x) for x in example9.split("\n")])  # Move left
	grid.set_neighbors_for_all()
	return {"grid": grid, "ed": 3, "eh": 200, "gd": 3, "gh": 200}


def part_one(d):
	set_damage(d["grid"], d["eh"], d["ed"], d["gh"], d["gd"])
	i = 0
	match_over = False
	while not match_over:
		all_combatants = [(y.get_row(), y.get_col()) for y in d["grid"].get_points() if y.get_value()[0] in ["E", "G"]]
		all_combatants.sort()
		full_round = True
		for x in all_combatants:
			combatant = d["grid"].get_point(coords=x)
			if combatant.get_value() not in ["E", "G"]:  # Needed since some may have been killed mid-round
				enemies = [(y.get_row(), y.get_col()) for y in d["grid"].get_points() if y.get_value()[0] == "E"] if combatant.get_value()[0] == "G" else [(y.get_row(), y.get_col()) for y in d["grid"].get_points() if y.get_value()[0] == "G"]
				if len(enemies) == 0:  # it's over once there are no enemies left to fight!
					full_round = False # if x != all_combatants[-1] else True
					match_over = True
					break
				else:
					if not attack(d["grid"], combatant):  # Attack if it's an option to -- if they do attack, their turn is over, otherwise they move.
						# min_dist = float("inf")
						# all_possible_moves = []
						# # for every "open" neighbor, do a BFS to every neighbor of every enemy and get the minimum
						# for neighbor in [n for n in combatant.get_neighbors() if n.get_value() == "."]:
						# 	for enemy in enemies:
						# 		possible_targets = [e for e in d["grid"].get_point(coords=enemy).get_neighbors() if e.get_value() == "." and abs(e.get_coord()[0] - neighbor.get_coord()[0]) + abs(e.get_coord()[1] - neighbor.get_coord()[1]) <= min_dist]
						# 		for target in possible_targets:
						# 			dist = bfs(src=target, dest=neighbor, neighbor_func=neighbor_traversal)
						# 			if dist:
						# 				all_possible_moves.append(dist)
						# 				min_dist = min(min_dist, dist[1])
						# if all_possible_moves:
						# 	all_possible_moves.sort(key=sort_func)
						# 	next_move = all_possible_moves[0]
						# 	next_move[0].set_value(combatant.get_value())
						# 	combatant.set_value(".")
						# 	attack(d["grid"], next_move[0])
						all_target_locations = []
						min_dist = float("inf")
						for enemy in enemies:  # Get a list of all destinations (open, accessible neighbor points for all enemies, and do a BFS to find distance to them all)
							possible_targets = [x for x in d["grid"].get_point(coords=enemy).get_neighbors() if x.get_value() == "." and abs(x.get_coord()[0] - combatant.get_coord()[0]) + abs(x.get_coord()[1] - combatant.get_coord()[1]) <= min_dist]
							for target in possible_targets:
								dist = bfs(src=combatant, dest=target, neighbor_func=neighbor_traversal)
								if dist:
									min_dist = min(min_dist, dist[1])
									all_target_locations.append(dist)
						if all_target_locations:  # if there are any places to move, do it, otherwise just stay still
							all_target_locations.sort(key=sort_func)
							# all_target_locations = [all_target_locations[0]]
							# Now go through all neighbors of combatant point, and find neighbor with shortest path to target and move there.
							all_next_moves = []
							for p in [n for n in combatant.get_neighbors() if n.get_value() == "."]:
								# for tl in all_target_locations:
								dist = bfs(src=all_target_locations[0][0], dest=p, neighbor_func=neighbor_traversal)
								if dist:
									all_next_moves.append(dist)
							if all_next_moves:
								all_next_moves.sort(key=sort_func)
								next_move = all_next_moves[0]
								next_move[0].set_value(combatant.get_value())
								combatant.set_value(".")
								attack(d["grid"], next_move[0])
		# print(output_grid(d["grid"]))
		# # print(d["grid"].output())
		# print()
		i += 1 if full_round else 0
	remaining = [x for x in d["grid"].get_points() if x.get_value()[0] in ["G", "E"]]
	print(i, sum(x.get_value()[1] for x in remaining))
	print(output_grid(d["grid"]))
	return i * sum(x.get_value()[1] for x in d["grid"].get_points() if x.get_value()[0] in ["G", "E"])


def neighbor_traversal(t):
	return [r for r in t[0].get_neighbors() if r.get_value() == "."]

def sort_func(t):
	return t[1], t[0].get_coord()

def attack(grid, combatant):
	immediate_targets = [x for x in combatant.get_neighbors() if (x.get_value()[0] == "G" and combatant.get_value()[0] == "E") or (x.get_value()[0] == "E" and combatant.get_value()[0] == "G")]
	if len(immediate_targets) > 0:
		immediate_targets.sort(key=lambda t: (t.get_value()[1], t.get_coord()))
		victim = grid.get_point(coords=immediate_targets[0].get_coord())
		new_hp = victim.get_value()[1] - combatant.get_value()[2]
		if new_hp <= 0:
			victim.set_value(".")
		else:
			victim.set_value((victim.get_value()[0], new_hp, victim.get_value()[2]))
		return True
	return False


def output_grid(grid):
	out_val = ""
	for row in range(len(grid.data)):
		out_val += "".join([str(x.get_value()[0]) for x in grid.data[row]])
		if row < len(grid.data) - 1:
			out_val += "\n"
	return out_val


def set_damage(grid, e_hp, e_dam, g_hp, g_dam):
	for row in range(grid.get_height()):
		for col in range(grid.get_width()):
			if grid.get_point(row, col).get_value() == "G":
				grid.get_point(row, col).set_value(("G", g_hp, g_dam))
			elif grid.get_point(row, col).get_value() == "E":
				grid.get_point(row, col).set_value(("E", e_hp, e_dam))


def part_two(d):
	return


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data) # 215168 (82 * 2624)
	run_with_timer(part_two, data) # 52374


if __name__ == '__main__':
	main()

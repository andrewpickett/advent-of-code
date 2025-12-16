from utils.timers import run_with_timer, get_data_with_timer
from utils.grid import Grid
from utils.algorithms import bfs


def get_data(filename):
	grid = Grid(file=filename)
	grid.set_neighbors_for_all()
	return {"grid": grid, "ed": 3, "eh": 200, "gd": 3, "gh": 200}


def part_one(d):
	set_damage(d["grid"], d["eh"], d["ed"], d["gh"], d["gd"])
	i = 1
	match_over = False
	while not match_over:
		# print("Round", i)
		# print("-------------------------------------------------------------------------------------")
		# print(output_grid(d["grid"]))
		all_combatants = [y for y in d["grid"].get_points() if y.get_value()[0] in ["E", "G"]]
		all_combatants.sort(key=lambda pt: (pt.get_row(), pt.get_col()))
		for z, combatant in enumerate(all_combatants):
			if combatant.get_value()[0] in ["E", "G"]:  # Needed since some may have been killed mid-round
				elves = [y for y in d["grid"].get_points() if y.get_value()[0] == "E"]
				goblins = [y for y in d["grid"].get_points() if y.get_value()[0] == "G"]
				enemies = elves if combatant.get_value()[0] == "G" else goblins
				if len(elves) == 0 or len(goblins) == 0:  # it's over once there are no enemies left to fight!
					# print("No enemies found. Time to finish.")
					i -= 1 if z < len(all_combatants) - 1 else 0
					match_over = True
					break
				else:
					# Move if we need to.
					combatant = move(combatant, [y for y in enemies if y.get_value() != "."])
					attack(combatant)
			else:
				print(combatant, "must have been killed this round!")
		if not match_over:
			# print("Finished full round", i)
			# print()
			i += 1

	# print()
	# print("FINAL AFTER", i, "FULL ROUNDS")
	# print(output_grid(d["grid"]))
	s = sum(x.get_value()[1] for x in d["grid"].get_points() if x.get_value()[0] in ["G", "E"])
	return i, s, i * s


def move(p, enemies):
	immediate_targets = [x for x in p.get_neighbors() if (x.get_value()[0] == "G" and p.get_value()[0] == "E") or (x.get_value()[0] == "E" and p.get_value()[0] == "G")]
	if len(immediate_targets) > 0:
		# Don't need to move, as we have an ememy right next to us! Just attack.
		# print(p, "can just attack someone next to them.")
		return p

	all_next_moves = []
	min_dist = float("inf")
	# for every possible next move, check the distance to every target location. Find the next move with the shortest distance and take it.
	for next_possible_move in [x for x in p.get_neighbors() if x.get_value() == "."]:
		if enemies:
			for enemy in enemies:
				# We can shortcut the list of possible targets a bit by only getting ones whose manhattan distance is less than or equal to the closest so far (since any further wouldn't matter)
				possible_targets = [x for x in enemy.get_neighbors() if x.get_value() == "." and abs(p.get_row() - x.get_row()) + abs(p.get_col() - x.get_col()) <= min_dist]
				if possible_targets:
					for possible_target in possible_targets:
						dist = bfs(src=possible_target, dest=next_possible_move, neighbor_func=lambda pt: [r for r in pt.get_neighbors() if r.get_value() == "."])
						if dist and dist[1] <= min_dist:
							min_dist = dist[1]
							all_next_moves.append(dist)
		# 		else:
		# 			print("No possible targets for", p, "to attack", enemy, "from", next_possible_move)
		# else:
		# 	print("No enemies available for", p, "to attack.")
	if all_next_moves:
		all_next_moves.sort(key=lambda pt: (pt[1], pt[0].get_coord()))
		next_move = all_next_moves[0][0]
		next_move.set_value(p.get_value())
		# print(p, "is moving to", next_move)
		p.set_value(".")
		return next_move
	return p


def attack(combatant):
	immediate_targets = [x for x in combatant.get_neighbors() if (x.get_value()[0] == "G" and combatant.get_value()[0] == "E") or (x.get_value()[0] == "E" and combatant.get_value()[0] == "G")]
	if len(immediate_targets) > 0:
		immediate_targets.sort(key=lambda t: (t.get_value()[1], t.get_coord()))
		victim = immediate_targets[0]
		new_hp = victim.get_value()[1] - combatant.get_value()[2]
		if new_hp <= 0:
			victim.set_value(".")
			# print(combatant, "killed", victim)
		else:
			victim.set_value((victim.get_value()[0], new_hp, victim.get_value()[2]))
			# print(combatant, "hit", victim, "for", combatant.get_value()[2], "damage. Down to", new_hp)


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
	run_with_timer(part_one, data)  # 215168 (82 * 2624)
	run_with_timer(part_two, data)  # 52374


if __name__ == '__main__':
	main("input.txt")

from utils.timers import run_with_timer, get_data_with_timer
from copy import copy


weapons = {
	"dagger": {"cost": 8, "damage": 4, "armor": 0},
	"shortsword": {"cost": 10, "damage": 5, "armor": 0},
	"warhammer": {"cost": 25, "damage": 6, "armor": 0},
	"longsword": {"cost": 40, "damage": 7, "armor": 0},
	"greataxe": {"cost": 74, "damage": 8, "armor": 0}
}
armor = {
	"leather": {"cost": 13, "damage": 0, "armor": 1},
	"chainmail": {"cost": 31, "damage": 0, "armor": 2},
	"splintmail": {"cost": 53, "damage": 0, "armor": 3},
	"bandedmail": {"cost": 75, "damage": 0, "armor": 4},
	"platemail": {"cost": 102, "damage": 0, "armor": 5}
}
rings = {
	"none1": {"cost": 0, "damage": 0, "armor": 0},
	"none2": {"cost": 0, "damage": 0, "armor": 0},
	"damage+1": {"cost": 25, "damage": 1, "armor": 0},
	"damage+2": {"cost": 50, "damage": 2, "armor": 0},
	"damage+3": {"cost": 100, "damage": 3, "armor": 0},
	"defense+1": {"cost": 20, "damage": 0, "armor": 1},
	"defense+2": {"cost": 40, "damage": 0, "armor": 2},
	"defense+3": {"cost": 80, "damage": 0, "armor": 3}
}


def get_data(filename):
	d = [x.strip() for x in open(filename).readlines()]
	return {"hp": int(d[0].split(" ")[2]), "damage": int(d[1].split(" ")[1]), "armor": int(d[2].split(" ")[1])}


def fight(player_stats, boss_stats):
	turn = 1
	while player_stats["hp"] > 0 and boss_stats["hp"] > 0:
		defender = boss_stats if turn % 2 == 1 else player_stats
		offender = player_stats if turn % 2 == 1 else boss_stats
		defender["hp"] -= 1 if offender["damage"] - defender["armor"] <= 0 else offender["damage"] - defender["armor"]
		turn += 1
	return player_stats["hp"] > 0


def get_fight_costs(d, want_to_win):
	costs = []
	for w in weapons:
		for a in armor:
			for r1 in rings:
				for r2 in rings:
					if r1 != r2:
						player_stats = {"hp": 100, "damage": sum([weapons[w]["damage"], rings[r1]["damage"], rings[r2]["damage"]]), "armor": sum([armor[a]["armor"], rings[r1]["armor"], rings[r2]["armor"]])}
						player_wins = fight(player_stats, copy(d))
						if (player_wins and want_to_win) or (not player_wins and not want_to_win):
							costs.append(sum([weapons[w]["cost"], armor[a]["cost"], rings[r1]["cost"], rings[r2]["cost"]]))
	return costs


def part_one(d):
	print(d)
	return min(get_fight_costs(d, True))


def part_two(d):
	return max(get_fight_costs(d, False))


if __name__ == '__main__':
	data = get_data_with_timer(get_data, "input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

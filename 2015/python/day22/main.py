from utils.timers import run_with_timer, get_data_with_timer
from copy import deepcopy

spells = {
	"Magic Missile": {"name": "Magic Missile", "cost": 53, "dmg": 4, "hp": 0, "mp": 0, "def": 0, "duration": 0},
	"Drain": {"name": "Drain", "cost": 73, "dmg": 2, "hp": 2, "mp": 0, "def": 0, "duration": 0},
	"Shield": {"name": "Shield", "cost": 113, "dmg": 0, "hp": 0, "mp": 0, "def": 7, "duration": 6},
	"Poison": {"name": "Poison", "cost": 173, "dmg": 3, "hp": 0, "mp": 0, "def": 0, "duration": 6},
	"Recharge": {"name": "Recharge", "cost": 229, "dmg": 0, "hp": 0, "mp": 101, "def": 0, "duration": 5}
}


def get_data(filename):
	stats = [int(x.strip().split()[-1]) for x in open(filename).readlines()]
	return {"hp": stats[0], "mp": 0, "atk": stats[1], "def": 0, "spells": []}


def play_game(p_hp, p_mp, b_hp, b_atk, p_turn, active_spells, mana_used, least_mana, hard_mode=False):
	p_def = 0

	if hard_mode and p_turn:
		p_hp -= 1
		if p_hp <= 0:
			return False

	new_active_spells = []
	for active_spell in active_spells:
		if active_spell["duration"] >= 0:
			b_hp -= active_spell["dmg"]
			p_hp += active_spell["hp"]
			p_def += active_spell["def"]
			p_mp += active_spell["mp"]

		new_active_spell = deepcopy(active_spell)
		new_active_spell["duration"] -= 1
		if new_active_spell["duration"] > 0:
			new_active_spells.append(new_active_spell)

	if b_hp <= 0:
		if mana_used < least_mana[0]:
			least_mana[0] = mana_used
		return True

	if mana_used >= least_mana[0]:
		return False

	if not p_turn:
		p_hp -= b_atk - p_def if b_atk - p_def > 0 else 1
		if p_hp > 0:
			play_game(p_hp, p_mp, b_hp, b_atk, True, new_active_spells, mana_used, least_mana, hard_mode)
	else:
		for k, v in spells.items():
			spell_active = False
			for active_spell in new_active_spells:
				if active_spell["name"] == k:
					spell_active = True
					break

			spell_cost = v["cost"]
			if spell_cost <= p_mp and not spell_active:
				a = deepcopy(new_active_spells)
				a.append(deepcopy(v))
				play_game(p_hp, p_mp - spell_cost, b_hp, b_atk, False, a, mana_used + spell_cost, least_mana, hard_mode)


def part_one(d):
	least_mana = [float("inf")]
	play_game(50, 500, d["hp"], d["atk"], True, [], 0, least_mana)
	return least_mana[0]


def part_two(d):
	least_mana = [float("inf")]
	play_game(50, 500, d["hp"], d["atk"], True, [], 0, least_mana, True)
	return least_mana[0]


if __name__ == '__main__':
	data = get_data_with_timer(get_data, "input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

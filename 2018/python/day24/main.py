from utils.timers import run_with_timer, get_data_with_timer
from copy import deepcopy


class Army:
	def __init__(self, name):
		self.name = name
		self.groups = []

	def add_group(self, group):
		self.groups.append(group)

	def has_fighters(self):
		return sum(1 for x in self.groups if x.units > 0)

	def remove_targets(self):
		for x in self.groups:
			x.target = None

	def __str__(self):
		s = self.name + ":\n"
		for x in self.groups:
			if x.units > 0:
				s += str(x) + "\n"
		return s

	def __repr__(self):
		return self.__str__()


class Group:
	def __init__(self, army, label, line):
		parts = line.split()
		self.army = army
		self.label = label
		self.units = int(parts[0])
		self.hp = int(parts[4])
		self.weakness = extract_properties(parts, "weak")
		self.immunity = extract_properties(parts, "immune")
		self.attack = int(parts[parts.index("attack")+3])
		self.type = parts[parts.index("attack")+4]
		self.initiative = int(parts[-1])
		self.target = None
		self.effective_power = self.units * self.attack
		self.dmg = 0

	def destroy_units(self, units):
		self.units -= units
		self.effective_power = self.units * self.attack
		self.dmg = calc_damage(self, self.target)

	def __str__(self):
		return "Group {} contains {} units".format(self.label, self.units)

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other):
		return self.label == other.label and self.army == other.army

	def __lt__(self, other):
		if self.effective_power == other.effective_power:
			return self.initiative > other.initiative
		else:
			return self.effective_power > other.effective_power


def get_data(filename):
	immune_system = Army("Immune System")
	infection = Army("Infection")

	lines = [x.strip() for x in open(filename).readlines()]
	curr_army = immune_system
	label = 1
	for line in lines[1:]:
		if line != "":
			if line == "Infection:":
				curr_army = infection
				label = 1
			else:
				curr_army.add_group(Group(curr_army.name, label, line))
				label += 1
	return [immune_system, infection]


def part_one(d):
	armies = deepcopy(d)
	while armies[0].has_fighters() and armies[1].has_fighters():
		fight(armies)
	return sum(x.units for x in armies[0].groups) + sum(x.units for x in armies[1].groups)


def part_two(d):
	boost = 0
	while True:
		boost += 1
		armies = deepcopy(d)
		for x in armies[0].groups:
			x.attack += boost
			x.effective_power = x.units * x.attack
		last_total_unit_count = 0
		total_count = sum(x.units for x in armies[0].groups) + sum(x.units for x in armies[1].groups)
		while armies[0].has_fighters() and armies[1].has_fighters() and total_count != last_total_unit_count:
			total_count = sum(x.units for x in armies[0].groups) + sum(x.units for x in armies[1].groups)
			fight(armies)
			last_total_unit_count = sum(x.units for x in armies[0].groups) + sum(x.units for x in armies[1].groups)
		if armies[0].has_fighters() and not armies[1].has_fighters():
			break
	return sum(x.units for x in armies[0].groups)


def fight(d):
	for army in d:
		army.groups.sort()
	select_targets(d[1], d[0])
	select_targets(d[0], d[1])
	attack_targets(d[0], d[1])
	d[0].remove_targets()
	d[1].remove_targets()


def select_targets(attackers, defenders):
	selected_targets = []
	for i in attackers.groups:
		target = None
		max_dmg = 0
		for j in [x for x in defenders.groups if x not in selected_targets and x.units > 0]:
			dmg = calc_damage(i, j)
			if dmg > max_dmg:
				max_dmg = dmg
				target = j
			elif dmg == max_dmg and dmg != 0:
				if j.effective_power > target.effective_power:
					target = j
				elif j.effective_power == target.effective_power:
					target = j if j.initiative > target.initiative else target
		if target:
			i.dmg = max_dmg
			i.target = target
			selected_targets.append(target)


def calc_damage(attacker, defender):
	dmg = attacker.effective_power
	if defender:
		if attacker.type in defender.weakness:
			dmg *= 2
		elif attacker.type in defender.immunity:
			dmg = 0
	return dmg


def attack_targets(immunities, infections):
	all_attackers = list(reversed(sorted(immunities.groups + infections.groups, key=lambda item: item.initiative)))
	for x in all_attackers:
		if x.target:
			units_killed = min(x.dmg // x.target.hp, x.target.units)
			x.target.destroy_units(units_killed)


def extract_properties(parts, prop):
	props = []
	if "(" + prop in parts or prop in parts:
		idx = parts.index("(" + prop) if "(" + prop in parts else parts.index(prop)
		for x in parts[idx+2:]:
			props.append(x[:-1])
			if x.endswith(";") or x.endswith(")"):
				break
	return props


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

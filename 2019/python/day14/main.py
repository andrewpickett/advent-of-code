data = [x.strip() for x in open("input.txt").readlines()]


def part_one():
	reactions, curr_inventory = build_reaction_map(list(data))
	return perform_reaction(reactions, 1, 'FUEL', curr_inventory)


def build_reaction_map(lines):
	reactions = {}
	curr_inventory = {'ORE': 0}
	for line in lines:
		parts = line.split(' => ')
		ins = [(int(y[0]), y[1]) for y in [x.strip().split(' ') for x in parts[0].split(',')]]
		outs = [(int(y[0]), y[1]) for y in [x.strip().split(' ') for x in parts[1].split(',')]]
		reactions[outs[0][1]] = (ins, outs)
		curr_inventory[outs[0][1]] = 0
	return reactions, curr_inventory


def perform_reaction(reactions, quantity, material, curr_inventory):
	if material == 'ORE':
		return quantity
	elif material == 'FUEL':
		for k in curr_inventory.keys():
			curr_inventory[k] = 0
	recipe = reactions[material]
	missing = quantity - curr_inventory[material]
	if missing <= 0:
		return 0
	(num, rem) = divmod(missing, recipe[1][0][0])
	if rem > 0:
		num += 1
	for ins in recipe[0]:
		perform_reaction(reactions, ins[0] * num, ins[1], curr_inventory)
		curr_inventory[ins[1]] -= ins[0] * num
	curr_inventory[material] += recipe[1][0][0] * num
	return -curr_inventory['ORE']


def part_two():
	reactions, curr_inventory = build_reaction_map(list(data))
	trying = 1
	goal = 1000000000000
	maxtry = mintry = 0
	while True:
		res = perform_reaction(reactions, trying, 'FUEL', curr_inventory)
		if res > goal:
			break
		mintry = trying
		trying *= 2
		maxtry = trying

	while maxtry - mintry > 1:
		newtry = (mintry + maxtry) // 2
		res = perform_reaction(reactions, newtry, 'FUEL', curr_inventory)
		if res > goal:
			maxtry = newtry
		else:
			mintry = newtry
	return mintry


if __name__ == '__main__':
	print(part_one())  # 178154
	print(part_two())  # 6226152

data = [x.strip() for x in open("input.txt").readlines()]


def part_one():
	recipes, counts = build_reaction_map(list(data))
	return produce(recipes, 1, 'FUEL', counts)


def build_reaction_map(lines):
	recipes = {}
	counts = {'ORE': 0}
	for line in lines:
		parts = line.split(' => ')
		ins = [(int(y[0]), y[1]) for y in [x.strip().split(' ') for x in parts[0].split(',')]]
		outs = [(int(y[0]), y[1]) for y in [x.strip().split(' ') for x in parts[1].split(',')]]
		recipes[outs[0][1]] = (ins, outs)
		counts[outs[0][1]] = 0
	return recipes, counts


def produce(recipes, num, what, counts):
	if what == 'ORE':
		return num
	elif what == 'FUEL':
		for k in counts.keys():
			counts[k] = 0
	recipe = recipes[what]
	missing = num - counts[what]
	if missing <= 0:
		return 0
	(num2, rem2) = divmod(missing, recipe[1][0][0])
	if rem2 > 0:
		num2 += 1
	for ins in recipe[0]:
		produce(recipes, ins[0]*num2, ins[1], counts)
		counts[ins[1]] -= ins[0]*num2
	counts[what] += recipe[1][0][0]*num2
	return -counts['ORE']


def part_two():
	recipes, counts = build_reaction_map(list(data))
	trying = 1
	goal = 1000000000000
	maxtry = mintry = 0
	while True:
		res = produce(recipes, trying, 'FUEL', counts)
		if res > goal:
			break
		mintry = trying
		trying *= 2
		maxtry = trying

	while maxtry - mintry > 1:
		newtry = (mintry + maxtry) // 2
		res = produce(recipes, newtry, 'FUEL', counts)
		if res > goal:
			maxtry = newtry
		else:
			mintry = newtry
	return mintry


if __name__ == '__main__':
	print(part_one())  # 178154
	print(part_two())  # 6226152

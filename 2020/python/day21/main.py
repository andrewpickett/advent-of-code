from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def map_allergens(full_list):
	possible_allergens = {}

	all_allergens = set()
	all_ingredients = set()
	for x in full_list:
		for i in x[0]:
			all_ingredients.add(i)
			if i not in possible_allergens:
				possible_allergens[i] = set()
			for a in x[1]:
				all_allergens.add(a)
				possible_allergens[i].add(a)

	mapped_allergens = {}
	while len(mapped_allergens.keys()) < len(all_allergens):
		for i, x in enumerate(all_allergens):
			if x not in mapped_allergens.keys():
				lines = [set(y[0]) for y in full_list if x in y[1]]
				# Remove any already-mapped allergens from the line.
				for line in lines:
					for a in mapped_allergens.values():
						if a in line:
							line.remove(a)
				# Find any words that are common across all lines for this allergen
				common = lines[0]
				for y in lines:
					common = common & y
				# If there is only one common word across all of the lines, then that must be the allergen
				if len(common) == 1:
					mapped_allergens[x] = common.pop()
	return mapped_allergens


def part_one():
	full_list = [([y.strip() for y in x[:x.index('(')-1].split()], [y.strip() for y in x[x.index('(')+10:-1].split(',')]) for x in data]
	mapped_allergens = map_allergens(full_list)
	all_data = ' '.join([' '.join(x[0]) for x in full_list])

	for x in mapped_allergens.values():
		all_data = all_data.replace(x, '')
	return len(all_data.split())


def part_two():
	full_list = [([y.strip() for y in x[:x.index('(')-1].split()], [y.strip() for y in x[x.index('(')+10:-1].split(',')]) for x in data]
	mapped_allergens = map_allergens(full_list)
	sorted_allergens = sorted(mapped_allergens.keys(), key=lambda x: x.lower())
	return ','.join([mapped_allergens[k] for k in sorted_allergens])


if __name__ == '__main__':
	run_with_timer(part_one)  # 2798 -- took 7 ms
	run_with_timer(part_two)  # gbt,rpj,vdxb,dtb,bqmhk,vqzbq,zqjm,nhjrzzj -- took 6 ms

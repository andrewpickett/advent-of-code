from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def get_bag_map():
	bag_map = {}
	for x in data:
		parts = x.split(' bags contain ')
		bag_map[parts[0]] = {}
		if not parts[1] == 'no other bags.':
			contents = parts[1].split(',')
			for content in contents:
				tmp = content.split()
				bag_map[parts[0]][' '.join(tmp[1:-1])] = int(tmp[0])
	return bag_map


def part_one():
	bag_map = get_bag_map()

	changed = True
	initial_bag_set = set()
	initial_bag_set.add('shiny gold')
	while changed:
		changed = False
		initial_size = len(initial_bag_set)
		for k, v in bag_map.items():
			for bag in bag_map[k].keys():
				if bag in initial_bag_set:
					initial_bag_set.add(k)
					if len(initial_bag_set) > initial_size:
						changed = True
	initial_bag_set.remove('shiny gold')
	return len(initial_bag_set)


def count_bags(bag_map, bag):
	return 1 + sum(v * count_bags(bag_map, k) for k, v in bag_map[bag].items())


def part_two():
	return count_bags(get_bag_map(), 'shiny gold') - 1


if __name__ == '__main__':
	run_with_timer(part_one)  # 185 -- took 2 ms
	run_with_timer(part_two)  # 89084 -- took 2 ms

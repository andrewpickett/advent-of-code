from aoc_utils import run_with_timer

data = [x.strip() for x in open('sample.txt').readlines() if not x.isspace()]


def get_data_as_molecule_map():
	molecule = get_elems(data[-1])
	replacements = data[:-1]
	molmap = {}
	for x in replacements:
		parts = x.split(' => ')
		if parts[0] not in molmap.keys():
			molmap[parts[0]] = []
		molmap[parts[0]].append(get_elems(parts[1]))
	return molecule, molmap


def get_elems(molecule):
	elems = []
	curr_elem = ''
	for i in range(len(molecule)):
		if molecule[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			if curr_elem != '':
				elems.append(curr_elem)
			curr_elem = ''
		curr_elem += molecule[i]
	elems.append(curr_elem)
	return elems


def replace_all_individually(molecule, replacee, replacements):
	all_replaced = []
	for replacement in replacements:
		curr_index = 0
		for _ in range(molecule.count(replacee)):
			# idx = molecule.index(replacee)
			curr_index = molecule[curr_index:].index(replacee) + curr_index
			mcop = molecule.copy()
			mcop[curr_index] = ''.join(replacement)
			all_replaced.append(''.join(mcop))
			curr_index += 1
	return all_replaced


def replacement_step(molecule, molmap):
	unique_molecules = set(x for x in [replace_all_individually(molecule, replacee, replacements) for replacee, replacements in molmap.items()])
	# for replacee, replacement in molmap.items():
	# 	unique_molecules.update(replace_all_individually(molecule, replacee, replacement))
	return len(unique_molecules)


def part_one():
	molecule, molmap = get_data_as_molecule_map()
	return replacement_step(molecule, molmap)


def f(start, target, molmap, depth):
	if len(start) > len(target):
		return None
	elif start == target:
		return depth

	curr_min = 999999999
	for i in range(len(start)):
		for j in molmap[start[i]]:
			next_val = f(start[:i] + j + start[i+1:], target, molmap, depth+1)
			if next_val:
				curr_min = min(curr_min, next_val)
	return curr_min


def part_two():
	molecule = get_elems(data[-1])
	molmap = get_data_as_molecule_map()


if __name__ == '__main__':
	run_with_timer(part_one)  # 509 -- took 0 ms
	run_with_timer(part_two)  #

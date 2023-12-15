from utils.timers import run_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines() if not x.isspace()]


def get_data_as_molecule_map(d):
	molecule = get_elems(d[-1])
	molmap = {}
	for x in d[:-1]:
		parts = x.split(' => ')
		if parts[0] not in molmap.keys():
			molmap[parts[0]] = []
		molmap[parts[0]].append(parts[1])
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


def replacement_step(molecule, molmap):
	unique_molecules = set()
	for i, x in enumerate(molecule):
		if x in molmap:
			for y in molmap[x]:
				new_molecule = molecule.copy()
				new_molecule[i] = ''.join(y)
				unique_molecules.add(''.join(new_molecule))
	return unique_molecules


def part_one(d):
	molecule, molmap = get_data_as_molecule_map(d)
	return len(replacement_step(molecule, molmap))


def invert_replacements(d):
	reverse = {}
	for k, v in d.items():
		for i in v:
			if i not in reverse:
				reverse[i] = []
			reverse[i].append(k)
	return reverse


def get_previous_molecules(target, replacements):
	molecules = set()

	for k, v in replacements.items():
		idx = target.find(k)
		while idx >= 0:
			for i in v:
				if i != "e":
					molecules.add(target[:idx] + i + target[idx + len(k):])
			idx = target.find(k, idx+1)
	if len(molecules) == 0:
		molecules = {"e"}
	return molecules


def build_molecule(target, replacements):
	replacements = invert_replacements(replacements)
	mset = {}
	last_generation = get_previous_molecules(target, replacements)
	n_steps = 1
	while last_generation != {"e"}:
		current_generation = set()
		m = min(last_generation, key=len)

		if m in mset:
			new_molecules = mset[m]
		else:
			new_molecules = get_previous_molecules(m, replacements)
			mset[m] = new_molecules
		current_generation |= new_molecules
		last_generation = current_generation
		n_steps += 1
	return n_steps


def part_two(d):
	molecule, molmap = get_data_as_molecule_map(d)
	return build_molecule(''.join(molecule), molmap)


if __name__ == '__main__':
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

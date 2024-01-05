from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	d = [x.strip() for x in open(filename).readlines() if not x.isspace()]

	molecule = []
	curr_elem = ''
	for i in range(len(d[-1])):
		if d[-1][i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			if curr_elem != '':
				molecule.append(curr_elem)
			curr_elem = ''
		curr_elem += d[-1][i]
	molecule.append(curr_elem)

	molmap = {}
	for x in d[:-1]:
		parts = x.split(' => ')
		if parts[0] not in molmap.keys():
			molmap[parts[0]] = []
		molmap[parts[0]].append(parts[1])

	return {"molecule": molecule, "molmap": molmap}


def part_one(d):
	unique_molecules = set()
	for i, x in enumerate(d["molecule"]):
		if x in d["molmap"]:
			for y in d["molmap"][x]:
				new_molecule = d["molecule"].copy()
				new_molecule[i] = ''.join(y)
				unique_molecules.add(''.join(new_molecule))
	return len(unique_molecules)


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
	return build_molecule(''.join(d["molecule"]), d["molmap"])


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

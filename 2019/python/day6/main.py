from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	data = [tuple(x.strip().split(')')) for x in open(filename).readlines()]
	return build_orbit_tree(data)


class TreeNode:
	def __init__(self):
		self.parent_node = None
		self.orbit_chain = []

	def add_child(self, child):
		child.parent_node = self

	def build_orbit_chain(self):
		ancestor = self.parent_node
		while ancestor:
			self.orbit_chain.append(ancestor)
			ancestor = ancestor.parent_node


def build_orbit_tree(d):
	orbitals = {}
	for x in d:
		orbitals[x[0]] = TreeNode() if x[0] not in orbitals else orbitals[x[0]]
		orbitals[x[1]] = TreeNode() if x[1] not in orbitals else orbitals[x[1]]
		orbitals[x[0]].add_child(orbitals[x[1]])

	for orbital in orbitals.values():
		orbital.build_orbit_chain()

	return orbitals


def part_one(d):
	return sum(len(d[x].orbit_chain) for x in d)


def part_two(d):
	my_chain = d['YOU'].orbit_chain
	san_chain = d['SAN'].orbit_chain

	common_ancestor = None
	for _, elem in enumerate(my_chain):
		if elem in san_chain:
			common_ancestor = elem
			break
	return my_chain.index(common_ancestor) + san_chain.index(common_ancestor)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

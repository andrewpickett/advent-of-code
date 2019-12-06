data = [tuple(x.strip().split(')')) for x in open("input.txt").readlines()]

planets = {}


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


def build_orbit_tree():
	orbitals = {}
	for d in data:
		orbitals[d[0]] = TreeNode() if d[0] not in orbitals else orbitals[d[0]]
		orbitals[d[1]] = TreeNode() if d[1] not in orbitals else orbitals[d[1]]
		orbitals[d[0]].add_child(orbitals[d[1]])

	for orbital in orbitals.values():
		orbital.build_orbit_chain()

	return orbitals


def part_one():
	return sum(len(planets[x].orbit_chain) for x in planets)


def part_two():
	my_chain = planets['YOU'].orbit_chain
	san_chain = planets['SAN'].orbit_chain

	common_ancestor = None
	for _, elem in enumerate(my_chain):
		if elem in san_chain:
			common_ancestor = elem
			break
	return my_chain.index(common_ancestor) + san_chain.index(common_ancestor)


if __name__ == '__main__':
	planets = build_orbit_tree()
	print(part_one())  # 308790
	print(part_two())  # 472

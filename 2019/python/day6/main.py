data = [x.strip() for x in open("input.txt").readlines()]

planets = {}


class OrbitTreeNode:
	def __init__(self, name):
		self.name = name
		self.parent_node = None
		self.child_nodes = set()

	def add_child(self, child):
		self.child_nodes.add(child)
		child.parent_node = self

	def get_orbit_chain(self):
		chain = []
		ancestor = self.parent_node
		while ancestor:
			chain.append(ancestor)
			ancestor = ancestor.parent_node
		return chain


def build_orbit_tree():
	orbitals = {}
	for orbit in data:
		objects = orbit.split(')')
		parent = objects[0]
		child = objects[1]

		orbitals[parent] = OrbitTreeNode(parent) if parent not in orbitals else orbitals[parent]
		orbitals[child] = OrbitTreeNode(child) if child not in orbitals else orbitals[child]
		orbitals[parent].add_child(orbitals[child])
	return orbitals


def part_one():
	return sum(len(planets[x].get_orbit_chain()) for x in planets)


def part_two():
	my_chain = planets['YOU'].get_orbit_chain()
	san_chain = planets['SAN'].get_orbit_chain()

	common_ancestor = None
	for i, elem in enumerate(my_chain):
		if elem in san_chain:
			common_ancestor = elem
			break
	return my_chain.index(common_ancestor) + san_chain.index(common_ancestor)


if __name__ == '__main__':
	planets = build_orbit_tree()
	print(part_one())  # 308790
	print(part_two())  # 472

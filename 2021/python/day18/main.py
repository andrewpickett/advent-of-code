from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


class Node:
	def __init__(self, left, right, parent, depth):
		self.left = left
		self.right = right
		self.parent = parent
		self.depth = depth

	def add(self, other):
		self.depth += 1
		other.depth += 1
		return Node(self, other, self.depth)

	def get_magnitude(self):
		left_val = self.left.get_magnitude() if isinstance(self.left, Node) else self.left
		right_val = self.right.get_magnitude() if isinstance(self.right, Node) else self.right
		return 3*left_val + 2*right_val

	def __repr__(self):
		return "[" + str(self.left) + "," + str(self.right) + "]"

	def __str__(self):
		return "[" + str(self.left) + "," + str(self.right) + "]"


def build_tree(st):
	depth = 1
	last_node = None
	root_node = None
	for s in st:
		if s == '[':
			n = Node(None, None, last_node, depth)
			if last_node:
				if last_node.left == 0 or last_node.left:
					last_node.right = n
				else:
					last_node.left = n
			depth += 1
			last_node = n
			if not root_node:
				root_node = n
		elif s == ']':
			depth -= 1
			last_node = last_node.parent
		elif s.isnumeric():
			if last_node.left == 0 or last_node.left:
				last_node.right = int(s)
			else:
				last_node.left = int(s)
	return root_node


def split_if_needed(root, parent, is_left):
	did_split = False
	if isinstance(root, Node):
		if root.left:
			did_split = did_split or split_if_needed(root.left, root, True)
		if root.right:
			did_split = did_split or split_if_needed(root.right, root, False)
	else:
		if root > 9:
			split(root, parent, is_left)
			return True
	return did_split


def explode_if_needed(root, is_left):
	exploded = False
	if isinstance(root, Node):
		if root.left:
			exploded = exploded or explode_if_needed(root.left, True)
		if root.right:
			exploded = exploded or explode_if_needed(root.right, False)
		if root.depth > 4:
			explode(root, is_left)
			return True
	return exploded


def find_nearest_neighbor(n, is_left):
	new_node = n
	if new_node.parent is None:
		# n was the root, so there is no nearest neighbor
		return None, False

	check_node = new_node.parent.left if is_left else new_node.parent.right
	while check_node == new_node:
		new_node = new_node.parent
		if new_node.parent is None:
			# We're at the root, and haven't found one, so there must not be one.
			return None, False
		check_node = new_node.parent.left if is_left else new_node.parent.right

	if not isinstance(check_node, Node):
		return new_node.parent, False
	new_node = check_node
	moved_over = False
	check_node = new_node.right if is_left else new_node.left
	while check_node is not None:
		moved_over = True
		if isinstance(check_node, Node):
			new_node = check_node
		else:
			break
		check_node = new_node.right if is_left else new_node.left
	return new_node, moved_over


def explode(n, is_left):
	explode_left, went_right = find_nearest_neighbor(n, True)
	explode_right, went_left = find_nearest_neighbor(n, False)

	if explode_left:
		if went_right:
			explode_left.right += n.left
		else:
			explode_left.left += n.left
	if explode_right:
		if went_left:
			explode_right.left += n.right
		else:
			explode_right.right += n.right

	if is_left:
		n.parent.left = 0
	else:
		n.parent.right = 0


def split(val, n, is_left):
	new_node = Node(val // 2, val - val // 2, n, n.depth + 1)
	if is_left:
		n.left = new_node
	else:
		n.right = new_node


def increment_depth(root):
	root.depth += 1
	if isinstance(root.left, Node):
		increment_depth(root.left)
	if isinstance(root.right, Node):
		increment_depth(root.right)


def add_nodes(node1, node2):
	new_root = Node(node1, node2, None, 1)
	node1.parent = new_root
	node2.parent = new_root
	increment_depth(node1)
	increment_depth(node2)
	return new_root


def run_steps(n):
	did_explode = True
	did_split = False
	while did_explode or did_split:
		did_explode = explode_if_needed(n, None)
		if not did_explode:
			did_split = split_if_needed(n, None, None)


def part_one():
	nodes = [build_tree(x) for x in data]
	node_sum = nodes[0]
	for i in range(1, len(nodes)):
		node_sum = add_nodes(node_sum, nodes[i])
		run_steps(node_sum)
	return node_sum.get_magnitude()


def part_two():
	curr_max = 0
	for i in range(len(data)):
		for j in range(len(data)):
			if i != j:
				nodes = [build_tree(x) for x in data]			# Need a fresh copy every time, since it gets manipulated...
				new_node_sum = add_nodes(nodes[i], nodes[j])
				run_steps(new_node_sum)
				if new_node_sum.get_magnitude() > curr_max:
					curr_max = new_node_sum.get_magnitude()
	return curr_max


if __name__ == '__main__':
	run_with_timer(part_one)  # 3734 -- took 162 ms
	run_with_timer(part_two)  # 4837 -- took 15149 ms

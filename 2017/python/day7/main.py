import copy
import json
from utils.timers import run_with_timer


class Node:
	def __init__(self, name, weight=-1):
		self.name = name
		self.weight = weight
		self.tower_weight = 0
		self.children = []
		self.parent = None

	def add_child(self, child):
		self.children.append(child)

	def __str__(self):
		return self.name

	def __repr__(self):
		return json.dumps(self.__dict__, default=lambda t: f'{t}')


def get_data(filename):
	tmp = [x.strip().split("->") for x in open(filename).readlines()]
	ret_val = []
	for x in tmp:
		left = x[0].strip().split()
		right = x[1].strip().split(",") if len(x) > 1 else []
		ret_val.append((left[0], int(left[1][1:-1]), right))
	return ret_val


def build_tree(d):
	tree = {}
	for x in d:
		# It was added to the tree already, as a child of something else. Update weight.
		if x[0] in tree:
			disc = tree[x[0]]
			disc.weight = x[1]
		else:
			disc = Node(x[0], x[1])
			tree[disc.name] = disc

		for child in [t.strip() for t in x[2]]:
			if child not in tree:
				tree[child] = Node(child)
			tree[child].parent = disc
			disc.add_child(tree[child])
	return tree, list({k: v for (k, v) in tree.items() if not v.parent}.keys())[0]


def part_one(d):
	return build_tree(d)[1]


def calc_tower_weights(root):
	if len(root.children) == 0:
		root.tower_weight = root.weight
	else:
		root.tower_weight = root.weight + sum(calc_tower_weights(child) for child in root.children)
	return root.tower_weight


def balance_tower(root):
	curr_node = root
	target_weight = -1
	while True:
		weights = [x.tower_weight for x in curr_node.children]
		if max(weights) != min(weights):
			# This tower is the imbalanced one...need to find which specific child is off
			idx = weights.index(min(weights))
			target_weight = max(weights)
			if weights.count(max(weights)) == 1:
				idx = weights.index(max(weights))
				target_weight = min(weights)
			curr_node = curr_node.children[idx]
		else:
			# We've reached the bottom of the imbalance!
			# curr_node.parent.children
			diff = target_weight - curr_node.tower_weight
			return curr_node.weight + diff


def part_two(d):
	tree, root = build_tree(d)
	calc_tower_weights(tree[root])
	return balance_tower(tree[root])


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, copy.deepcopy(data))
	run_with_timer(part_two, copy.deepcopy(data))

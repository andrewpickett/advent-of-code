from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return build_tree([int(x) for x in open(filename).readline().split()])


def part_one(d):
	return meta_sum(d)


def part_two(d):
	return node_value(d)


def meta_sum(elem):
	if len(elem["children"]) == 0:
		return sum(elem["metas"])
	else:
		return sum(meta_sum(i) for i in elem["children"]) + sum(elem["metas"])


def node_value(elem):
	if len(elem["children"]) == 0:
		return sum(elem["metas"])
	else:
		return sum(node_value(elem["children"][i - 1]) for i in elem["metas"] if i <= len(elem["children"]))


def build_tree(vals):
	i = 0
	node_stack = []
	while i < len(vals):
		if len(node_stack) == 0:
			node_stack.append({"c": vals[i], "m": vals[i+1], "children": [], "metas": []})
			i+= 2
		else:
			if node_stack[-1]["c"] > 0:
				if vals[1] == 0:
					node_stack[-1]["children"].append({"c": 0, "m": 0, "children": [], "metas": vals[i+2:i+2+vals[i+1]]})
					i += 2 + vals[i+1]
					node_stack[-1]["c"] -= 1
				else:
					node_stack.append({"c": vals[i], "m": vals[i+1], "children": [], "metas": []})
					i+= 2
			else:
				if node_stack[-1]["m"] == 0:
					node_stack[-2]["c"] -= 1
					node_stack[-2]["children"].append(node_stack.pop(-1))
				else:
					node_stack[-1]["metas"].extend(vals[i:i+node_stack[-1]["m"]])
					i += node_stack[-1]["m"]
					node_stack[-1]["m"] = 0
	return node_stack[0]


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

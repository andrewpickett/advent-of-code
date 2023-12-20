from utils.timers import run_with_timer
import math


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	workflows = {}
	parts = []
	in_workflows = True
	for line in lines:
		if line == "":
			in_workflows = False
			continue
		if in_workflows:
			workflows[line[0:line.find("{")]] = build_workflow(line[line.find("{")+1:-1])
		else:
			parts.append(build_part(line))
	return {"workflows": workflows, "parts": parts}


def build_workflow(line):
	rules = line.split(",")
	new_rules = []
	for rule in rules:
		new_rule = {}
		if rule.find(":") < 0:
			new_rule["dest"] = rule
		else:
			rule_parts = rule.split(":")
			new_rule["dest"] = rule_parts[1]
			comp = "<" if rule_parts[0].find("<") > 0 else ">"
			new_rule["part"] = rule_parts[0][0:rule_parts[0].find(comp)]
			new_rule["comp"] = comp
			new_rule["val"] = int(rule_parts[0][rule_parts[0].find(comp)+1:])
		new_rules.append(new_rule)
	return new_rules


def build_part(line):
	p = line[1:-1].split(",")
	new_obj = {}
	for y in p:
		z = y.split("=")
		new_obj[z[0]] = int(z[1])
	return new_obj


def part_one(d):
	workflows = d["workflows"]
	accepted = []
	rejected = []
	for x in d["parts"]:
		curr_workflow = "in"
		finished = False
		while not finished:
			workflow = workflows[curr_workflow]
			for w in workflow:
				if "part" not in w:
					if w["dest"] == "A":
						accepted.append(x)
						finished = True
					elif w["dest"] == "R":
						rejected.append(x)
						finished = True
					else:
						curr_workflow = w["dest"]
					break
				else:
					if (w["comp"] == ">" and x[w["part"]] > w["val"]) or (w["comp"] == "<" and x[w["part"]] < w["val"]):
						if w["dest"] == "A":
							accepted.append(x)
							finished = True
						elif w["dest"] == "R":
							rejected.append(x)
							finished = True
						else:
							curr_workflow = w["dest"]
						break
	return sum(sum(y for y in x.values()) for x in accepted)


def part_two(d):
	workflows = d["workflows"]
	ranges = [("in", {"x": range(1, 4001), "m": range(1, 4001), "a": range(1, 4001), "s": range(1, 4001)})]
	accept_count = 0
	while len(ranges) > 0:
		i, rs = ranges.pop(0)
		if i == "A":
			accept_count += math.prod([len(v) for v in rs.values()])
		elif i != "R":
			rules = workflows[i]
			for x in rules[:-1]:
				curr_range = rs[x["part"]]
				if x["val"] in curr_range:
					if x["comp"] == ">":
						new_ranges = (range(x["val"]+1, curr_range.stop), range(curr_range.start, x["val"]+1))
					else:
						new_ranges = (range(curr_range.start, x["val"]), range(x["val"], curr_range.stop))
					new_rs = rs.copy()
					new_rs[x["part"]] = new_ranges[0]
					ranges.append((x["dest"], new_rs))
					rs[x["part"]] = new_ranges[1]
			ranges.append((rules[-1]["dest"], rs))
	return accept_count


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	ret_val = {"rules": {}, "updates": []}
	updates = False
	for line in lines:
		if line == "":
			updates = True
			continue
		if not updates:
			parts = list(map(int, line.split("|")))
			if parts[0] not in ret_val["rules"]:
				ret_val["rules"][parts[0]] = set()
			if parts[1] not in ret_val["rules"]:
				ret_val["rules"][parts[1]] = set()
			ret_val["rules"][parts[0]].add(parts[1])
		else:
			ret_val["updates"].append(list(map(int, line.split(","))))
	return ret_val


def part_one(d):
	vm = get_validity(d["rules"], d["updates"])
	return sum(x[len(x) // 2] for x in vm["valid"])


def part_two(d):
	vm = get_validity(d["rules"], d["updates"])
	for u in vm["invalid"]:
		is_valid = False
		while not is_valid:
			is_valid = True
			for j, update in enumerate(u):
				if j == len(u) or set(u[j+1:]).issubset(d["rules"][update]):
					for k in u[:j]:
						if update not in d["rules"][k]:
							is_valid = False
							u[u.index(update)], u[u.index(k)] = u[u.index(k)], u[u.index(update)]
							break
					if not is_valid:
						break
	return sum(x[len(x) // 2] for x in vm["invalid"])


def get_validity(rules, updates):
	valid_map = {"valid": [], "invalid": []}
	for u in updates:
		if check_if_valid(u, rules):
			valid_map["valid"].append(u)
		else:
			valid_map["invalid"].append(u)
	return valid_map


def check_if_valid(updates, rules):
	for j, update in enumerate(updates):
		if j == len(updates) or set(updates[j+1:]).issubset(rules[update]):
			for k in updates[:j]:
				if update not in rules[k]:
					return False
	return True


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

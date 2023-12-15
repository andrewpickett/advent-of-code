from utils.timers import run_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readline().strip().split(",")]


def h_alg(s):
	curr_val = 0
	for x in s:
		curr_val = ((curr_val + ord(x)) * 17) % 256
	return curr_val


def map_contains(bucket, label):
	for i, x in enumerate(bucket):
		if list(x.keys())[0] == label:
			return i
	return -1


def part_one(d):
	return sum(h_alg(x) for x in d)


def part_two(d):
	hashmap = {i: [] for i in range(256)}
	label_objs = {}
	for x in d:
		if "=" in x:
			parts = x.split("=")
			h = h_alg(parts[0])
			o = {parts[0]: int(parts[1])}
			c = map_contains(hashmap[h], parts[0])
			if c < 0:
				hashmap[h].append(o)
			else:
				hashmap[h].pop(c)
				hashmap[h].insert(c, o)
			label_objs[parts[0]] = o
		elif "-" in x:
			label = x[:-1]
			h = h_alg(label)
			if label in label_objs and label_objs[label] in hashmap[h]:
				hashmap[h].remove(label_objs[label])

	return sum((k+1) * (i+1) * list(x.values())[0] for k, v in hashmap.items() for i, x in enumerate(v))


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

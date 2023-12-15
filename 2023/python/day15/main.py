from utils.timers import run_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readline().strip().split(",")]


def hash_alg(s):
	curr_val = 0
	for x in s:
		curr_val += ord(x)
		curr_val *= 17
		curr_val %= 256
	return curr_val


def part_one(d):
	return sum(hash_alg(x) for x in d)


def map_contains(bucket, label):
	for i, x in enumerate(bucket):
		if list(x.keys())[0] == label:
			return i
	return -1


def part_two(d):
	hashmap = {}
	label_objs = {}
	for i in range(256):
		hashmap[i] = []
	for x in d:
		if "=" in x:
			parts = x.split("=")
			h = hash_alg(parts[0])
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
			if label in label_objs and label_objs[label] in hashmap[hash_alg(label)]:
				hashmap[hash_alg(label)].remove(label_objs[label])

	s = 0
	for k, v in hashmap.items():
		for i, x in enumerate(v):
			s += (k+1) * (i+1) * list(x.values())[0]

	return s


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

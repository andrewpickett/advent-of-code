from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	ret_val = {"avail": [], "steps": {}, "reqs": {}, "workers": 5}
	avail = set()
	for line in [x.strip() for x in open(filename).readlines()]:
		parts = line.split()
		if parts[1] not in ret_val["steps"]:
			ret_val["steps"][parts[1]] = []
		if parts[7] not in ret_val["reqs"]:
			ret_val["reqs"][parts[7]] = []
		ret_val["steps"][parts[1]].append(parts[7])
		ret_val["reqs"][parts[7]].append(parts[1])
		avail.add(parts[1])
	for k, v in ret_val["steps"].items():
		for x in v:
			if x in avail:
				avail.remove(x)
	ret_val["avail"] = list(sorted(avail))
	return ret_val


def part_one(d):
	avail = d["avail"].copy()
	path = ""
	while len(avail) > 0:
		next_step = avail.pop(0)
		path += next_step
		if next_step in d["steps"]:
			next_steps = d["steps"][next_step]
			ready_steps = []
			for x in next_steps:
				reqs = d["reqs"][x]
				ready = True
				for y in reqs:
					if y not in path:
						ready = False
						break
				if ready:
					ready_steps.append(x)
			avail.extend(ready_steps)
			avail.sort()
	return path


def part_two(d):
	ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	workers = [None] * d["workers"]
	avail = d["avail"].copy()
	t = 0
	while len(avail) > 0:
		avail.pop(0)
		t += 1
	print(workers)
	return


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

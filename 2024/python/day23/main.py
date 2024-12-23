from utils.timers import run_with_timer, get_data_with_timer

from collections import defaultdict
from collections import deque
from itertools import combinations

def get_data(filename):
	lines = [x.strip().split("-") for x in open(filename).readlines()]
	graph = defaultdict(set)
	for line in lines:
		graph[line[0]].add(line[1])
		graph[line[1]].add(line[0])
	return graph


def part_one(d):
	keys = {tuple(list(sorted([k1, k2, k3]))) for k1 in d for k2 in d[k1]-{k1} for k3 in d[k2]-{k1,k2} if k1 in d[k3]}
	return len({key for key in keys for x in key if x.startswith("t")})


def part_two(d):
	cons = set()
	for k, v in d.items():
		for comp in v:
			cons.add((k, comp))
			cons.add((comp, k))
	comps = list(sorted(d.keys()))
	q = deque([x for x in combinations(comps, 2) if x in cons])
	clique = tuple()
	while len(q) > 0:
		cur = q.popleft()
		if len(cur) > len(clique):
			clique = cur
		for x in comps:
			if x > cur[-1]:
				good = True
				for y in cur:
					if (x, y) not in cons:
						good = False
						break
				if good:
					q.append(cur + tuple([x]))
	return ",".join(sorted(clique))


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

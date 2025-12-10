import z3

from collections import deque

from utils.timers import run_with_timer, get_data_with_timer


def get_data(f):
	lines = [x.strip() for x in f.readlines()]
	machines = []
	for line in lines:
		parts = line.split(" ")
		machines.append({
			"m": {i for i, x in enumerate(parts[0][1:-1]) if x == "#"},
			"b": [{int(z) for z in y.split(',')} for x in parts[1:-1] for y in x[1:-1].split(" ")],
			"j": [int(x) for x in parts[-1][1:-1].split(",")]
		})
	return machines


def part_one(d):
	return sum(button_bfs(x["m"], x["b"]) for x in d)


def button_bfs(target, buttons):
	q = deque()
	q.append((set(), 0))
	visited = set()
	while q:
		curr_set, steps = q.popleft()
		if curr_set == target:
			return steps
		for button in buttons:
			n = frozenset(curr_set ^ button)
			if n not in visited:
				visited.add(n)
				q.append((n, steps + 1))
	return 0


def part_two(d):
	return sum(lp(x["b"], x["j"]) for x in d)

def lp(buttons, joltages):
	s = z3.Optimize()
	button_presses = [z3.Int(f"{i}") for i in range(len(buttons))]
	for i in range(len(buttons)):
		s.add(button_presses[i] >= 0)
	for i in range(len(joltages)):
		s.add(sum(button_presses[j] for j, btn in enumerate(buttons) if i in btn) == joltages[i])

	s.minimize(sum(button_presses))
	if s.check() == z3.sat:
		m = s.model()
		return sum(m[b].as_long() for b in button_presses)
	return 0

def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import DIR_COORDS
import heapq


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	t = tuple(map(int, [x for x in lines[1].split()[1].split(",")]))
	return {"depth": int(lines[0].split()[1]), "target": t, "grid": [[0 for _ in range(t[1]+100)] for _ in range(t[0]+800)]}


def e_level(d, y, x):
	if d["grid"][y][x]:
		return d["grid"][y][x]
	if (y, x) == d["target"]:
		gi = 0
	else:
		gi = x * 16807 if y == 0 else (y * 48271 if x == 0 else e_level(d, y-1, x) * e_level(d, y, x-1))
	d["grid"][y][x] = (gi + d["depth"]) % 20183
	return d["grid"][y][x]


def risk_level(d, y, x):
	return e_level(d, y, x) % 3


def part_one(d):
	return sum(e_level(d, y, x) % 3 for y in range(d["target"][1]+1) for x in range(d["target"][0]+1))


def part_two(d):
	queue = [(0, 0, 0, 1)]
	best = dict()
	target = (d["target"][0], d["target"][1], 1)

	while queue:
		minutes, x, y, c = heapq.heappop(queue)
		best_key = (x, y, c)
		if best_key not in best or minutes < best[best_key]:
			best[best_key] = minutes

			if best_key == target:
				return minutes

			for i in range(3):
				if i != c and i != risk_level(d, y, x):
					heapq.heappush(queue, (minutes + 7, x, y, i))

			for dx, dy in DIR_COORDS:
				newx = x + dx
				newy = y + dy
				if newx >= 0 and newy >= 0 and risk_level(d, newy, newx) != c:
					heapq.heappush(queue, (minutes + 1, newx, newy, c))


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

from aoc_utils import run_with_timer

data = [list(x.strip()) for x in open("input.txt").readlines()]

start_delims = '([{<'
end_delims = ')]}>'
points = [3, 57, 1197, 25137]
closing_points = [1, 2, 3, 4]


def part_one():
	total = 0
	for x in data:
		st = []
		for y in x:
			if y in start_delims:
				st.append(y)
			else:
				if start_delims[end_delims.find(y)] == st[-1]:
					st.pop()
				else:
					total += points[end_delims.find(y)]
					break
	return total


def part_two():
	scores = []
	for x in data:
		corrupt = False
		st = []
		for y in x:
			if y in start_delims:
				st.append(y)
			else:
				if start_delims[end_delims.find(y)] == st[-1]:
					st.pop()
				else:
					corrupt = True
					break
		if not corrupt and len(st) > 0:
			total = 0
			while len(st) > 0:
				p = st.pop()
				total *= 5
				total += closing_points[start_delims.find(p)]
			scores.append(total)
	return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
	run_with_timer(part_one)  # 216297 -- took 5 ms
	run_with_timer(part_two)  # 2165057169 -- took 12 ms

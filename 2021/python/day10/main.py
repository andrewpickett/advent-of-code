from aoc_utils import run_with_timer

data = [list(x.strip()) for x in open("input.txt").readlines()]

START_DELIMS = '([{<'
END_DELIMS = ')]}>'
PTS = {"syntax": [3, 57, 1197, 25137], "autocorrect": [1, 2, 3, 4]}


def analyze_code(code):
	st = []
	syntax_pts = 0
	for y in code:
		if y in START_DELIMS:
			st.append(y)
		else:
			if START_DELIMS[END_DELIMS.find(y)] == st[-1]:
				st.pop()
			else:
				syntax_pts += PTS["syntax"][END_DELIMS.find(y)]
				break
	return syntax_pts, st


def part_one():
	return sum(analyze_code(x)[0] for x in data)


def part_two():
	scores = []
	for x in data:
		syntax_pts, st = analyze_code(x)
		if syntax_pts <= 0 and len(st) > 0:
			total = 0
			while len(st) > 0:
				p = st.pop()
				total *= 5
				total += PTS["autocorrect"][START_DELIMS.find(p)]
			scores.append(total)
	return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
	run_with_timer(part_one)  # 216297 -- took 5 ms
	run_with_timer(part_two)  # 2165057169 -- took 12 ms

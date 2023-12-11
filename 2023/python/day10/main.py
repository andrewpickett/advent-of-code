from utils.timers import run_with_timer


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	vals = []
	for line in lines:
		next_line = ["."]
		next_line.extend(list(line))
		next_line.append(".")
		vals.append(next_line)
	vals.insert(0, ["."]*len(vals[0]))
	vals.append(["."]*len(vals[0]))
	return vals


tmp = {
	"NW": "F",
	"EN": "7",
	"SW": "L",
	"ES": "J",
	"NS": "|",
	"EW": "-"
}


def take_step(d, c, from_dir):
	next_point = None
	if c[2] == "|":
		next_point = ((c[0]-1, c[1], d[c[0]-1][c[1]]), "S") if from_dir == "S" else ((c[0]+1, c[1], d[c[0]+1][c[1]]), "N")
	elif c[2] == "-":
		next_point = ((c[0], c[1]+1, d[c[0]][c[1]+1]), "W") if from_dir == "W" else ((c[0], c[1]-1, d[c[0]][c[1]-1]), "E")
	elif c[2] == "7":
		next_point = ((c[0], c[1]-1, d[c[0]][c[1]-1]), "E") if from_dir == "S" else ((c[0]+1, c[1], d[c[0]+1][c[1]]), "N")
	elif c[2] == "F":
		next_point = ((c[0], c[1]+1, d[c[0]][c[1]+1]), "W") if from_dir == "S" else ((c[0]+1, c[1], d[c[0]+1][c[1]]), "N")
	elif c[2] == "L":
		next_point = ((c[0], c[1]+1, d[c[0]][c[1]+1]), "W") if from_dir == "N" else ((c[0]-1, c[1], d[c[0]-1][c[1]]), "S")
	elif c[2] == "J":
		next_point = ((c[0], c[1]-1, d[c[0]][c[1]-1]), "E") if from_dir == "N" else ((c[0]-1, c[1], d[c[0]-1][c[1]]), "S")
	return next_point


def get_path(d):
	curr_point = None
	from_dir = ""
	for i, row in enumerate(d):
		if 0 < i < len(d):
			for j, col in enumerate(row):
				if 0 < j < len(row):
					if d[i][j] == "S":
						dirs = []
						if d[i-1][j] in ["|", "7", "F"]:
							dirs.append(((i-1, j), "S"))
						if d[i+1][j] in ["|", "J", "L"]:
							dirs.append(((i+1, j), "N"))
						if d[i][j-1] in ["-", "L", "F"]:
							dirs.append(((i, j-1), "E"))
						if d[i][j+1] in ["-", "7", "J"]:
							dirs.append(((i, j+1), "W"))
						start_val = tmp[''.join(list(sorted([x[1] for x in dirs])))]
						curr_point = (i, j, start_val)
						if start_val in ["7", "-", "J"]:
							from_dir = "W"
						elif start_val in ["|", "L"]:
							from_dir = "N"
						elif start_val in ["F"]:
							from_dir = "S"
						break
	curr_point = (curr_point, from_dir)
	path = []
	while curr_point and curr_point[0] not in path:
		path.append(curr_point[0])
		curr_point = take_step(d, curr_point[0], curr_point[1])
	return path


def part_one(d):
	return len(get_path(d)) // 2


def part_two(d):
	path = get_path(d)
	t = 0
	for i, row in enumerate(d):
		if 0 < i < len(d):
			crossings = 0
			sf = False
			sl = False
			for j, col in enumerate(row):
				if 0 < j < len(row):
					pt = (i, j, col)
					in_path = pt in path
					if not in_path:
						if (sl or sf) and col != "-":
							sf = False
							sl = False
						elif crossings % 2 == 1:
							t += 1
					else:
						if col == "|" or (col == "J" and sf) or (col == "7" and sl):
							crossings += 1
							sf = False
							sl = False
						elif col == "F":
							sf = True
							sl = False
						elif col == "L":
							sf = False
							sl = True
						elif (sl or sf) and col != "-":
							sf = False
							sl = False
	return t


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

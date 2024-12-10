DIRS = {
	"U": (-1, 0),
	"N": (-1, 0),
	"^": (-1, 0),
	"UL": (-1, -1),
	"NW": (-1, -1),
	"UR": (-1, 1),
	"NE": (-1, 1),
	"D": (1, 0),
	"S": (1, 0),
	"v": (1, 0),
	"DL": (1, -1),
	"SW": (1, -1),
	"DR": (1, 1),
	"SE": (1, 1),
	"L": (0, -1),
	"W": (0, -1),
	"<": (0, -1),
	"R": (0, 1),
	"E": (0, 1),
	">": (0, 1)
}

DIR_LOOKUP = {
	(-1, 0): "^",
	(1, 0): "v",
	(0, -1): "<",
	(0, 1): ">"
}

DIR_TURNS = {
	DIRS["U"]: {"L": DIRS["L"], "R": DIRS["R"], "B": DIRS["D"]},
	DIRS["L"]: {"L": DIRS["D"], "R": DIRS["U"], "B": DIRS["R"]},
	DIRS["D"]: {"L": DIRS["R"], "R": DIRS["L"], "B": DIRS["U"]},
	DIRS["R"]: {"L": DIRS["U"], "R": DIRS["D"], "B": DIRS["L"]}
}

DIR_COORDS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

NEIGHBOR_COORDS = {
	"orthogonal": [(-1, 0), (0, 1), (1, 0), (0, -1)],
	"diagonal": [(-1, -1), (-1, 1), (1, -1), (1, 1)]
}


def turn_right(curr_dir):
	return DIR_TURNS[curr_dir]["R"]


def turn_left(curr_dir):
	return DIR_TURNS[curr_dir]["L"]


def turn_around(curr_dir):
	return DIR_TURNS[curr_dir]["B"]


def neighbors(grid, curr_pos, condition=lambda grid, curr, n: True, include_diagonals=False):
	ns = NEIGHBOR_COORDS["orthogonal"]
	if include_diagonals:
		ns.extend(NEIGHBOR_COORDS["diagonal"])
	return [(z[0], z[1], grid[z[0]][z[1]]) for z in tuple_add(ns, (curr_pos[0], curr_pos[1])) if condition(grid, curr_pos, z)]


def tuple_add(array_of_tuples, scalar_tuple):
	if array_of_tuples is None:
		return None
	if len(array_of_tuples[0]) != len(scalar_tuple):
		raise ValueError("Tuples must have same length")
	return [tuple(a+b for a, b in zip(t, scalar_tuple)) for t in array_of_tuples]


def tuple_multiply(array_of_tuples, scalar_tuple):
	if array_of_tuples is None:
		return None
	if len(array_of_tuples[0]) != len(scalar_tuple):
		raise ValueError("Tuples must have same length")
	return [tuple(a*b for a, b in zip(t, scalar_tuple)) for t in array_of_tuples]

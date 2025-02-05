DIRS = {
	"U": (-1, 0),
	"N": (-1, 0),
	"^": (-1, 0),
	"D": (1, 0),
	"S": (1, 0),
	"v": (1, 0),
	"L": (0, -1),
	"W": (0, -1),
	"<": (0, -1),
	"R": (0, 1),
	"E": (0, 1),
	">": (0, 1)
}

DIR_COORDS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def turn_right(curr_dir):
	if curr_dir == DIRS["U"]:
		return DIRS["R"]
	elif curr_dir == DIRS["R"]:
		return DIRS["D"]
	elif curr_dir == DIRS["D"]:
		return DIRS["L"]
	elif curr_dir == DIRS["L"]:
		return DIRS["U"]


def turn_left(curr_dir):
	if curr_dir == DIRS["U"]:
		return DIRS["L"]
	elif curr_dir == DIRS["L"]:
		return DIRS["D"]
	elif curr_dir == DIRS["D"]:
		return DIRS["R"]
	elif curr_dir == DIRS["R"]:
		return DIRS["U"]


def turn_around(curr_dir):
	if curr_dir == DIRS["U"]:
		return DIRS["D"]
	elif curr_dir == DIRS["L"]:
		return DIRS["R"]
	elif curr_dir == DIRS["D"]:
		return DIRS["U"]
	elif curr_dir == DIRS["R"]:
		return DIRS["L"]

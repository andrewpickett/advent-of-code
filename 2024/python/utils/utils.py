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

DIR_COORDS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_input_as_2d_int_array(file, pad_size=0, pad_val=-1):
	lines = [x.strip() for x in open(file).readlines()]
	if pad_size > 0:
		ret_val = []
		ns_pad = [[pad_val] * (len(lines[0])+(2*pad_size)) for _ in range(pad_size)]
		ret_val.extend(ns_pad.copy())
		ret_val.extend([[pad_val] * pad_size + list(map(int, [y for y in x])) + [pad_val] * pad_size for x in lines])
		ret_val.extend(ns_pad.copy())
		return ret_val
	else:
		return [list(map(int, [y for y in x])) for x in lines]


def read_input_as_2d_str_array(file, pad_size=0, pad_val="."):
	lines = [x.strip() for x in open(file).readlines()]
	if pad_size > 0:
		ret_val = []
		ns_pad = [[pad_val] * (len(lines[0])+(2*pad_size)) for _ in range(pad_size)]
		ret_val.extend(list(ns_pad))
		ret_val.extend([list(x) for x in [pad_val * pad_size + x + pad_val * pad_size for x in lines]])
		ret_val.extend(list(ns_pad))
		return ret_val
	else:
		return [list(x) for x in lines]


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

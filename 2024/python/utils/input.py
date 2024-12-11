def read_input_as_int_arrays(file):
	return [list(map(int, x.strip().split())) for x in open(file).readlines()]


def read_input_as_2d_int_grid(file, pad_size=0, pad_val=-1):
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


def read_input_as_2d_str_grid(file, pad_size=0, pad_val="."):
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

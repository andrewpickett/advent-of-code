from aoc_utils import run_with_timer

data = [x for x in open("input.txt").readline().strip()]


def get_piece(key):
	match key:
		case "-":
			return {
				"start": 2,
				"height": 1,
				"width": 4,
				"rows": [
					[True, True, True, True]
				]
			}
		case "+":
			return {
				"start": 2,
				"height": 3,
				"width": 3,
				"rows": [
					[False, True, False],
					[True, True, True],
					[False, True, False],
				]
			}
		case "L":
			return {
				"start": 2,
				"height": 3,
				"width": 3,
				"rows": [
					[False, False, True],
					[False, False, True],
					[True, True, True],
				]
			}
		case "|":
			return {
				"start": 2,
				"height": 4,
				"width": 1,
				"rows": [
					[True],
					[True],
					[True],
					[True],
				]
			}
		case "#":
			return {
				"start": 2,
				"height": 2,
				"width": 2,
				"rows": [
					[True, True],
					[True, True],
				]
			}


pieces = ["-", "+", "L", "|", "#"]


def print_cavern(cavern, print_floor=True):
	for x in cavern:
		print("|" + ''.join(["#" if y else "." for y in x]) + "|")
	if print_floor:
		print("+-------+")


# we can just move the piece down and shift right away.
def get_next_piece(move_counter, piece):
	for i in range(3):
		d = data[(move_counter + i) % len(data)]
		if d == "<" and piece["start"] > 0:
			piece["start"] -= 1
		elif d == ">" and piece["start"] < 7-piece["width"]:
			piece["start"] += 1
	new_rows = []
	for x in piece["rows"]:
		new_row = [False] * piece["start"]
		new_row.extend(x)
		new_row.extend([False] * (7-len(x)-piece["start"]))
		new_rows.insert(0, new_row)
	return new_rows


def move_horiz(cavern, piece, move_counter, vert_pos):
	d = data[move_counter % len(data)]
	space = cavern[vert_pos:vert_pos+piece["height"]]
	new_space = []
	if d == "<" and piece["start"] > 0:
		for i in space:
			num_blocks = i.count(True)
			new_row = [x for x in i]
			for j in range(piece["start"]-1, piece["start"] + piece["width"], 1):
				if j < len(i)-1:
					new_row[j] = new_row[j + 1]
			new_row[piece["start"] + piece["width"]-1] = False
			if num_blocks != new_row.count(True):
				return False
			new_space.append(new_row)
		piece["start"] -= 1
	elif d == ">" and piece["start"] < 7-piece["width"]:
		for i in space:
			num_blocks = i.count(True)
			new_row = [x for x in i]
			for j in range(piece["start"] + piece["width"], piece["start"], -1):
				new_row[j] = new_row[j - 1]
			new_row[piece["start"]] = False
			if num_blocks != new_row.count(True):
				return False
			new_space.append(new_row)
		piece["start"] += 1
	for i in range(len(new_space)):
		cavern[vert_pos+i] = new_space[i]
	return True


def move_vertical(cavern, piece, vert_pos):
	if vert_pos + piece["height"] == len(cavern):
		return False
	space = cavern[vert_pos:vert_pos + piece["height"] + 1]
	new_space = [x for x in space]
	for i in range(len(space) - 1, 0, -1):
		new_line = [x for x in new_space[i][piece["start"]:piece["start"] + piece["width"]]]
		prev_line = [x for x in new_space[i - 1][piece["start"]:piece["start"] + piece["width"]]]

		new_line = [(new_line[i] and prev_line[i]) for i in range(piece["width"])]
		if True in new_line:
			return False
		else:
			new_line = new_space[i][0:piece["start"]]
			new_line.extend(space[i - 1][piece["start"]:piece["start"] + piece["width"]])
			new_line.extend(space[i][piece["start"] + piece["width"]:])
			prev_line = new_space[i-1][0:piece["start"]]
			prev_line.extend([False]*piece["width"])
			prev_line.extend(space[i-1][piece["start"] + piece["width"]:])
			new_space[i] = new_line
			new_space[i-1] = prev_line
	for i in range(len(space)):
		cavern[vert_pos + i] = new_space[i]
	return True


def part_one():
	cavern = []
	move_counter = 0
	for i in range(2022):
		next_piece = get_piece(pieces[i % len(pieces)])
		new_piece_rows = get_next_piece(move_counter, next_piece)
		for x in new_piece_rows:
			cavern.insert(0, x)
		move_counter += 3

		moved = True
		vert_pos = -1
		while moved:
			vert_pos += 1
			# Move horizontal if possible
			move_horiz(cavern, next_piece, move_counter, vert_pos)
			move_counter += 1
			# Move down if possible
			moved = move_vertical(cavern, next_piece, vert_pos)
		# print_cavern(cavern)
		# print()

		# Remove any rows that are blank
		while True not in cavern[0]:
			cavern.pop(0)
	return len(cavern)


def part_two():
	return


if __name__ == '__main__':
	run_with_timer(part_one)  #
	# run_with_timer(part_two)  #

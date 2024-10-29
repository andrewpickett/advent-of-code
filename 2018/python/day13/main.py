from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import DIRS
from copy import deepcopy

TURNS = {
	"/": {"v": "<", ">": "^", "<": "v", "^": ">"},
	"\\": {"v": ">", ">": "v", "<": "^", "^": "<"},
	"+": {
		"^": ["<", "^", ">"],
		">": ["^", ">", "v"],
		"v": [">", "v", "<"],
		"<": ["v", "<", "^"]}
}


def get_data(filename):
	ret_val = {"tracks": [[y for y in x] for x in open(filename).readlines()], "carts": [], "collisions": []}
	for y, row in enumerate(ret_val["tracks"]):
		for x, col in enumerate(row):
			if col in [">", "<", "^", "v"]:
				ret_val["carts"].append((y, x, col, 0))
				if col in ["v", "^"]:
					ret_val["tracks"][y][x] = "|"
				elif col in [">", "<"]:
					ret_val["tracks"][y][x] = "-"
	return ret_val


def part_one(d):
	while not move_carts(d):
		d["carts"].sort()
	return "{},{}".format(d["collisions"][0][0], d["collisions"][0][1])


def part_two(d):
	while len(d["carts"]) > 1:
		d["carts"].sort()
		move_carts(d)
	return "{},{}".format(d["collisions"][0][0], d["collisions"][0][1]) if len(d["carts"]) == 0 else "{},{}".format(d["carts"][0][1], d["carts"][0][0])


def move_carts(d):
	ci = 0
	while ci < len(d["carts"]):
		cart = d["carts"].pop(ci)
		next_y = cart[0] + DIRS[cart[2]][0]
		next_x = cart[1] + DIRS[cart[2]][1]
		next_counter = cart[3]
		if d["tracks"][next_y][next_x] == "+":
			next_counter = (cart[3] + 1) % 3

		new_cart = (next_y, next_x, turn(cart[2], d["tracks"][next_y][next_x], cart[3]), next_counter)
		i = check_collisions(new_cart, d["carts"])
		if i is not None:
			d["carts"].pop(i)
			d["collisions"].append((next_x, next_y))
			if i < ci:
				ci -= 1
		else:
			d["carts"].insert(0, new_cart)
			ci += 1
	return len(d["collisions"]) > 0


def check_collisions(new_cart, other_carts):
	for i, x in enumerate(other_carts):
		if new_cart[0] == x[0] and new_cart[1] == x[1]:
			return i
	return None


def turn(curr_dir, track, counter):
	if track in ["/", "\\"]:
		return TURNS[track][curr_dir]
	elif track == "+":
		return TURNS[track][curr_dir][counter]
	else:
		return curr_dir


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, deepcopy(data))
	run_with_timer(part_two, deepcopy(data))


if __name__ == '__main__':
	main()

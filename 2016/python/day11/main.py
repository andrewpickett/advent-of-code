from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]

# def parse_input(d):
# 	elevator_floor = 0
# 	floors = [["PG", "PM"], ["CG", "UG", "RG", "PG"], ["CM", "UM", "RM", "PM"], []]
# 	for i, x in enumerate(d):
# 		if "nothing relevant" not in x:
# 			parts = x.split(" ")
# 			for j, y in enumerate(parts):
# 				if y == "a":
# 					part = (parts[j+1][0:3] + " " + parts[j+2][0:3]).upper()
# 					if part.endswith(".") or part.endswith(","):
# 						part = part[:-1]
# 					floors[i].append(part)
# 	return floors

def find_valid_two_up(current_floor, target):
	pass


def part_one(d):
	# floors = parse_input(d)
	# print(floors)
	# floors = [{"g": ["p"], "m": ["p"]}, {"g": ["c", "u", "r", "l"], "m": []}, {"g": [], "m": ["c", "u", "r", "l"]}, {"g": [], "m": []}]
	floors = [{"g": [], "m": ["h", "l"]}, {"g": ["h"], "m": []}, {"g": [], "m": ["l"]}, {"g": [], "m": []}]
	curr_floor = 0
	move_count = 0
	# while len(floors[0]) != 0 or len(floors[1]) != 0 or len(floors[2]) != 0:
		# Elevator can only move with 1 or 2 items (either type)
		# can't move mixed M and Gs of different types together
		# M and G on the same floor without matching the M and G is not allowed
		# if I ever "undo" a move I just did, then stop that branch (if recursing)??

		# assumptions:
			# best to move 2 up if possible
			# never move 2 down

		# Find all valid 2 up moves...then find all valid 1 up moves...then find all valid 1 down moves

		# What is a "move" -- it is a target floor, and 1 or 2 elements

		# move_count += 1
	return move_count


def part_two(d):
	return


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

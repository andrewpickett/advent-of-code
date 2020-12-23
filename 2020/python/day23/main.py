from aoc_utils import run_with_timer

data = [int(x) for x in open("input.txt").readline().strip()]


def play_round(game_board, rounds):
	for i in range(rounds):
		next_pickup = [x for x in game_board[1:4]]
		for x in next_pickup:
			game_board.remove(x)
		dest_cup = game_board[0] - 1
		while dest_cup in next_pickup or dest_cup < min(game_board):
			dest_cup -= 1
			if dest_cup < min(game_board):
				dest_cup = max(game_board)
		drop_idx = game_board.index(dest_cup)
		for x in list(reversed(next_pickup)):
			game_board.insert(drop_idx+1, x)
		game_board.append(game_board.pop(0))
	return game_board


def part_one():
	final_board = play_round(data.copy(), 100)
	start = final_board.index(1)
	return ''.join([str(x) for x in list(final_board[start+1:] + final_board[:start])])


def part_two():
	num_cups = 1000000
	game_board = data + [x for x in range(max(data)+1, num_cups+1)]

	# Create a doubly linked list, with the node element, pointer to next, and pointer to previous nodes.
	head = {"val": data[0], "previous": None, "next": None}
	previous = head
	for i in game_board[1:]:
		node = {"val": i, "previous": previous, "next": None}
		previous["next"] = node
		previous = node
	# Handle ends of the list (wrap around)
	head["previous"] = previous
	previous["next"] = head

	# Maps are going to be quicker to look up than arrays for finding the destination...so create a lookup map.
	cups = {}
	curr = head
	for i in range(num_cups):
		cups[curr["val"]] = curr
		curr = curr["next"]

	for i in range(10000000):
		picked_cards = [curr["next"], curr["next"]["next"], curr["next"]["next"]["next"]]
		# Effectively REMOVE those three elements by updating points to skip over them.
		curr["next"] = curr["next"]["next"]["next"]["next"]
		curr["next"]["previous"] = curr

		# Get the destination cup
		picked_vals = [x["val"] for x in picked_cards]
		dest_val = (curr["val"] - 1) % num_cups
		if dest_val == 0:
			dest_val = num_cups
		while dest_val in picked_vals:
			dest_val = (dest_val - 1) % num_cups
			if dest_val == 0:
				dest_val = num_cups
		dest_cup = cups[dest_val]

		# Alright, now just adjust pointers to re-insert the picked values.
		picked_cards[2]["next"] = dest_cup["next"]
		picked_cards[2]["next"]["previous"] = picked_cards[2]
		dest_cup["next"] = picked_cards[0]
		picked_cards[0]["previous"] = dest_cup

		# NEXT!
		curr = curr["next"]
	return cups[1]["next"]["val"] * cups[1]["next"]["next"]["val"]


if __name__ == '__main__':
	run_with_timer(part_one)  # 82934675 -- took 0 ms
	run_with_timer(part_two)  # 474600314018 -- took 22712 ms

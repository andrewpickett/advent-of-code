from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]

even_map = {"e": (1, 0), "w": (-1, 0), "ne": (1, -1), "nw": (0, -1), "se": (1, 1), "sw": (0, 1)}
odd_map = {"e": (1, 0), "w": (-1, 0), "ne": (0, -1), "nw": (-1, -1), "se": (0, 1), "sw": (-1, 1)}


def get_tile_map(tile):
	return even_map if tile[1] % 2 == 0 else odd_map


def get_black_tiles():
	black_tiles = set()
	for x in data:
		pos = (0, 0)
		while len(x) > 0:
			dir = x[:2] if x[0] in ('s', 'n') else x[:1]
			x = x[len(dir):]

			m = get_tile_map(pos)
			pos = (pos[0] + m[dir][0], pos[1] + m[dir][1])

		if pos in black_tiles:
			black_tiles.remove(pos)
		else:
			black_tiles.add(pos)
	return black_tiles


def get_neighbors(tile):
	return {(tile[0] + x[0], tile[1] + x[1]) for x in get_tile_map(tile).values()}


def perform_flip(black_tiles):
	flip_to_white = set()
	flip_to_black = set()
	visited_white_tiles = set()
	for tile in black_tiles:
		tile_neighbors = get_neighbors(tile)
		adjacent_black_tiles = tile_neighbors.intersection(black_tiles)
		if len(adjacent_black_tiles) == 0 or len(adjacent_black_tiles) > 2:
			flip_to_white.add(tile)
		adjacent_white_tiles = tile_neighbors.difference(black_tiles)
		for wt in adjacent_white_tiles:
			if wt not in visited_white_tiles:
				visited_white_tiles.add(wt)
				wt_neighbors = get_neighbors(wt)
				wt_adjacent_black = wt_neighbors.intersection(black_tiles)
				if len(wt_adjacent_black) == 2:
					flip_to_black.add(wt)
	return black_tiles.union(flip_to_black).difference(flip_to_white)


def part_one():
	return len(get_black_tiles())


def part_two():
	black_tiles = get_black_tiles()
	for i in range(100):
		black_tiles = perform_flip(black_tiles)
	return len(black_tiles)


if __name__ == '__main__':
	run_with_timer(part_one)  # 512 -- took 9 ms
	run_with_timer(part_two)  # 4120 -- took 1800 ms

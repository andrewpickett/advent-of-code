import math
from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def get_tiles_as_binary():
	tiles = {}
	curr_tile = None
	for x in data:
		if 'Tile' in x:
			curr_tile = ''.join(x.split()[1][:-1])
			tiles[curr_tile] = []
		elif '' != x:
			tiles[curr_tile].append(x.replace('#', '1').replace('.', '0'))
	return tiles


def get_edge_values(tiles):
	edge_values = {}
	for k, v in tiles.items():
		edge_values[k] = [
			int(v[0], 2),											# top
			int(''.join([x[-1] for x in v]), 2),			# right
			int(v[-1], 2),											# bottom
			int(''.join([x[0] for x in v]), 2),				# left
			int(v[0][::-1], 2),									# top reversed
			int(''.join([x[-1] for x in v])[::-1], 2),	# right reversed
			int(v[-1][::-1], 2),									# bottom reversed
			int(''.join([x[0] for x in v])[::-1], 2),		# left reversed
		]
	return edge_values


def find_corners(edge_vals):
	return [int(k) for k, v in edge_vals.items() if sum(1 for x in v[:4] for k2, v2 in edge_vals.items() if k2 != k and x in v2) == 2]


def part_one():
	return math.prod(corner for corner in find_corners(get_edge_values(get_tiles_as_binary())))


def part_two():
	pass


if __name__ == '__main__':
	run_with_timer(part_one)  # 7492183537913 -- took 48 ms
	run_with_timer(part_two)  #

import math
from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]
sea_monster = [(18, -1), (0, 0), (5, 0), (6, 0), (11, 0), (12, 0), (17, 0), (18, 0), (19, 0), (1, 1), (4, 1), (7, 1), (10, 1), (13, 1), (16, 1)]


class Tile:
	NEIGHBOR_IDX = ["top", "right", "bottom", "left"]

	def __init__(self, name, d):
		self.name = int(name)
		self.data = d
		self.neighbors = {"top":None, "right":None, "bottom":None, "left":None}

	def __str__(self):
		return Tile.to_string(self)

	def copy(self):
		return Tile(self.name, self.data.copy())

	@staticmethod
	def to_string(tile):
		return '\n'.join([''.join(x) for x in tile.data])

	def add_neighbor(self, idx, neighbor):
		self.neighbors[self.NEIGHBOR_IDX[idx]] = neighbor

	def get_neighbor(self, idx):
		return self.neighbors[self.NEIGHBOR_IDX[idx]]

	def rotate(self):
		self.data = list(zip(*self.data[::-1]))
		tmp = self.neighbors["top"]
		self.neighbors["top"] = self.neighbors["left"]
		self.neighbors["left"] = self.neighbors["bottom"]
		self.neighbors["bottom"] = self.neighbors["right"]
		self.neighbors["right"] = tmp

	def flip_vertical(self):
		self.data = list(reversed(self.data))
		tmp = self.neighbors["top"]
		self.neighbors["top"] = self.neighbors["bottom"]
		self.neighbors["bottom"] = tmp

	def flip_horizontal(self):
		for i in range(len(self.data)):
			self.data[i] = self.data[i][::-1]
		tmp = self.neighbors["left"]
		self.neighbors["left"] = self.neighbors["right"]
		self.neighbors["right"] = tmp

	def remove_edges(self):
		self.data = [[y for y in x[1:-1]] for x in self.data[1:-1]]

	def get_edge(self, edge):
		if edge == 'top':
			return self.top_edge()
		elif edge == 'bottom':
			return self.bottom_edge()
		elif edge == 'left':
			return self.left_edge()
		elif edge == 'right':
			return self.right_edge()

	def all_edges(self):
		return self.edges() + self.rotated_edges()

	def edges(self):
		return self.top_edge(), self.right_edge(), self.bottom_edge(), self.left_edge()

	def rotated_edges(self):
		return self.top_edge()[::-1], self.right_edge()[::-1], self.bottom_edge()[::-1], self.left_edge()[::-1]

	def top_edge(self):
		return self.data[0]

	def bottom_edge(self):
		return self.data[-1]

	def right_edge(self):
		return tuple([x[-1] for x in self.data])

	def left_edge(self):
		return tuple([x[0] for x in self.data])

	def contains_edge(self, edge):
		return self.top_edge() == edge or self.bottom_edge() == edge or self.left_edge() == edge or self.right_edge == edge


def get_tiles():
	tiles = {}
	curr_tile = None
	for x in data:
		if 'Tile' in x:
			curr_tile = ''.join(x.split()[1][:-1])
			tiles[curr_tile] = []
		elif '' != x:
			tiles[curr_tile].append(tuple(list(x)))
	for id, tile in tiles.items():
		tiles[id] = Tile(id, tiles[id])
	return tiles


def part_one():
	# This is what I USED to have before I rewrote it.
	# 		return math.prod(corner for corner in find_corners(get_edge_values(get_tiles_as_binary())))

	# Now it is this.
	tiles = get_tiles()
	corners = [t for k, t in tiles.items() if sum(1 for edge in t.edges() for tile in tiles.values() if t != tile and edge in tile.all_edges()) == 2]
	return math.prod(t.name for t in corners)


def get_neighbors_for_tile(tile: Tile, tiles):
	for i, edge in enumerate(tile.edges()):
		for k, t in tiles.items():
			if t.name != tile.name and edge in t.all_edges():
				tile.add_neighbor(i, t.copy())


def rotate_until_aligned(tile, tile_edge, fixed_edge):
	counter = 0
	aligned = tile.get_edge(tile_edge) == fixed_edge
	while counter < 4 and not aligned:
		tile.rotate()
		counter += 1
		aligned = tile.get_edge(tile_edge) == fixed_edge
	return aligned


def align_tile(tile, tile_edge, fixed_edge):
	aligned = rotate_until_aligned(tile, tile_edge, fixed_edge)
	if not aligned:
		tile.flip_horizontal()
		aligned = rotate_until_aligned(tile, tile_edge, fixed_edge)
		if not aligned:
			tile.flip_vertical()
			aligned = rotate_until_aligned(tile, tile_edge, fixed_edge)
			if not aligned:
				tile.flip_horizontal()
				aligned = rotate_until_aligned(tile, tile_edge, fixed_edge)
	return aligned


def flatten_image(image):
	width = int(math.sqrt(len(image)))
	full_image = []
	for i in range(width):
		for j in range(len(image[0].data)):
			next_line = ''
			for k in range(width):
				next_line += ''.join(list(image[i*width+k].data[j]))
			full_image.append(next_line)
	return full_image


def find_sea_monsters(full_image):
	total_count = 0
	for i, x in enumerate(full_image):
		if 0 < i < len(full_image) - 1:
			for j in range(len(x)-20):
				if x[j] == '#':
					# Found a possible tail. Check all points of interest. If all are "#", then we're good.
					found = True
					for p in sea_monster:
						if full_image[i+p[1]][j+p[0]] != '#':
							found = False
							break
					if found:
						total_count += 1
	return total_count


def part_two():
	tiles = get_tiles()
	image = [None] * len(tiles)
	corners = [t for k, t in tiles.items() if sum(1 for edge in t.edges() for tile in tiles.values() if t != tile and edge in tile.all_edges()) == 2]
	c = corners[0]
	get_neighbors_for_tile(c, tiles)
	while not c.neighbors["right"] or not c.neighbors["bottom"]:
		c.rotate()
	get_neighbors_for_tile(c, tiles)
	# At this point, I have the upper left tile image in place.
	idx = 0
	image[idx] = c
	idx += 1
	# Take the right neighbor and orient it correctly.
	first_in_row = c
	while idx < len(image):
		while c.neighbors['right']:
			next_tile = tiles[str(c.neighbors['right'].name)]
			align_tile(next_tile, "left", c.right_edge())
			get_neighbors_for_tile(next_tile, tiles)
			image[idx] = next_tile
			idx += 1
			c = next_tile
		if first_in_row.neighbors['bottom']:
			next_tile = tiles[str(first_in_row.neighbors['bottom'].name)]
			align_tile(next_tile, "top", first_in_row.bottom_edge())
			get_neighbors_for_tile(next_tile, tiles)
			image[idx] = next_tile
			idx += 1
			first_in_row = next_tile
			c = next_tile

	# Remove the borders
	for x in image:
		x.remove_edges()

	# Now combine the images into one giant array
	full_image = flatten_image(image)

	# Check all rotations for sea monsters.
	num_sea_monsters = 0
	counter = 0
	while counter < 4 and num_sea_monsters == 0:
		full_image = list(zip(*full_image[::-1]))
		num_sea_monsters = find_sea_monsters(full_image)
		counter += 1
	if num_sea_monsters == 0:
		counter = 0
		full_image = list(reversed(full_image))
		while counter < 4 and num_sea_monsters == 0:
			full_image = list(zip(*full_image[::-1]))
			num_sea_monsters = find_sea_monsters(full_image)
			counter += 1
		if num_sea_monsters == 0:
			counter = 0
			full_image = list(reversed(full_image))
			while counter < 4 and num_sea_monsters == 0:
				for i in range(len(full_image)):
					full_image[i] = full_image[i][::-1]
				num_sea_monsters = find_sea_monsters(full_image)
				counter += 1

	# total number of "#" - (number of sea monsters * number of "#" per sea monster)
	return sum(x.count("#") for x in full_image) - (num_sea_monsters * len(sea_monster))


if __name__ == '__main__':
	run_with_timer(part_one)  # 7492183537913 -- took 48 ms
	run_with_timer(part_two)  # 2323 -- took 1105 ms


# These methods are no longer used, as I removed them when I rewrote it...but keeping them because I liked it.
# def get_tiles_as_binary():
# 	tiles = {}
# 	curr_tile = None
# 	for x in data:
# 		if 'Tile' in x:
# 			curr_tile = ''.join(x.split()[1][:-1])
# 			tiles[curr_tile] = []
# 		elif '' != x:
# 			tiles[curr_tile].append(x.replace('#', '1').replace('.', '0'))
# 	return tiles
#
#
# def get_edge_values(tiles):
# 	edge_values = {}
# 	for k, v in tiles.items():
# 		edge_values[k] = [
# 			int(v[0], 2),											# top
# 			int(''.join([x[-1] for x in v]), 2),			# right
# 			int(v[-1], 2),											# bottom
# 			int(''.join([x[0] for x in v]), 2),				# left
# 			int(v[0][::-1], 2),									# top reversed
# 			int(''.join([x[-1] for x in v])[::-1], 2),	# right reversed
# 			int(v[-1][::-1], 2),									# bottom reversed
# 			int(''.join([x[0] for x in v])[::-1], 2),		# left reversed
# 		]
# 	return edge_values
#
#
# def find_corners(edge_vals):
# 		return [int(k) for k, v in edge_vals.items() if sum(1 for x in v[:4] for k2, v2 in edge_vals.items() if k2 != k and x in v2) == 2]
#
#

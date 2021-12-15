import sys
from aoc_utils import run_with_timer, Grid

data = [list(x.strip()) for x in open("input.txt").readlines()]


def h(point):
	return int(point.get_value())


def a_star(start, end):
	open_nodes = set([start])
	closed_nodes = set()

	shortest_distances = {start: 0}

	dest_node = start
	while dest_node != end:
		current_lowest_node = None
		for next_node in open_nodes:
			if current_lowest_node is None or shortest_distances[next_node] + h(next_node) < shortest_distances[current_lowest_node] + h(current_lowest_node):
				current_lowest_node = next_node

		if current_lowest_node == end:
			return shortest_distances[end]

		for neighbor in current_lowest_node.get_neighbors():
			if neighbor not in open_nodes and neighbor not in closed_nodes:
				open_nodes.add(neighbor)
				shortest_distances[neighbor] = shortest_distances[current_lowest_node] + int(neighbor.get_value())
			elif shortest_distances[current_lowest_node] + int(neighbor.get_value()) < shortest_distances[neighbor]:
				shortest_distances[neighbor] = shortest_distances[current_lowest_node] + int(neighbor.get_value())
				if neighbor in closed_nodes:
					closed_nodes.remove(neighbor)
					open_nodes.add(neighbor)

		open_nodes.remove(current_lowest_node)
		closed_nodes.add(current_lowest_node)


# Not used anymore, as it was WAY too slow...
def dijkstra(grid, start, end):
	shortest_distances = {}
	unvisited_nodes = grid.get_points()
	for pt in unvisited_nodes:
		shortest_distances[pt] = sys.maxsize
	shortest_distances[start] = 0

	while unvisited_nodes:
		current_min_node = None
		for node in unvisited_nodes:
			if current_min_node is None or node not in shortest_distances or shortest_distances[node] < shortest_distances[current_min_node]:
				current_min_node = node

		neighbors = current_min_node.get_neighbors()
		for neighbor in neighbors:
			tentative_value = shortest_distances[current_min_node] + int(neighbor.get_value())
			if tentative_value < shortest_distances[neighbor]:
				shortest_distances[neighbor] = tentative_value
		unvisited_nodes.remove(current_min_node)
	return shortest_distances[end]


def get_extended_data():
	new_data = []
	for row in data:
		new_row = []
		for x in range(0, 5):
			new_row.extend([y+x if y+x <= 9 else y+x-9 for y in [int(x) for x in row]])
		new_data.append(new_row)

	new_rows = [[y+x if y+x <= 9 else y+x-9 for y in row] for x in range(1, 5) for row in new_data]
	for row in new_rows:
		new_data.append(row)
	return new_data


def part_one():
	m = Grid(values=data)
	m.set_neighbors_for_all(False)
	return a_star(m.get_point(0, 0), m.get_point(m.get_height()-1, m.get_width()-1))
	# return dijkstra(m, m.get_point(0, 0), m.get_point(m.get_height()-1, m.get_width()-1))


def part_two():
	m = Grid(values=get_extended_data())
	m.set_neighbors_for_all(False)
	return a_star(m.get_point(0, 0), m.get_point(m.get_height()-1, m.get_width()-1))
	# return dijkstra(m, m.get_point(0, 0), m.get_point(m.get_height()-1, m.get_width()-1))


if __name__ == '__main__':
	run_with_timer(part_one)  # 745 -- took 2978 ms
	run_with_timer(part_two)  # 3002 -- took 385831 ms

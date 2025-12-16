from aoc_utils import run_with_timer
import re

data = [x.strip().split(" ") for x in open("input.txt").readlines()]

# procedure DFS_iterative(G, v) is
	# let S be a stack
	# S.push(v)
	# while S is not empty do
		# v = S.pop()
		# if v is not labeled as discovered then
			# label v as discovered
			# for all edges from v to w in G.adjacentEdges(v) do
				# S.push(w)
class Valve():
	def __init__(self, name, flow_rate:int, connections):
		self.name = name
		self.flow_rate = flow_rate
		self.connections = connections

	def __repr__(self) -> str:
		return f"Valve('{self.name}', {self.flow_rate}, {self.connections})"

	def __eq__(self, __o: object) -> bool:
		return (self.name == __o.name
				  and self.flow_rate == __o.flow_rate
				  and self.connections == __o.connections)

def parse_data():
	return {x[1]: {"name": x[1], "flow": int(x[4].split("=")[1][:-1]), "tunnels": [y.replace(",", "") for y in x[9:]], "visited": False} for x in data}


def find_paths_dfs(g, root):
	s = [root]
	while len(s) > 0:
		v = s.pop()
		if not v["visited"]:
			v["visited"] = True
			for neighbor in v["tunnels"]:
				s.append(g[neighbor])

def parse(puzzle_input):
	"""Parse input."""
	store_dict = {}
	# valves = []
	prog = re.compile(r'Valve ([A-Z]{2}) has flow rate=(\d+); '
							r'tunnels? leads? to valves? ((([A-Z]{2}), )*([A-Z]{2}))')
	for line in puzzle_input.splitlines():
		match = prog.match(line)
		if match:
			name = match.group(1)
			flow_rate = int(match.group(2))
			connections = set(match.group(3).split(', '))
			valve = Valve(name, flow_rate, connections)
			# valves.append(valve)
			store_dict[name] = valve
	steps = {x:{y:1 if y in store_dict[x].connections else float('inf') for y in store_dict} for x in store_dict}
	# Floyd-Warshall Algorithm for steps between nodes (valves)
	for k in steps:
		for i in steps:
			for j in steps:
				steps[i][j] = min(steps[i][j], steps[i][k] + steps[k][j])

	# logging.debug(valves)
	return store_dict, steps #, valves


def part_one():
	g = parse_data()

	print(g)
	# find_paths_dfs(g, g["AA"])
	return


def part_two():
	return


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

#
#
# def find_shortest_path_bfs(valves, root):
# 	dist_queue = [root]
# 	while len(dist_queue) > 0:
# 		p = dist_queue.pop(0)
# 		for x in p["tunnels"]:
# 			next_valve = valves[x]
# 			if next_valve["flow"] > 0 and next_valve["open_time"] == 0:
# 				next_valve["dist_from_root"] = p["dist_from_root"] + 1
# 				dist_queue.append(next_valve)
#
#
# def find_paths(edges, goal):
# 	q = [(0, goal)]
# 	path_lengths = {goal: 0}
# 	while q:
# 		cost, current = heapq.heappop(q)
# 		for point, point_cost in edges[current].items():
# 			if point not in path_lengths or cost + point_cost < path_lengths[point]:
# 				path_lengths[point] = cost + point_cost
# 				heapq.heappush(q, (cost + point_cost, point))
# 	return path_lengths
#
# def part_one():
# 	valves = {x[1]: {"name": x[1], "flow": int(x[4].split("=")[1][:-1]), "tunnels": [y.replace(",", "") for y in x[9:]], "open_time": 0, "dist_from_root":0} for x in data}
# 	key_valves = {x: v for x, v in valves.items() if v["flow"] > 0}
# 	print(valves)
#
# 	find_shortest_path_bfs(valves, valves["AA"])
# 	print(valves)
#
# 	# visited_valves = []
# 	# open_valves = []
# 	# time_remaining = 30
# 	# curr_valve = valves["AA"]
# 	# total_flow = 0
# 	# while time_remaining > 0:
# 	# 	one_move_vals = {}
# 	# 	two_move_vals = {}
# 	# 	for x in curr_valve["tunnels"]:
# 	# 		one_move_vals[x] = valves[x]["flow"] * (time_remaining - 1)
# 	# 		for y in valves[x]["tunnels"]:
# 	# 			two_move_vals[y] = valves[y]["flow"] * (time_remaining - 2)
#
# 		# if curr_valve["flow"] > 0 and curr_valve["name"] not in open_valves:
# 		# 	open_valves.append(curr_valve["name"])
# 		# 	total_flow += curr_valve["flow"] * time_remaining
# 		# 	print("opened " + curr_valve["name"])
# 		# else:
# 		# 	for x in curr_valve["tunnels"]:
# 		# 		if x not in visited_valves:
# 		# 			print("moving from " + curr_valve["name"] + " to " + x)
# 		# 			curr_valve = valves[x]
# 		# 			visited_valves.append(x)
# 		# 			break
# 		# time_remaining -= 1
#
# 	# return total_flow
#
#
# def part_two():
# 	return
#
#


# Part 1: 2029
# Part 2: 2723

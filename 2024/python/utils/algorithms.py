from collections import deque


def bfs(grid, src, dest, neighbor_func=lambda g, p: g.get_neighbors(p), inc_func=lambda _: 1):
	"""
	Simple BFS algorithm that takes a "source" object, a "destination" and finds the shortest path from src to dest.
	:param grid: The grid we're traversing with a BFS
	:param src: Some object that is the source
	:param dest: Some object that is the destination
	:param neighbor_func: The function that should be called to determine neighbors of a given "point"
	:param inc_func: Optional increment function that determines how much to increment the value. This basically allows for weighted distances between nodes. By default, the value is just 1
	:return: a tuple containing the destination point, the distance to get to that point, and the parent (which can be used to trace all the way back to the source)
	"""
	a = (src, 0, None)
	q = deque([a])
	visited = set(a[0])
	while q:
		curr = q.popleft()
		if curr[0] == dest:
			return curr
		for x in neighbor_func(grid, curr[0]):
			if x not in visited:
				a = (x, curr[1] + inc_func(x), curr)
				visited.add(a[0])
				q.append(a)


def reconstruct_path(came_from, current):
	total_path = [current]
	while current in came_from.keys():
		current = came_from[current]
		total_path.insert(0, current)
	return total_path


def astar(grid, src, dest, early_exit=True, h=lambda x: 0):
	open_set = [src]
	came_from = {}

	g_score = {src: 0}
	f_score = {src: h(src)}

	while len(open_set) > 0:
		min_val = float("inf")
		min_x = None
		for x in open_set:
			if x in f_score and f_score[x] < min_val:
				min_val = f_score[x]
				min_x = x
		current = min_x

		if early_exit and current == dest:
			return reconstruct_path(came_from, current)

		open_set.remove(current)
		for neighbor in [x for x in grid.get_neighbors(current) if x.get_value() != "#"]:
			tentative_g_score = g_score[current] + 1
			if neighbor not in g_score:
				g_score[neighbor] = float("inf")
			if neighbor not in f_score:
				f_score[neighbor] = float("inf")
			if tentative_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = tentative_g_score
				f_score[neighbor] = tentative_g_score + h(neighbor)
				if neighbor not in open_set:
					open_set.append(neighbor)
	return None

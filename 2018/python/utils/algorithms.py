def bfs(src, dest, neighbor_func, inc_func=lambda _: 1):
	"""
	Simple BFS algorithm that takes a "source" object, a "destination" and finds the shortest path from src to dest.
	:param src: Some object that is the source
	:param dest: Some object that is the destination
	:param neighbor_func: The function that should be called to determine neighbors of a given "point"
	:param inc_func: Optional increment function that determines how much to increment the value. This basically allows for weighted distances between nodes. By default, the value is just 1
	:return: a tuple containing the destination point, the distance to get to that point, and the parent (which can be used to trace all the way back to the source)
	"""
	a = (src, 0, None)
	visited = [a[0]]
	q = [a]
	while len(q) > 0:
		p = q.pop(0)
		if p[0] == dest:
			return p

		for x in neighbor_func(p):
			if x not in visited:
				a = (x, p[1] + inc_func(x), p)
				visited.append(a[0])
				q.append(a)


def dfs(src, dest, neighbor_func, inc_func=lambda _: 1):
	s = [(src, 0, None)]
	visited = []
	while len(s) > 0:
		p = s.pop(0)
		if p[0] == dest:
			return p

		if p[0] not in visited:
			visited.append(p[0])
			for x in neighbor_func(p):
				s.insert(0, (x, p[1] + inc_func(x), p))
	return visited

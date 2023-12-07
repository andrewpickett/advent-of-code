from utils.timers import run_with_timer
import itertools


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def build_guest_graph(d):
	guest_graph = {}
	for x in d:
		parts = x.split(' ')
		if not parts[0] in guest_graph.keys():
			guest_graph[parts[0]] = {}
		guest_graph[parts[0]][parts[10][:-1]] = int(parts[3]) * (1 if parts[2] == 'gain' else -1)
	return guest_graph


def calculate_happiness(guest_graph, s):
	return sum(guest_graph[s[i]][s[(i+1)%len(s)]] + guest_graph[s[i]][s[(i-1)%len(s)]] for i in range(len(s)))


def part_one(d):
	guest_graph = build_guest_graph(d)
	return max(calculate_happiness(guest_graph, x) for x in list(itertools.permutations(guest_graph.keys())))


def part_two(d):
	guest_graph = build_guest_graph(d)
	guest_graph['Me'] = {}
	for x in guest_graph.keys():
		guest_graph['Me'][x] = 0
		guest_graph[x]['Me'] = 0
	del guest_graph['Me']['Me']
	return max(calculate_happiness(guest_graph, x) for x in list(itertools.permutations(guest_graph.keys())))


if __name__ == '__main__':
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

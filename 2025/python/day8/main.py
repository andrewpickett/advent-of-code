from collections import defaultdict

from utils.timers import run_with_timer, get_data_with_timer

import math

def get_data(filename):
	coords = [tuple(map(int, parts.strip().split(","))) for parts in open(filename).readlines()]
	distances = sorted([(calc_dist(coords, i, j), i, j) for i in range(len(coords) - 1) for j in range(i + 1, len(coords))])
	return {"coords": coords, "distances": distances, "links": 1000}


def part_one(d):
	circuits = {i: i for i in range(len(d["coords"]))}
	return run(d["coords"], d["distances"], circuits, d["links"])


def part_two(d):
	circuits = {i: i for i in range(len(d["coords"]))}
	return run(d["coords"], d["distances"], circuits)


def calc_dist(coords, i, j):
	return math.sqrt((coords[i][0]-coords[j][0])**2 + (coords[i][1]-coords[j][1])**2 + (coords[i][2]-coords[j][2])**2)


def run(d, distances, circuits, link_count=None):
	connections = 0
	for t, distance in enumerate(distances):
		if link_count and t == link_count:
			circuit = defaultdict(int)
			for x in range(len(d)):
				circuit[dis_find(circuits, x)] += 1
			sorted_circuit = sorted(circuit.values())
			return sorted_circuit[-1] * sorted_circuit[-2] * sorted_circuit[-3]
		if dis_find(circuits, distance[1]) != dis_find(circuits, distance[2]):
			connections += 1
			if connections == len(d) - 1:
				return d[distance[1]][0] * d[distance[2]][0]
			connect(circuits, distance[1], distance[2])
	return 0


def dis_find(circuits, x):
	if x == circuits[x]:
		return x
	circuits[x] = dis_find(circuits, circuits[x])
	return circuits[x]


def connect(circuits, x, y):
	circuits[dis_find(circuits, x)] = dis_find(circuits, y)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main("input.txt")

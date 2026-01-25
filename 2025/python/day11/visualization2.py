from collections import defaultdict

from pyvis.network import Network
import networkx as nx

import functools

from utils.timers import run_with_timer, get_data_with_timer
from utils.utils import HashableDict

start_node = "svr"
# start_node = "you"

def get_data(f):
	dg = defaultdict(list)
	for x in f.readlines():
		parts = x.strip().split(":")
		dg[parts[0]].extend(parts[1].strip().split(" "))
	dg["out"] = []
	return HashableDict(dg)


def part_one(d):
	nx_graph = nx.DiGraph()
	for k, v in d.items():
		edges = []
		for e in v:
			edges.append((k, e, 1))
		nx_graph.add_weighted_edges_from(edges)
	nx.set_node_attributes(nx_graph, 5, 'size')
	nx.set_edge_attributes(nx_graph, '#999999', 'color')
	nx.set_edge_attributes(nx_graph, 10, 'arrowsize')
	set_node_props(nx_graph, "out", {"size": 20, "color": "#990000"})
	set_node_props(nx_graph, "you", {"size": 20, "color": "#009900"})
	set_node_props(nx_graph, "svr", {"size": 20, "color": "#009900"})
	set_node_props(nx_graph, "dac", {"size": 20, "color": "#000099"})
	set_node_props(nx_graph, "fft", {"size": 20, "color": "#000099"})
	net = Network('1200px', '1900px', directed=True)
	net.from_nx(nx_graph)
	net.show("nx.html", notebook=False)


def set_node_props(g, node, props={}):
	if node in g.nodes:
		for k, v in props.items():
			g.nodes[node][k] = v

@functools.cache
def count_paths(d, f, dac, fft):
	if f == "out":
		return 1 if dac and fft else 0
	return sum(count_paths(d, v, dac or (f == "dac"), fft or (f == "fft")) for v in d[f])


def part_two(d):
	return count_paths(d, "svr", False, False)


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	# run_with_timer(part_two, data)


if __name__ == '__main__':
	main("input.txt")

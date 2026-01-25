from collections import defaultdict

import igraph as ig
import networkx as nx
import matplotlib.pyplot as plt
import pydot
import graphviz

import functools
import pprint

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
	g = ig.Graph()
	print(d.keys())
	for k, v in enumerate(d.keys()):
		g.add_vertices(k)
	g.add_vertices(len(d.keys()))
	print(g)
	ig.summary(g)
	# pprint.pprint(d)
	# G = nx.Graph()
	# for k in d.keys():
	# 	G.add_node(k)
	# G.add_node("out")
	# for k, v in d.items():
	# 	for e in v:
	# 		G.add_edge(k, e)
	# # pos = nx.spring_layout(G, seed=3113794652)
	# pos = nx.drawing.nx_agraph.graphviz_layout(G, prog='sfdp')
	# # nx.nx_pydot.graphviz_layout(G)
	#
	# node_options = {"edgecolors": "tab:gray", "alpha": 1.0}
	# nx.draw_networkx_nodes(G, pos, nodelist=[i for i in G.nodes if i not in [start_node, "out"]], node_color="#eaeaea", node_size=600, **node_options)
	# nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_size=1500, node_color="tab:red", **node_options)
	# nx.draw_networkx_nodes(G, pos, nodelist=["out"], node_size=1500, node_color="tab:green", **node_options)
	#
	# label_options = {"font_family": "Consolas"}
	# nx.draw_networkx_labels(G, pos, labels={i: i for i in G.nodes.keys() if i not in [start_node, "out"]}, font_color="black", font_size=8, **label_options)
	# nx.draw_networkx_labels(G, pos, labels={start_node: start_node, "out": "out"}, font_weight="bold", font_size=16, **label_options)
	#
	# edge_options = {"edge_color": "black"}
	# nx.draw_networkx_edges(G, pos, **edge_options)
	#
	# plt.figure()
	# plt.tight_layout()
	# plt.axis("off")
	# # plt.figure(figsize=(1200, 1200))
	# # plt.show()
	# plt.title("Graph Visualization using Graphviz layout")
	# plt.show()
	# # plt.savefig("large_graph.svg", format="svg", bbox_inches="tight")
	#
	# nodes_to_visit = list(d[start_node])
	# counter = 0
	# #
	# # while nodes_to_visit:
	# # 	next_node = nodes_to_visit.pop(0)
	# # 	if next_node == "out":
	# # 		counter += 1
	# # 	else:
	# # 		nodes_to_visit.extend(list(d[next_node]))
	# return counter


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
	main("sample.txt")

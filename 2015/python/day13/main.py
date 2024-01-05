from utils.timers import run_with_timer, get_data_with_timer
import itertools


def get_data(filename):
	guest_graph = {}
	for x in [y.strip() for y in open(filename).readlines()]:
		parts = x.split(' ')
		if not parts[0] in guest_graph.keys():
			guest_graph[parts[0]] = {}
		guest_graph[parts[0]][parts[10][:-1]] = int(parts[3]) * (1 if parts[2] == 'gain' else -1)
	return guest_graph


def calculate_happiness(guest_graph, s):
	return sum(guest_graph[s[i]][s[(i+1)%len(s)]] + guest_graph[s[i]][s[(i-1)%len(s)]] for i in range(len(s)))


def part_one(d):
	return max(calculate_happiness(d, x) for x in list(itertools.permutations(d.keys())))


def part_two(d):
	d['Me'] = {}
	for x in [y for y in d.keys() if y != 'Me']:
		d['Me'][x] = 0
		d[x]['Me'] = 0
	return max(calculate_happiness(d, x) for x in list(itertools.permutations(d.keys())))


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

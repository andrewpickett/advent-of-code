from aoc_utils import run_with_timer

data = [x.strip() for x in open('input.txt').readlines()]


def build_city_graph():
	city_map = {}
	for x in data:
		city_data = x.split(' = ')

		cities = city_data[0].split(' to ')
		if cities[0] not in city_map.keys():
			city_map[cities[0]] = {}
		if cities[1] not in city_map.keys():
			city_map[cities[1]] = {}

		if cities[1] not in city_map[cities[0]].keys():
			city_map[cities[0]][cities[1]] = int(city_data[1])
		if cities[0] not in city_map[cities[1]].keys():
			city_map[cities[1]][cities[0]] = int(city_data[1])
	return city_map


def traverse_map(city_map, start_city, visited_cities, is_min):
	visited_cities.append(start_city)

	dist = float('inf') if is_min else float('-inf')
	curr_dist = 0
	for next_city in city_map[start_city]:
		if next_city not in visited_cities:
			curr_dist = city_map[start_city][next_city] + traverse_map(city_map, next_city, visited_cities.copy(), is_min)
			if (is_min and curr_dist < dist) or (not is_min and curr_dist > dist):
				dist = curr_dist
	return dist if curr_dist > 0 else 0


def part_one():
	city_map = build_city_graph()
	return min(traverse_map(city_map, start_city, [], True) for start_city in city_map)


def part_two():
	city_map = build_city_graph()
	return max(traverse_map(city_map, start_city, [], False) for start_city in city_map)


if __name__ == '__main__':
	run_with_timer(part_one)  # 251 -- took 208 ms
	run_with_timer(part_two)  # 898 -- took 197 ms

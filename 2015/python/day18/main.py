from utils.timers import run_with_timer
from utils.grid import Grid
from copy import copy


def get_data(filename):
	g = Grid(values=[[y for y in x.strip()] for x in open(filename).readlines()])
	g.set_neighbors_for_all(True)
	return {"steps": 100, "grid": g}


def run_steps(grid, steps, broken_lights):
	for i in range(steps):
		lights_to_switch = []
		for light in [x for x in grid.get_points() if x not in broken_lights]:
			neighbor_lights = [x for x in light.get_neighbors() if x.value == "#"]
			if light.value == "#" and len(neighbor_lights) not in (2, 3):
				lights_to_switch.append(light)
			elif light.value == "." and len(neighbor_lights) == 3:
				lights_to_switch.append(light)
		for light in lights_to_switch:
			light.value = "#" if light.value == "." else "."
	return sum(1 for x in grid.get_points() if x.value == "#")


def part_one(d):
	return run_steps(copy(d["grid"]), d["steps"], [])


def part_two(d):
	grid = copy(d["grid"])
	broken_lights = [grid.get_point(0, 0), grid.get_point(0, -1), grid.get_point(-1, 0), grid.get_point(-1, -1)]
	for light in broken_lights:
		light.value = "#"
	return run_steps(grid, d["steps"], broken_lights)


if __name__ == '__main__':
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

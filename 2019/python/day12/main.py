import copy
from math import gcd

data = [x[1:-2] for x in open("input.txt").readlines()]

orig_universe = []


def _compare_velocity(a, b):
	return 0 if a == b else ((a - b) // abs(a - b))


class Planet:
	def __init__(self, position, velocity=(0, 0, 0,)):
		self.position = position
		self.velocity = velocity

	def update_velocity(self, other):
		x_val = self.velocity[0] - _compare_velocity(self.position[0], other.position[0])
		y_val = self.velocity[1] - _compare_velocity(self.position[1], other.position[1])
		z_val = self.velocity[2] - _compare_velocity(self.position[2], other.position[2])
		self.velocity = (x_val, y_val, z_val,)

	def apply_velocity(self):
		self.position = tuple(x + y for x, y in zip(self.position, self.velocity))

	def get_potential_energy(self):
		return sum(abs(x) for x in self.position)

	def get_kinetic_enerty(self):
		return sum(abs(x) for x in self.velocity)

	def get_total_energy(self):
		return self.get_potential_energy() * self.get_kinetic_enerty()


def populate_planets():
	for d in data:
		positions = d.split(',')
		orig_universe.append(Planet((int(positions[0].split('=')[1]), int(positions[1].split('=')[1]), int(positions[2].split('=')[1]),)))


def step_forward(planets):
	for i, planet in enumerate(planets):
		for j in range(i + 1, len(planets)):
			planet.update_velocity(planets[j])
			planets[j].update_velocity(planet)
		planet.apply_velocity()


def part_one():
	planets = copy.deepcopy(orig_universe)
	step = 0
	while step < 1000:
		step_forward(planets)
		step += 1
	return sum(int(planet.get_total_energy()) for planet in planets)


def lcm(a, b):
	return a * b // gcd(a, b)


def get_cycle_length(plane_idx):
	planets = copy.deepcopy(orig_universe)
	cycle_elems = []
	i = 0
	start_cycle_idx = 0
	test_idx = 0
	started_cycle_test = False
	while True:
		plane = str([planet.position[plane_idx] for planet in planets])
		if started_cycle_test:
			test_idx += 1
			if cycle_elems[test_idx] != plane:
				test_idx = 0
				started_cycle_test = False
				if cycle_elems[0] == plane:
					started_cycle_test = True
					start_cycle_idx = i
			if test_idx == start_cycle_idx:
				return start_cycle_idx
		else:
			if len(cycle_elems) > 0 and cycle_elems[0] == plane:
				started_cycle_test = True
				start_cycle_idx = i
		cycle_elems.append(plane)
		step_forward(planets)
		i += 1


def part_two():
	cycles = set()
	for i in range(3):
		cycles.add(get_cycle_length(i))
	cycles = list(cycles)
	return lcm(lcm(cycles[0], cycles[1]), cycles[2])


if __name__ == '__main__':
	populate_planets()
	print(part_one())  # 9958
	print(part_two())  # 318382803780324

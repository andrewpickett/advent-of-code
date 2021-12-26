from aoc_utils import run_with_timer

data = [x.strip() for x in open("sample2.txt").readlines()]

#
# class Cuboid:
# 	def __init__(self, xrange, yrange, zrange):
# 		self.off_x =
# 		self.yrange = yrange
# 		self.zrange = zrange
#
# 	def calc_on_cells(self):
# 		return 0
#
class Point3:
	def __init__(self, x, y, z, on=False):
		self.x = x
		self.y = y
		self.z = z
		self.on = on

	def __hash__(self):
		return hash(str(self))

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z

	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

	def __repr__(self):
		return str(self)


def part_one():
	return
	# all_points = set()
	# for x in range(-50, 51):
	# 	for y in range(-50, 51):
	# 		for z in range(-50, 51):
	# 			all_points.add(Point3(x, y, z))
	#
	# for d in data:
	# 	action = d.split(" ")[0]
	# 	coords = d.split(",")
	# 	x_range = coords[0].split("=")[1].split("..")
	# 	y_range = coords[1].split("=")[1].split("..")
	# 	z_range = coords[2].split("=")[1].split("..")
	#
	# 	for x in range(int(x_range[0]), int(x_range[1])+1):
	# 		if -50 <= x <= 50:
	# 			for y in range(int(y_range[0]), int(y_range[1])+1):
	# 				if -50 <= y <= 50:
	# 					for z in range(int(z_range[0]), int(z_range[1])+1):
	# 						if -50 <= z <= 50:
	# 							p = Point3(x, y, z)
	# 							p.on = action == 'on'
	# 							all_points.remove(p)
	# 							all_points.add(p)
	# return len(set(filter(lambda e: e.on, all_points)))


def create_point_set(source_elem):
	source_points = set()
	for x in source_elem["xrange"]:
		for y in source_elem["yrange"]:
			for z in source_elem["zrange"]:
				source_points.add(Point3(x, y, z, source_elem["action"] == "on"))
	return source_points


def get_range_overlap(range1, range2):
	return range(max(range1[0], range2[0]), min(range1[-1], range2[-1])+1)

def get_volume_from_ranges(xr, yr, zr):
	return len(xr) * len(yr) * len(zr)


def part_two():
	all_instructions = []
	for d in data:
		action = d.split(" ")[0]
		coords = d.split(",")
		x_range = coords[0].split("=")[1].split("..")
		y_range = coords[1].split("=")[1].split("..")
		z_range = coords[2].split("=")[1].split("..")
		all_instructions.append({
			"action": action,
			"xrange": range(int(x_range[0]), int(x_range[1]) + 1),
			"yrange": range(int(y_range[0]), int(y_range[1]) + 1),
			"zrange": range(int(z_range[0]), int(z_range[1]) + 1)
		})
	total_on = 0
	on_regions = []
	for i, inst in enumerate(all_instructions):
		cuboid_volume = get_volume_from_ranges(inst["xrange"], inst["yrange"], inst["zrange"])
		for j, n in enumerate(on_regions):

			overlapx = get_range_overlap(inst["xrange"], n["xrange"])
			if len(overlapx) > 0:
				overlapy = get_range_overlap(inst["yrange"], n["yrange"])
				if len(overlapy) > 0:
					overlapz = get_range_overlap(inst["zrange"], n["zrange"])
					if len(overlapz) > 0:
						if inst["action"] == "on":
							print("Removing duplicates", get_volume_from_ranges(overlapx, overlapy, overlapz), "because of", inst)
							total_on -= get_volume_from_ranges(overlapx, overlapy, overlapz)
						else:

							print("Turning off", get_volume_from_ranges(overlapx, overlapy, overlapz), "because of", inst)
							total_on -= get_volume_from_ranges(overlapx, overlapy, overlapz)



						# return
		if inst["action"] == "on":
			print("Turning on", get_volume_from_ranges(inst["xrange"], inst["yrange"], inst["zrange"]), "because of", inst)
			total_on += cuboid_volume
			on_regions.append(inst)

	# for i1 in range(len(all_instructions) - 1):
	# 	source = all_instructions[i1]
	# 	if source["action"] == "on":
	# 		total_on += get_volume_from_ranges(source["xrange"], source["yrange"], source["zrange"])
	# 	for i2 in range(i1 + 1, len(all_instructions)):
	# 		inst = all_instructions[i2]
	# 		overlapx = get_range_overlap(source["xrange"], inst["xrange"])
	# 		if len(overlapx) > 0:
	# 			overlapy = get_range_overlap(source["yrange"], inst["yrange"])
	# 			if len(overlapy) > 0:
	# 				overlapz = get_range_overlap(source["zrange"], inst["zrange"])
	# 				if len(overlapz) > 0:
	# 					if source["action"] == "on" and inst["action"] == "on":
	# 						# only count non-overlapping
	# 						print("Adding non-overlapping points from", inst)
	# 						total_on += get_volume_from_ranges(inst["xrange"], inst["yrange"], inst["zrange"]) - get_volume_from_ranges(overlapx, overlapy, overlapz)
	# 					elif source["action"] == "on" and inst["action"] == "off":
	# 						# subtract the overlap
	# 						print("Subtracting overlapping points non-overlapping points from", source)
	# 						total_on -= get_volume_from_ranges(overlapx, overlapy, overlapz)
	#
	# 					# if inst["action"] == "off":
	# 						print(source, "has", (len(overlapx) * len(overlapy) * len(overlapz)), "overlaps with", inst)
		# all_instructions[i1]
		# full_range = create_point_set(all_instructions[i1])
		# source_points = create_point_set(all_instructions[i1])
		# 	if all_instructions[i2]["action"] == 'off':
		# 		source_points -= comp_points
		# 	else:
		# 		source_points = source_points.union(full_range.intersection(comp_points))
		# total_on += len(source_points)
	return total_on


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

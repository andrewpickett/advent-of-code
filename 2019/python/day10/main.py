from pprint import pp
from fractions import Fraction

data = [x.strip()for x in open("input.txt").readlines()]

def part_one():
	points = []
	map = []
	for i, line in enumerate(data):
		map.append([])
		for j, pos in enumerate(line):
			map[i].append(-1 if pos == '.' else 0)
			if pos == '#':
				points.append(tuple((j, i)))

	tots = {}
	for i in range(len(points)):
		start_point = points[i]
		tots[start_point] = set()
		for j in range(len(points)):
			end_point = points[j]
			if start_point != end_point:
				# vertical lines first
				if start_point[0] == end_point[0]:
					equation = "x={}".format(start_point[0])
				# horizontal lines next
				elif start_point[1] == end_point[1]:
					equation = 'y={}'.format(start_point[1])
				else:
					# The rest have slope
					slope = Fraction(end_point[1] - start_point[1], end_point[0] - start_point[0])
					yint = start_point[1] - (start_point[0] * slope)
					equation = 'y={}x+{}'.format(slope, yint)

					if slope < 0 and end_point[1] > start_point[1]:
						equation += ' (B)'
					elif slope > 0 and end_point[1] < start_point[1]:
						equation += ' (B)'
				tots[start_point].add(equation)

	pp(tots)
	max_val = 0
	max_pos = (0, 0)
	for point in tots:
		if len(tots[point]) > max_val:
			max_val = len(tots[point])
			max_pos = point
	print()

	print("{} at {}".format(max_val, max_pos))
	return


def part_two():
	return


if __name__ == '__main__':
	#
	# print(Fraction(10/2))
	# print(Fraction(20/4))
	print(part_one())  # 3460311188
	# print(part_two())  # 42202

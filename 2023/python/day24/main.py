from utils.timers import run_with_timer


def get_data(filename):
	lines = [x.strip().split(" @ ") for x in open(filename).readlines()]
	ret_val = []
	for line in lines:
		coords = tuple([int(x) for x in line[0].split(", ")])
		vels = tuple([int(x) for x in line[1].split(", ")])
		ret_val.append([coords, vels])
	return ret_val


def count_collisions(d, r):
	cnt = 0
	for i in range(len(d)-1):
		for j in range(i+1, len(d)):
			s1 = d[i][1][1] / d[i][1][0]
			s2 = d[j][1][1] / d[j][1][0]
			if s1 == s2:
				# parallel, don't intersect
				continue
			else:
				c1 = d[i][0][1] - (s1 * d[i][0][0])
				c2 = d[j][0][1] - (s2 * d[j][0][0])
				xint = (c2-c1)/(s1-s2)
				yint = (s1*xint) + c1
				if r.start <= xint <= r.stop and r.start <= yint <= r.stop:
					if ((d[i][1][0] <= 0 and xint <= d[i][0][0]) or (d[i][1][0] >= 0 and xint >= d[i][0][0])) and ((d[j][1][0] <= 0 and xint <= d[j][0][0]) or (d[j][1][0] >= 0 and xint >= d[j][0][0])):
						cnt += 1
	return cnt


def part_one(d):
	return count_collisions(d, range(200000000000000, 400000000000000))


def calc_slope(p1, p2):
	return (p1[0]-p2[0], p1[1]-p2[1], p1[2]-p2[2])

def part_two(d):

	# for each point get slopes from time t to time t+? with every other point
	# {(x1, y1, z1): {(x2, y2, z2): [<t1>, <t2>, ... <tn>]

	point_slope_map = {}
	for i in range(len(d)-1):
		pt = d[i][0]
		point_slope_map[pt] = {}
		for j in range(i+1, len(d)):
			point_slope_map[pt][d[j][0]] = []
			for t in range(6):
				t_pt = (d[j][0][0]+d[j][1][0]*t, d[j][0][1]+d[j][1][1]*t, d[j][0][2]+d[j][1][2]*t)
				point_slope_map[pt][d[j][0]].append(calc_slope(pt, t_pt))
	print(point_slope_map)
	# for t in range(0, 10):
	# 	for pt in d:
	# 		x = pt[0][0] + pt[1][0]*t
	# 		y = pt[0][1] + pt[1][1]*t
	# 		z = pt[0][2] + pt[1][2]*t
	# 		all_points.append((x, y, z, t))
	# print(all_points)
	#
	# nont = [tuple(x[:-1]) for x in all_points]
	# for i in nont:
	# 	print(i, nont.count(i))
	return False


if __name__ == "__main__":
	data = get_data("sample.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

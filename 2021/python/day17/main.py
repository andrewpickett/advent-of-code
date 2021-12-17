from aoc_utils import run_with_timer
import math

data = open("input.txt").readline().strip().split(" ")
region = {
	"xs": int(data[2][2:-1].split("..")[0]),
	"xe": int(data[2][2:-1].split("..")[1]),
	"ys": int(data[3][2:].split("..")[1]),
	"ye": int(data[3][2:].split("..")[0])
}


def get_valid_initial_velocities():
	valid_coords = []
	yrange = abs(region["ye"]) + 1
	for x_init in range(math.floor(math.sqrt(region["xs"] * 2)), region["xe"] + 1):
		for y_init in range(yrange, -yrange, -1):
			y = 0
			x = 0
			curr_x_velocity = x_init
			curr_y_velocity = y_init
			while y >= region["ye"] and x <= region["xe"]:
				if curr_x_velocity == 0 and x < region["xs"]:
					break
				x += curr_x_velocity
				y += curr_y_velocity
				if region["xs"] <= x <= region["xe"] and region["ys"] >= y >= region["ye"]:
					valid_coords.append({"x": x_init, "y": y_init})
					break
				curr_y_velocity -= 1
				curr_x_velocity -= 1 if curr_x_velocity > 0 else 0
	return valid_coords


def part_one():
	maxy = int(abs(region["ye"]))-1
	return maxy * (maxy + 1) // 2


def part_two():
	return len(get_valid_initial_velocities())


if __name__ == '__main__':
	run_with_timer(part_one)  # 12561 -- took 0 ms
	run_with_timer(part_two)  # 3785 -- took 90 ms

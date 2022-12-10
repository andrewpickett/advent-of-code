from aoc_utils import run_with_timer

data = [x.strip().split(" ") for x in open("input.txt").readlines()]


def get_signal_strength(cycle, register):
	return register * cycle if cycle in [20, 60, 100, 140, 180, 220] else 0


def draw_pixel(pixels, cycle, register):
	if (cycle - 1) % 40 in [register - 1, register, register + 1]:
		pixels[(cycle-1)//40] += "#"
	else:
		pixels[(cycle-1)//40] += " "


def output_pixels(pixels):
	for x in pixels:
		print(x)


def part_one():
	register = 1
	cycle = 1
	s = 0
	for x in data:
		cycle += 1
		s += get_signal_strength(cycle, register)
		if x[0] == "addx":
			cycle += 1
			register += int(x[1])
			s += get_signal_strength(cycle, register)
	return s


def part_two():
	pixels = ["", "", "", "", "", ""]
	register = 1
	cycle = 0
	for x in data:
		cycle += 1
		draw_pixel(pixels, cycle, register)
		if x[0] == "addx":
			cycle += 1
			draw_pixel(pixels, cycle, register)
			register += int(x[1])
	output_pixels(pixels)
	return


if __name__ == '__main__':
	run_with_timer(part_one)  # 13920 -- took 0 ms
	run_with_timer(part_two)  # EGLHBLFJ -- took 0 ms

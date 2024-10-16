from utils.timers import run_with_timer, get_data_with_timer
import math


def get_data(filename):
	lines = [x.strip() for x in open(filename).readlines()]
	rules = {"start": ".#./..#/###"}
	for line in lines:
		parts = line.split(" => ")
		p = parts[0]
		rules[p] = parts[1]
		rules[flip_vertical(p)] = parts[1]
		rules[flip_horizontal(p)] = parts[1]
		rules[rotate_90(p)] = parts[1]
		rules[flip_horizontal(rotate_90(p))] = parts[1]
		rules[flip_horizontal(rotate_270(p))] = parts[1]
		rules[rotate_180(p)] = parts[1]
		rules[rotate_270(p)] = parts[1]
	return rules


def part_one(d, iters=5):
	return run(d, d["start"].split("/"), iters)


def part_two(d, iters=18):
	return run(d, d["start"].split("/"), iters)


def run(d, image, iterations):
	divisions = 0
	for i in range(iterations):
		size = len(image)
		divided_images = ["/".join(image)]

		if size > 2 and size % 2 == 0:
			divided_images = divide(image, size, 2)
			divisions = size // 2
		elif size > 3 and size % 3 == 0:
			divided_images = divide(image, size, 3)
			divisions = size // 3
		new_image = []
		for division in divided_images:
			new_image.append(d[division])
		image = combine(new_image, divisions)
	return "".join(image).count("#")


def combine(image, divisions):
	if len(image) == 1:
		return image[0].split("/")
	else:
		all_parts = [x.split("/") for x in image]
		new_image = []
		for r in range(0, len(image), divisions):
			for t in range(0, len(all_parts[0])):
				new_row = ""
				for s in range(r, r+divisions):
					new_row += all_parts[s][t]
				new_image.append(new_row)
		return new_image


def divide(image, size, subsize):
	divided_images = []
	for i in range(0, size, subsize):
		for j in range(0, size, subsize):
			sub_image = []
			for k in range(i, i+subsize):
				sub_image.append(image[k][j:j+subsize])
			divided_images.append("/".join(sub_image))
	return divided_images


def flip_horizontal(rule):
	return "/".join([x[::-1] for x in rule.split("/")])


def flip_vertical(rule):
	return "/".join([x for x in rule.split("/")][::-1])


def rotate_180(rule):
	return flip_horizontal(flip_vertical(rule))


def rotate_90(rule):
	p = rule.split("/")
	s = "".join([i[x] for x in range(len(p[0])-1, -1, -1) for i in p])
	size = int(math.sqrt(len(s)))
	return "/".join([s[i:size+i] for i in range(0, len(s), size)])


def rotate_270(rule):
	return flip_horizontal(flip_vertical(rotate_90(rule)))


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

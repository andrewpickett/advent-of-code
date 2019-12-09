from pprint import pp

data = [int(x) for x in open("input.txt").readline().strip()]

WIDTH = 25
HEIGHT = 6
LAYERS = int(len(data) / WIDTH / HEIGHT)


def chunks(lst, n):
	for i in range(0, len(lst), n):
		yield lst[i:i + n]


def part_one():
	layers = list(chunks(data, int(len(data) / LAYERS)))

	min_layer = None
	for layer in layers:
		if not min_layer or layer.count(0) < min_layer.count(0):
			min_layer = layer
	return min_layer.count(2) * min_layer.count(1)


def part_two():
	layers = list(chunks(data, int(len(data) / LAYERS)))

	result_layer = [0] * len(layers[0])
	for i in range(len(layers[0])):
		for layer in layers:
			if layer[i] == 0 or layer[i] == 1:
				result_layer[i] = layer[i]
				break

	return list(chunks(result_layer, WIDTH))


if __name__ == '__main__':
	print(part_one())  # 1935
	pp(part_two())  # CFLUL

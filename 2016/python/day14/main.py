from aoc_utils import run_with_timer
import hashlib
import re

data = open("input.txt").readline().strip()


def get_matches(salt, stretch, start, end, trips, pents):
	prog1 = re.compile(r'(.)\1{2,}')
	prog2 = re.compile(r'(.)\1{4,}')
	for i in range(start, end):
		h = hash_stretch(salt + str(i), stretch)
		t = prog1.search(h)
		p = prog2.search(h)
		if t:
			trips.append((i, t.group()[0], h))
		if p:
			pents.append((i, p.group()[0], h))


def get_key_index(salt, stretch):
	trips = []
	pents = []
	key_count = 0
	start = 1
	step = 25000
	while key_count < 64:
		get_matches(salt, stretch, start, start + step, trips, pents)
		for trip in trips:
			for pent in pents:
				if trip[0] < pent[0] <= trip[0] + 1000 and pent[1] == trip[1]:
					key_count += 1
					break
			if key_count == 64:
				return trip[0]
		start += step
		trips = []
		pents = []


def hash_stretch(key, stretch):
	h = hashlib.md5(key.encode()).hexdigest()
	for x in range(stretch):
		h = hashlib.md5(h.encode()).hexdigest()
	return h


def part_one():
	return get_key_index(data, 0)


def part_two():
	return get_key_index(data, 2016)


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

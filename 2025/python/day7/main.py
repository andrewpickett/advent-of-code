from utils.timers import run_with_timer, get_data_with_timer

from collections import defaultdict

def get_data(f):
	all_data = f.readlines()
	return {"lines": [x for x in all_data if "^" in x], "start": all_data[0].index("S")}

def part_one(d):
	return fire_tachyon_beams({d["start"]: 1}, d["lines"], True)


def part_two(d):
	return fire_tachyon_beams({d["start"]: 1}, d["lines"], False)


def fire_tachyon_beams(beam_counters, lines, p1):
	splits = 0
	for line in lines:
		tachyon_beams = defaultdict(int)
		for idx, counter in beam_counters.items():
			if line[idx] == '^':
				splits += 1
				tachyon_beams[idx-1] += counter
				tachyon_beams[idx+1] += counter
			else:
				tachyon_beams[idx] += counter
			beam_counters = tachyon_beams
	return splits if p1 else sum(beam_counters.values())


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

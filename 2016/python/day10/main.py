from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip().split(" ") for x in open(filename).readlines()]


def run_instructions(d, outputs, low_comp, high_comp):
	process_instructions = []
	bots = {}
	comparing_bot = ""
	while len(process_instructions) < len(d):
		for x in d:
			if x not in process_instructions:
				if x[0] == "value":
					if x[5] not in bots:
						bots[x[5]] = set()
					bots[x[5]].add(int(x[1]))
					process_instructions.append(x)
				elif x[0] == "bot":
					if x[1] not in bots:
						bots[x[1]] = set()
					if len(bots[x[1]]) == 2:
						low_target = bots if x[5] == "bot" else outputs
						high_target = bots if x[10] == "bot" else outputs
						if x[6] not in low_target:
							low_target[x[6]] = set()
						if x[11] not in high_target:
							high_target[x[11]] = set()
						low_val = min(bots[x[1]])
						high_val = max(bots[x[1]])
						low_target[x[6]].add(low_val)
						bots[x[1]].remove(low_val)
						high_target[x[11]].add(high_val)
						bots[x[1]].remove(high_val)
						if low_val == low_comp and high_val == high_comp and comparing_bot == "":
							comparing_bot = x[1]
						process_instructions.append(x)
	return comparing_bot


def part_one(d):
	return run_instructions(d, {}, 17, 61)


def part_two(d):
	outputs = {}
	run_instructions(d, outputs, 17, 61)
	return list(outputs["0"])[0] * list(outputs["1"])[0] * list(outputs["2"])[0]


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

from utils.timers import run_with_timer


def get_data(filename):
	return open(filename).readline().strip()


def process_stream(d):
	depth = 0
	i = 0
	scores = []
	garbage_count = 0
	in_garbage = False
	while i < len(d):
		if d[i] == "!":
			i += 1
		else:
			if d[i] == "<":
				if not in_garbage:
					in_garbage = True
					garbage_count -= 1
			if not in_garbage:
				if d[i] == "{":
					depth += 1
					scores.append(depth)
				if d[i] == "}":
					depth -= 1
			else:
				if d[i] == ">":
					in_garbage = False
				else:
					garbage_count += 1
		i += 1
	return scores, garbage_count


def part_one(d):
	return sum(process_stream(d)[0])


def part_two(d):
	return process_stream(d)[1]


if __name__ == "__main__":
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

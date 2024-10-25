from collections import deque
from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	line = open(filename).readline().strip().split()
	return {"p": int(line[0]), "s": int(line[-2])}


def part_one(d):
	return run(d["p"], d["s"])


def part_two(d):
	return run(d["p"], d["s"]*100)


def run(players, marbles):
	circle = deque([0])
	scores = {i: 0 for i in range(players)}

	for current_marble in range(1, marbles+1):
		if current_marble % 23 == 0:
			circle.rotate(7)
			scores[current_marble % players] += current_marble + circle.pop()
			circle.rotate(-1)
		else:
			circle.rotate(-1)
			circle.append(current_marble)
	return max(scores.values())


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

import time

DIR_LOOKUP = {"L": -1, "R": 1}

def run(f):
	pos = 50
	ans1, ans2 = 0, 0
	for x in f.readlines():
		direction, amount = x[0], int(x[1:])
		next_pos = pos + DIR_LOOKUP[direction] * (amount % 100)
		ans1 += 1 if next_pos % 100 == 0 else 0
		ans2 += (1 if not next_pos in range(1, 100) and pos != 0 else 0) + (amount // 100 if amount >= 100 else 0)
		pos = next_pos % 100
	return ans1, ans2


def main(f="input.txt"):
	runtimes = []
	for i in range(20000):
		total_time = 0
		with open(f) as input_file:
			stime = time.time_ns()
			run(input_file)
			total_time += time.time_ns() - stime
		runtimes.append(total_time)
	total_avg = (sum(runtimes) / len(runtimes)) / 1000000
	print("took {} ms (over {} runs)".format(total_avg, len(runtimes)))

if __name__ == '__main__':
	main()

import os
import time
import day1.main as d1
import day2.main as d2
import day3.main as d3
import day4.main as d4
import day5.main as d5
import day6.main as d6
import day7.main as d7
import day8.main as d8
import day9.main as d9
import day10.main as d10
import day11.main as d11
import day12.main as d12

days = [d5]


def run_all(runs):
	runtimes = []
	for i in range(runs):
		total_time = 0
		for day in days:
			stime = time.time_ns()
			day.main(os.path.join(os.path.dirname(day.__file__), "input.txt"))
			total_time += time.time_ns() - stime
		runtimes.append(total_time)
	total_avg = (sum(runtimes) / len(runtimes)) / 1000000
	print("2025 -- took {} ms (average {} ms per day over {} runs)".format(total_avg, int(total_avg // len(days)), len(runtimes)))


def run_all_get_data(runs):
	runtimes = []
	for i in range(runs):
		total_time = 0
		for day in days:
			stime = time.time_ns()
			day.get_data(os.path.join(os.path.dirname(day.__file__), "input.txt"))
			total_time += time.time_ns() - stime
		runtimes.append(total_time)
	total_avg = (sum(runtimes) / len(runtimes)) / 1000000
	print("2025 get_data -- took {} ms (average {} ms per day over {} runs)".format(total_avg, int(total_avg // len(days)), len(runtimes)))


def run_all_part_one_no_data(runs):
	run_part_with_no_data(runs, False)


def run_all_part_two_no_data(runs):
	run_part_with_no_data(runs, True)


def run_part_with_no_data(runs, part2):
	runtimes = []
	for i in range(runs):
		total_time = 0
		for day in days:
			d = day.get_data(os.path.join(os.path.dirname(day.__file__), "input.txt"))
			f = day.part_two if part2 else day.part_one
			stime = time.time_ns()
			f(d)
			total_time += time.time_ns() - stime
		runtimes.append(total_time)
	total_avg = (sum(runtimes) / len(runtimes)) / 1000000
	print("2025 {} -- took {} ms (average {} ms per day over {} runs)".format("part_two" if part2 else "part_one", total_avg, int(total_avg // len(days)), len(runtimes)))


def main():
	runs = 20000
	# run_all_get_data(runs)
	# run_all_part_one_no_data(runs)
	run_all_part_two_no_data(runs)
	# run_all(runs)


if __name__ == "__main__":
	main()

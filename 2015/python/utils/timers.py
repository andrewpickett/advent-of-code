import time


def get_data_with_timer(f, filename):
	stime = time.time_ns()
	result = f(filename)
	etime = time.time_ns()
	print("{} -- took {} ms".format(f.__name__, (etime - stime) // 1000000))
	return result


def run_with_timer(f, d):
	stime = time.time_ns()
	result = f(d)
	etime = time.time_ns()
	print("{} -- {} -- took {} ms".format(f.__name__, result, (etime - stime) // 1000000))
	return result

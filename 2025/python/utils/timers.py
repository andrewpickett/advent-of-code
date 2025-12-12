import time


def get_data_with_timer(f, filename) -> object:
	with open(filename) as file_obj:
		stime = time.time_ns()
		result = f(file_obj)
		etime = time.time_ns()
	print("{} -- took {} ms".format(f.__name__, (etime - stime) // 1000000))
	return result


def run_with_timer(f, d) -> object:
	stime = time.time_ns()
	result = f(d)
	etime = time.time_ns()
	print("{} -- {} -- took {} ms".format(f.__name__, result, (etime - stime) // 1000000))
	return result

from utils.timers import run_with_timer, get_data_with_timer


ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class Worker:

	def __init__(self, timer=60, weighted=True):
		self.orig_timer = timer
		self.timer = 0
		self.item = None
		self.weighted = weighted

	def set_item(self, item):
		self.item = item
		self.timer = (ALPHA.find(item) if self.weighted else 0) + self.orig_timer + 1

	def work(self):
		ret_val = None
		if self.item:
			self.timer -= 1
		if self.timer == 0:
			ret_val = self.item
			self.item = None
		return ret_val

	def can_work(self):
		return self.item is None


def get_data(filename):
	ret_val = {"avail": [], "steps": {}, "reqs": {}, "workers": 5, "timer": 60}
	avail = set()
	for line in [x.strip() for x in open(filename).readlines()]:
		parts = line.split()
		if parts[1] not in ret_val["steps"]:
			ret_val["steps"][parts[1]] = []
		if parts[7] not in ret_val["reqs"]:
			ret_val["reqs"][parts[7]] = []
		ret_val["steps"][parts[1]].append(parts[7])
		ret_val["reqs"][parts[7]].append(parts[1])
		avail.add(parts[1])
	for k, v in ret_val["steps"].items():
		for x in v:
			if x in avail:
				avail.remove(x)
	ret_val["avail"] = list(sorted(avail))
	return ret_val


def run_workers(d, workers):
	avail = d["avail"].copy()
	path = []
	t = 0
	while len(avail) > 0 or are_workers_working(workers):
		added_steps = []
		working_steps = []
		for worker in workers:
			if worker.can_work() and len(avail) > 0:
				worker.set_item(avail.pop(0))
			i = worker.work()
			if worker.item:
				working_steps.append(worker.item)
			if i:
				added_steps.append(i)
		added_steps.sort()
		path.extend(added_steps)
		next_available = get_next_available_steps(path, working_steps, avail, d)
		avail.extend(next_available)
		avail.sort()
		t += 1
	return path, t


def are_workers_working(workers):
	return sum(1 for worker in workers if not worker.can_work()) > 0


def get_next_available_steps(completed, working_steps, avail, d):
	return [step for step in [x for x in d["reqs"] if x not in completed and x not in working_steps and x not in avail] if sum(1 for req in d["reqs"][step] if req not in completed) == 0]


def part_one(d):
	path, t = run_workers(d, [Worker(d["timer"], False)])
	return ''.join(path)


def part_two(d):
	workers = []
	for _ in range(d["workers"]):
		workers.append(Worker(d["timer"], True))
	path, t = run_workers(d, workers)
	return t


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

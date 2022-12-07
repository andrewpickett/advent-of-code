from aoc_utils import run_with_timer

data = [x.strip().split() for x in open("input.txt").readlines()]


class File:
	def __init__(self, name, level, size, is_dir, parent):
		self.name = name
		self.level = level
		self.is_dir = is_dir
		self.size = size
		self.files = set()
		self.parent = parent

	def update_size(self):
		self.size = 0
		for file in self.files:
			if file.is_dir:
				file.update_size()
			self.size += file.size

	def add_file(self, file):
		self.files.add(file)

	def __eq__(self, other):
		return self.name == other.name and self.level == other.level

	def __str__(self):
		return "".ljust(self.level * 2, " ") + (self.name + "(" + str(self.size) + ")")

	def __repr__(self):
		return "".ljust(self.level * 2, " ") + (self.name + "[" + str(self.level) + "] -- (" + str(self.size) + ")")

	def __hash__(self):
		return hash(self.name) * 3 + hash(str(self.level)) * 7


def build_filesystem():
	root = File("/", 0, 0, True, None)
	curr_file = root
	all_files = [curr_file]
	for x in data:
		if x[0] == "$":
			if x[1] == "cd":
				if x[2] == "..":
					curr_file = curr_file.parent
				elif x[2] == "/":
					curr_file = root
				else:
					f = File(x[2], curr_file.level+1, 0, True, curr_file)
					for file in all_files:
						if file == f:
							f = file
					curr_file = f
		elif x[0].isnumeric():
			new_file = File(x[1], curr_file.level+1, int(x[0]), False, curr_file)
			curr_file.add_file(new_file)
			all_files.append(new_file)
		elif x[0] == "dir":
			new_file = File(x[1], curr_file.level+1, 0, True, curr_file)
			all_files.append(new_file)
			curr_file.add_file(new_file)
	root.update_size()
	return all_files, root


def part_one():
	all_files, root = build_filesystem()
	return sum(x.size for x in all_files if x.is_dir and x.size <= 100000)


def part_two():
	all_files, root = build_filesystem()
	space_needed = root.size - 40000000
	min_file = None
	for x in all_files:
		if x.is_dir and x.size >= space_needed:
			if min_file is None or min_file.size > x.size:
				min_file = x
	return min_file.size


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #

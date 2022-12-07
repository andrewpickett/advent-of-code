from aoc_utils import run_with_timer

data = [x.strip().split() for x in open("input.txt").readlines()]


class FileSystem:
	def __init__(self, root=None):
		self.root = root
		self.current_directory = self.root

	def change_directory(self, path):
		if path == "/":
			self.current_directory = self.root
		elif path == "..":
			self.current_directory = self.current_directory.parent
		else:
			for file in self.current_directory.files:
				if file.is_dir and file.name == path:
					self.current_directory = file
					return

	def list_files(self):
		return

	def handle_listed_file(self, file_type, file_name):
		if file_type == "dir":
			new_file = File(file_name, self.current_directory.level + 1, parent=self.current_directory)
			self.current_directory.add_file(new_file)
		elif file_type.isnumeric():
			new_file = File(file_name, self.current_directory.level + 1, int(file_type), False, self.current_directory)
			self.current_directory.add_file(new_file)

	def get_all_directories(self):
		return self.root.get_all_directories()


class File:
	def __init__(self, name, level, size=0, is_dir=True, parent=None):
		self.name = name
		self.level = level
		self.is_dir = is_dir
		self.size = size
		self.files = []
		self.parent = parent
		self.needs_update = False

	def update_size(self):
		if self.needs_update:
			self.size = 0
			for file in self.files:
				if file.is_dir:
					file.update_size()
				self.size += file.size
			self.needs_update = False

	def add_file(self, file):
		if file not in self.files:
			self.needs_update = True
			self.files.append(file)

	def get_all_directories(self):
		all_dirs = []
		if self.is_dir:
			all_dirs.append(self)
			for file in self.files:
				if file.is_dir:
					all_dirs.extend(file.get_all_directories())
		return all_dirs

	def __eq__(self, other):
		return self.name == other.name and self.level == other.level

	def __hash__(self):
		return hash(self.name) * 3 + hash(str(self.level)) * 7


def build_filesystem():
	fs = FileSystem(File("/", 0))
	for x in data:
		if x[0] == "$":
			if x[1] == "cd":
				fs.change_directory(x[2])
			if x[1] == "ls":
				fs.list_files()
		else:
			fs.handle_listed_file(x[0], x[1])
	fs.root.update_size()
	return fs


def part_one():
	return sum(x.size for x in build_filesystem().get_all_directories() if x.size <= 100000)


def part_two():
	fs = build_filesystem()
	return min([x.size for x in fs.get_all_directories() if x.size >= fs.root.size - 40000000])


if __name__ == '__main__':
	run_with_timer(part_one)  # 1644735 -- took 1 ms
	run_with_timer(part_two)  # 1300850 -- took 1 ms

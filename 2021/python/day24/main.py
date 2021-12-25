from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]

'''
By analyzing the input by HAND, I was able to come up with these constraints on the input:
	D - 1 = E
	C - 5 = F
	H + 3 = I
	G + 7 = J
	K + 2 = L
	B - 2 = M
	A + 4 = N
With that, we can put concrete constraints on the possible values for each position in the model number. These are below.
'''
constraints = [
	[1, 2, 3, 4, 5],
	[3, 4, 5, 6, 7, 8, 9],
	[6, 7, 8, 9],
	[2, 3, 4, 5, 6, 7, 8, 9],
	[1, 2, 3, 4, 5, 6, 7, 8],
	[1, 2, 3, 4],
	[1, 2],
	[1, 2, 3, 4, 5, 6],
	[4, 5, 6, 7, 8, 9],
	[8, 9],
	[1, 2, 3, 4, 5, 6, 7],
	[3, 4, 5, 6, 7, 8, 9],
	[1, 2, 3, 4, 5, 6, 7],
	[5, 6, 7, 8, 9]
]

class ALU:
	def __init__(self, i):
		self.input = i
		self.variables = {"w": 0, "x": 0, "y": 0, "z": 0}
		self.input_counter = 0

	def __str__(self):
		return str(self.variables)

	def __repr__(self):
		return str(self)

	def run(self, instructions):
		for inst in instructions:
			self.run_inst(inst)

	def run_inst(self, inst):
		parts = inst.split(" ")
		if len(parts) == 2:
			self.inp(parts[1])
		else:
			if parts[0] == 'add':
				self.add(parts[1], parts[2])
			elif parts[0] == 'mul':
				self.mul(parts[1], parts[2])
			elif parts[0] == 'div':
				self.div(parts[1], parts[2])
			elif parts[0] == 'mod':
				self.mod(parts[1], parts[2])
			elif parts[0] == 'eql':
				self.eql(parts[1], parts[2])

	def inp(self, a):
		self.variables[a] = int(self.input[self.input_counter])
		self.input_counter += 1

	def add(self, a, b):
		self.variables[a] = self.variables[a] + self.variables[b] if b in self.variables else self.variables[a] + int(b)

	def mul(self, a, b):
		self.variables[a] = self.variables[a] * self.variables[b] if b in self.variables else self.variables[a] * int(b)

	def div(self, a, b):
		self.variables[a] = self.variables[a] // self.variables[b] if b in self.variables else self.variables[a] // int(b)

	def mod(self, a, b):
		self.variables[a] = self.variables[a] % self.variables[b] if b in self.variables else self.variables[a] % int(b)

	def eql(self, a, b):
		if b in self.variables:
			self.variables[a] = 1 if self.variables[a] == self.variables[b] else 0
		else:
			self.variables[a] = 1 if self.variables[a] == int(b) else 0


def part_one():
	model_number = ''.join([str(max(x)) for x in constraints])
	# Don't actually need to run these through the ALU afterall...but am doing it just as a verification step...
	alu = ALU(model_number)
	alu.run(data)
	if alu.variables["z"] == 0:
		return model_number
	return None


def part_two():
	model_number = ''.join([str(min(x)) for x in constraints])
	# Don't actually need to run these through the ALU afterall...but am doing it just as a verification step...
	alu = ALU(model_number)
	alu.run(data)
	if alu.variables["z"] == 0:
		return model_number
	return None


if __name__ == '__main__':
	run_with_timer(part_one)  #
	run_with_timer(part_two)  #


# Must end in a 9...

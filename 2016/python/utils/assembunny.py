class AssembunnyProgram:
	DEFAULT_REGISTERS = {"a": 0, "b": 0, "c": 0, "d": 0, "out": []}

	def __init__(self, code, registers=None):
		self.code = []
		for x in code:
			self.code.append(AssembunnyInstruction.get_instance(x))
		self.pointer = 0
		self.registers = self.DEFAULT_REGISTERS if not registers else registers
		if "out" not in self.registers:
			self.registers["out"] = []

	def run(self, limit=float("inf")):
		counter = 0
		while self.pointer < len(self.code):
			if counter > limit:
				return 1119
			self.pointer += self.code[self.pointer].eval(self.code, self.pointer, self.registers)
			if len(self.registers["out"]) > 1:
				if (self.registers["out"][-2] == 1 and self.registers["out"][-1] != 0) or (self.registers["out"][-2] == 0 and self.registers["out"][-1] != 1):
					return False
			# print(self.registers)
			counter += 1
		return counter


class AssembunnyInstruction:
	def __init__(self, op, args):
		self.op = op
		self.args = args
		self.valid = True

	@staticmethod
	def get_instance(i):
		parts = i.split(" ")
		match parts[0]:
			case "cpy":
				return AssembunnyCopy(parts[1:])
			case "jnz":
				return AssembunnyJumpNotZero(parts[1:])
			case "inc":
				return AssembunnyIncrease(parts[1:])
			case "dec":
				return AssembunnyDecrease(parts[1:])
			case "tgl":
				return AssembunnyToggle(parts[1:])
			case "out":
				return AssembunnyOut(parts[1:])

	def eval(self, code, pointer, registers):
		print("Unknown operation", self.op, self.args)

	def __str__(self):
		return "{} {} {}".format(self.op, self.args, self.valid)

	def __repr__(self):
		return "{} {} {}".format(self.op, self.args, self.valid)


class AssembunnyCopy(AssembunnyInstruction):
	OP_NAME = "cpy"

	def __init__(self, args):
		super().__init__(self.OP_NAME, args)
		self.valid = len(self.args) == 2 and not self.args[1].lstrip("+-").isnumeric()

	def eval(self, code, pointer, registers):
		if self.valid:
			registers[self.args[1]] = int(self.args[0]) if self.args[0].lstrip("+-").isnumeric() else registers[self.args[0]]
		return 1


class AssembunnyIncrease(AssembunnyInstruction):
	OP_NAME = "inc"

	def __init__(self, args):
		super().__init__(self.OP_NAME, args)
		self.valid = len(self.args) == 1 and not self.args[0].lstrip("+-").isnumeric()

	def eval(self, code, pointer, registers):
		if self.valid:
			registers[self.args[0]] += 1
		return 1


class AssembunnyDecrease(AssembunnyInstruction):
	OP_NAME = "dec"

	def __init__(self, args):
		super().__init__(self.OP_NAME, args)
		self.valid = len(self.args) == 1 and not self.args[0].lstrip("+-").isnumeric()

	def eval(self, code, pointer, registers):
		if self.valid:
			registers[self.args[0]] -= 1
		return 1


class AssembunnyJumpNotZero(AssembunnyInstruction):
	OP_NAME = "jnz"

	def __init__(self, args):
		super().__init__(self.OP_NAME, args)
		self.valid = len(self.args) == 2

	def eval(self, code, pointer, registers):
		if self.valid:
			v1 = int(self.args[0]) if self.args[0].lstrip("+-").isnumeric() else registers[self.args[0]]
			v2 = int(self.args[1]) if self.args[1].lstrip("+-").isnumeric() else registers[self.args[1]]
			return 1 if v1 == 0 else v2
		return 1


class AssembunnyToggle(AssembunnyInstruction):
	OP_NAME = "tgl"

	def __init__(self, args):
		super().__init__(self.OP_NAME, args)
		self.valid = len(self.args) == 1 and not self.args[0].lstrip("+-").isnumeric()

	def eval(self, code, pointer, registers):
		if self.valid:
			v = int(self.args[0]) if self.args[0].lstrip("+-").isnumeric() else registers[self.args[0]]
			if 0 <= pointer + v < len(code):
				i = code[pointer + v]
				if len(i.args) == 1:
					code[pointer + v] = AssembunnyDecrease(i.args) if i.op == "inc" else AssembunnyIncrease(i.args)
				else:
					code[pointer + v] = AssembunnyCopy(i.args) if i.op == "jnz" else AssembunnyJumpNotZero(i.args)
		return 1


class AssembunnyOut(AssembunnyInstruction):
	OP_NAME = "out"

	def __init__(self, args):
		super().__init__(self.OP_NAME, args)
		self.valid = len(self.args) == 1 and not self.args[0].lstrip("+-").isnumeric()

	def eval(self, code, pointer, registers):
		if self.valid:
			registers["out"].append(registers[self.args[0]])
		return 1

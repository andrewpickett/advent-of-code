class DuetProgram:
	DEFAULT_REGISTERS = {x: 0 for x in "abcdefghijklmnopqrstuvwxyz"}

	def __init__(self, code, sound=True):
		self.code = []
		for x in code:
			self.code.append(DuetInstruction.get_instance(x, sound))
		self.pointer = 0
		self.registers = self.DEFAULT_REGISTERS.copy()
		if "snd" not in self.registers:
			self.registers["snd"] = []
		if "rcv" not in self.registers:
			self.registers["rcv"] = []
		self.waiting = False
		self.sound = sound

	def run(self):
		while self.pointer < len(self.code):
			# For part 1, if I get to a receive and it's not 0, then return the last sound value.
			if self.code[self.pointer].op == DuetReceive.OP_NAME and self.sound:
				if self.code[self.pointer].eval(self.code, self.pointer, self.registers):
					return self.registers["snd"][-1]
				self.pointer += 1
			# For part 2, if I get a receive, then I receive the first value if there are any, otherwise I wait.
			elif self.code[self.pointer].op == DuetReceive.OP_NAME:
				if len(self.registers["rcv"]) == 0:
					self.waiting = True
					return self.registers["snd"].copy()
				else:
					self.pointer += self.code[self.pointer].eval(self.code, self.pointer, self.registers)
			else:
				self.pointer += self.code[self.pointer].eval(self.code, self.pointer, self.registers)
		return

	def send(self, other):
		other.registers["rcv"].extend(self.registers["snd"])
		other.waiting = len(self.registers["snd"]) == 0
		self.registers["snd"].clear()

class DuetInstruction:
	def __init__(self, op, args):
		self.op = op
		self.args = args

	@staticmethod
	def get_instance(i, sound):
		parts = i.split(" ")
		match parts[0]:
			case DuetSend.OP_NAME:
				return DuetSend(parts[1:])
			case DuetSet.OP_NAME:
				return DuetSet(parts[1:])
			case DuetAdd.OP_NAME:
				return DuetAdd(parts[1:])
			case DuetMultiply.OP_NAME:
				return DuetMultiply(parts[1:])
			case DuetModulo.OP_NAME:
				return DuetModulo(parts[1:])
			case DuetReceive.OP_NAME:
				return DuetReceive(parts[1:], sound)
			case DuetJump.OP_NAME:
				return DuetJump(parts[1:])

	def eval(self, code, pointer, registers):
		print("Unknown operation", self.op, self.args)

	def __str__(self):
		return "{} {}".format(self.op, self.args)

	def __repr__(self):
		return "{} {}".format(self.op, self.args)


class DuetSend(DuetInstruction):
	OP_NAME = "snd"

	def __init__(self, args):
		super().__init__(self.OP_NAME, args)

	def eval(self, code, pointer, registers):
		registers["snd"].append(int(self.args[0]) if self.args[0].lstrip("+-").isnumeric() else registers[self.args[0]])
		return 1


class DuetSet(DuetInstruction):
	OP_NAME = "set"

	def __init__(self, args):
		super().__init__(self.OP_NAME, args)

	def eval(self, code, pointer, registers):
		registers[self.args[0]] = int(self.args[1]) if self.args[1].lstrip("+-").isnumeric() else registers[self.args[1]]
		return 1


class DuetAdd(DuetInstruction):
	OP_NAME = "add"

	def __init__(self, args):
		super().__init__(self.OP_NAME, args)

	def eval(self, code, pointer, registers):
		registers[self.args[0]] += int(self.args[1]) if self.args[1].lstrip("+-").isnumeric() else registers[self.args[1]]
		return 1


class DuetMultiply(DuetInstruction):
	OP_NAME = "mul"

	def __init__(self, args):
		super().__init__(self.OP_NAME, args)

	def eval(self, code, pointer, registers):
		registers[self.args[0]] *= int(self.args[1]) if self.args[1].lstrip("+-").isnumeric() else registers[self.args[1]]
		return 1


class DuetModulo(DuetInstruction):
	OP_NAME = "mod"

	def __init__(self, args):
		super().__init__(self.OP_NAME, args)

	def eval(self, code, pointer, registers):
		registers[self.args[0]] %= int(self.args[1]) if self.args[1].lstrip("+-").isnumeric() else registers[self.args[1]]
		return 1


class DuetReceive(DuetInstruction):
	OP_NAME = "rcv"

	def __init__(self, args, sound):
		super().__init__(self.OP_NAME, args)
		self.sound = sound

	def eval(self, code, pointer, registers):
		if self.sound:
			v = int(self.args[0]) if self.args[0].lstrip("+-").isnumeric() else registers[self.args[0]]
			return v != 0
		else:
			registers[self.args[0]] = registers["rcv"].pop(0)
			return 1


class DuetJump(DuetInstruction):
	OP_NAME = "jgz"

	def __init__(self, args):
		super().__init__(self.OP_NAME, args)

	def eval(self, code, pointer, registers):
		arg1 = (int(self.args[0]) if self.args[0].lstrip("+-").isnumeric() else registers[self.args[0]])
		arg2 = (int(self.args[1]) if self.args[1].lstrip("+-").isnumeric() else registers[self.args[1]])
		return arg2 if arg1 > 0 else 1

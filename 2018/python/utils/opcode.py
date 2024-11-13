class OpCodeOperation:

	def __init__(self, op, immediate):
		self.op = op
		self.immediate = immediate

	@staticmethod
	def get_instance(op_name):
		return OP_CODES[op_name]

	def eval(self, instruction, registers):
		print("Unknown operation", self.immediate)

	def __str__(self):
		return "{} {}".format(self.op, self.immediate)

	def __repr__(self):
		return "{} {}".format(self.op, self.immediate)


class OpCodeAdd(OpCodeOperation):
	def __init__(self, immediate):
		super().__init__("add" + ("i" if immediate else "r"), immediate)

	def eval(self, instruction, registers):
		registers[instruction[3]] = registers[instruction[1]] + (instruction[2] if self.immediate else registers[instruction[2]])
		return registers


class OpCodeMul(OpCodeOperation):
	def __init__(self, immediate):
		super().__init__("mul" + ("i" if immediate else "r"), immediate)

	def eval(self, instruction, registers):
		registers[instruction[3]] = registers[instruction[1]] * (instruction[2] if self.immediate else registers[instruction[2]])
		return registers


class OpCodeBan(OpCodeOperation):
	def __init__(self, immediate):
		super().__init__("ban" + ("i" if immediate else "r"), immediate)

	def eval(self, instruction, registers):
		registers[instruction[3]] = registers[instruction[1]] & (instruction[2] if self.immediate else registers[instruction[2]])
		return registers


class OpCodeBor(OpCodeOperation):
	def __init__(self, immediate):
		super().__init__("bor" + ("i" if immediate else "r"), immediate)

	def eval(self, instruction, registers):
		registers[instruction[3]] = registers[instruction[1]] | (instruction[2] if self.immediate else registers[instruction[2]])
		return registers


class OpCodeSet(OpCodeOperation):
	def __init__(self, immediate):
		super().__init__("set" + ("i" if immediate else "r"), immediate)

	def eval(self, instruction, registers):
		registers[instruction[3]] = instruction[1] if self.immediate else registers[instruction[1]]
		return registers


class OpCodeGti(OpCodeOperation):
	def __init__(self, immediate=True):
		super().__init__("gti", immediate)

	def eval(self, instruction, registers):
		registers[instruction[3]] = 1 if instruction[1] > registers[instruction[2]] else 0
		return registers


class OpCodeGtr(OpCodeOperation):
	def __init__(self, immediate):
		super().__init__("gtr" + ("i" if immediate else "r"), immediate)

	def eval(self, instruction, registers):
		registers[instruction[3]] = 1 if registers[instruction[1]] > (instruction[2] if self.immediate else registers[instruction[2]]) else 0
		return registers


class OpCodeEqi(OpCodeOperation):
	def __init__(self, immediate=True):
		super().__init__("eqi", immediate)

	def eval(self, instruction, registers):
		registers[instruction[3]] = 1 if instruction[1] == registers[instruction[2]] else 0
		return registers


class OpCodeEqr(OpCodeOperation):
	def __init__(self, immediate=True):
		super().__init__("eqr" + ("i" if immediate else "r"), immediate)

	def eval(self, instruction, registers):
		registers[instruction[3]] = 1 if registers[instruction[1]] == (instruction[2] if self.immediate else registers[instruction[2]]) else 0
		return registers


OP_CODES = {
	"addi": OpCodeAdd(True),
	"addr": OpCodeAdd(False),
	"muli": OpCodeMul(True),
	"mulr": OpCodeMul(False),
	"bani": OpCodeBan(True),
	"banr": OpCodeBan(False),
	"bori": OpCodeBor(True),
	"borr": OpCodeBor(False),
	"seti": OpCodeSet(True),
	"setr": OpCodeSet(False),
	"gtir": OpCodeGti(),
	"gtri": OpCodeGtr(True),
	"gtrr": OpCodeGtr(False),
	"eqir": OpCodeEqi(),
	"eqri": OpCodeEqr(True),
	"eqrr": OpCodeEqr(False)
}

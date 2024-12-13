class OpcodeInstruction:
	def __init__(self, size):
		self.size = size

	def run(self, instructions, args):
		pass


class OpcodeAdd(OpcodeInstruction):
	def __init__(self):
		super().__init__(4)

	def run(self, instructions, args):
		instructions[args[3]] = instructions[args[1]] + instructions[args[2]]


class OpcodeMultiply(OpcodeInstruction):
	def __init__(self):
		super().__init__(4)

	def run(self, instructions, args):
		instructions[args[3]] = instructions[args[1]] * instructions[args[2]]


class OpcodeExit(OpcodeInstruction):
	def __init__(self):
		super().__init__(1)

	def run(self, instructions, args):
		pass


class IntcodeMachine:
	op_map = {
		1: OpcodeAdd(),
		2: OpcodeMultiply(),
		99: OpcodeExit()
	}

	def __init__(self, instructions):
		self.pointer = 0
		self.instructions = instructions
		self.running = False


	def run(self):
		self.running = True
		while self.running:
			if self.instructions[self.pointer] == 99:
				self.running = False
			self.run_instruction()


	def run_instruction(self):
		inst = IntcodeMachine.op_map[self.instructions[self.pointer]]
		args = self.instructions[self.pointer:self.pointer+inst.size]
		inst.run(self.instructions, args)
		self.pointer += len(args)

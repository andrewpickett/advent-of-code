class IntcodeMachine:

	def __init__(self, instructions):
		self._pointer = 0
		self.instructions = instructions
		self.running = False
		self.outputs = []
		self.inputs = []
		self._op_map = {
			1: self._op_add,
			2: self._op_multiply,
			3: self._op_input,
			4: self._op_output,
			5: self._op_jump_if_true,
			6: self._op_jump_if_false,
			7: self._op_less_than,
			8: self._op_equals
		}


	def set_inputs(self, inputs):
		self.inputs = inputs


	def run(self):
		self.running = True
		while self.running:
			code = str(self.instructions[self._pointer]).zfill(5)
			icode = int(code[-2:])
			if icode == 99:
				self.running = False
			else:
				self.run_instruction(code)


	def run_instruction(self, code):
		modes = code[:-2]
		params = [
			self.instructions[self._pointer + 1] if modes[-1] == "0" else self._pointer + 1,
			self.instructions[self._pointer + 2] if modes[-2] == "0" else self._pointer + 2,
			self.instructions[self._pointer + 3] if modes[-3] == "0" else self._pointer + 3,
		]
		self._op_map[int(code[-2:])](params)


	def _op_add(self, params):
		self.instructions[params[2]] = self.instructions[params[0]] + self.instructions[params[1]]
		self._pointer += 4

	def _op_multiply(self, params):
		self.instructions[params[2]] = self.instructions[params[0]] * self.instructions[params[1]]
		self._pointer += 4

	def _op_input(self, params):
		if self.inputs:
			self.instructions[params[0]] = self.inputs.pop(0)
		else:
			self.instructions[params[0]] = int(input(">> "))
		self._pointer += 2

	def _op_output(self, params):
		self.outputs.append(self.instructions[params[0]])
		self._pointer += 2

	def _op_jump_if_true(self, params):
		self._pointer = self.instructions[params[1]] if self.instructions[params[0]] != 0 else self._pointer + 3

	def _op_jump_if_false(self, params):
		self._pointer = self.instructions[params[1]] if self.instructions[params[0]] == 0 else self._pointer + 3

	def _op_less_than(self, params):
		self.instructions[params[2]] = 1 if self.instructions[params[0]] < self.instructions[params[1]] else 0
		self._pointer += 4

	def _op_equals(self, params):
		self.instructions[params[2]] = 1 if self.instructions[params[0]] == self.instructions[params[1]] else 0
		self._pointer += 4

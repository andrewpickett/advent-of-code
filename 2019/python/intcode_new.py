class IntcodeOpMachine:
	def __init__(self, instructions, input_vals=None):
		self.instructions = instructions
		self.input_vals = input_vals if input_vals else []
		self.prompt_for_input = False
		self._received_input = True if input_vals else False
		self.cycle_inputs = False
		self.output = []
		self.halted = False
		self._pointer = 0
		self._relative_base = 0
		self._input_pointer = 0
		self._op_map = {
			1: self._op_add,
			2: self._op_multiply,
			3: self._op_input,
			4: self._op_output,
			5: self._op_jump_if_true,
			6: self._op_jump_if_false,
			7: self._op_less_than,
			8: self._op_equals,
			9: self._op_relative_base
		}

	def run_until_halt(self):
		exit_code = 0
		while exit_code != 99:
			exit_code = self.run()

	def add_input(self, in_val, increment_pointer=True):
		self.input_vals.append(in_val)
		if increment_pointer:
			self._input_pointer += 1 if self._input_pointer + 1 < len(self.input_vals) else 0

	def run(self, dynamic_input=False):
		while True:
			op = self.instructions[self._pointer]
			str_op = str(op).zfill(5)
			if op == 99:
				self.halted = True
				return 99
			elif op == 3:
				if self.prompt_for_input:
					self.instructions[self._pointer + 1] = input(">> ")
				elif dynamic_input and not self._received_input:
					self._received_input = True
					return 3
			elif op > 99:
				op = int(str_op[3]) * 10 + int(str_op[4])

			self._perform_operation(op, int(str_op[2]), int(str_op[1]), int(str_op[0]))
			if op == 4:
				return 4
			elif op == 3:
				if dynamic_input:
					self._received_input = False

	def _perform_operation(self, op, param1_mode, param2_mode, param3_mode):
		param1_idx = self._get_param_index(param1_mode, self._pointer + 1)
		param2_idx = self._get_param_index(param2_mode, self._pointer + 2) if op in [1, 2, 5, 6, 7, 8] else 0
		param3_idx = self._get_param_index(param3_mode, self._pointer + 3) if op in [1, 2, 7, 8] else 0
		self._op_map[op]((param1_idx, param2_idx, param3_idx))

	def _get_param_index(self, mode, base_idx):
		if mode == 0:
			self._resize_array_if_needed(self.instructions[base_idx])
			return self.instructions[base_idx]
		elif mode == 1:
			return base_idx
		elif mode == 2:
			self._resize_array_if_needed(max(base_idx, self.instructions[base_idx] + self._relative_base))
			return self.instructions[base_idx] + self._relative_base

	def _resize_array_if_needed(self, base_idx):
		if base_idx >= len(self.instructions):
			self.instructions.extend([0] * (base_idx - len(self.instructions) + 1))

	def _op_add(self, params):
		self.instructions[params[2]] = self.instructions[params[0]] + self.instructions[params[1]]
		self._pointer += 4

	def _op_multiply(self, params):
		self.instructions[params[2]] = self.instructions[params[0]] * self.instructions[params[1]]
		self._pointer += 4

	def _op_input(self, params):
		self.instructions[params[0]] = self.input_vals[self._input_pointer]
		self._input_pointer += 1 if self._input_pointer + 1 < len(self.input_vals) else 0
		self._pointer += 2

	def _op_output(self, params):
		self.output.append(self.instructions[params[0]])
		self._pointer += 2

	def _op_jump_if_true(self, params):
		self._pointer = self.instructions[params[1]] if self.instructions[params[0]] else self._pointer + 3

	def _op_jump_if_false(self, params):
		self._pointer = self.instructions[params[1]] if not self.instructions[params[0]] else self._pointer + 3

	def _op_less_than(self, params):
		self.instructions[params[2]] = 1 if self.instructions[params[0]] < self.instructions[params[1]] else 0
		self._pointer += 4

	def _op_equals(self, params):
		self.instructions[params[2]] = 1 if self.instructions[params[0]] == self.instructions[params[1]] else 0
		self._pointer += 4

	def _op_relative_base(self, params):
		self._relative_base += self.instructions[params[0]]
		self._pointer += 2

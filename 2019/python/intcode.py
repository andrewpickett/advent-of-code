class IntcodeOpMachine:
	def __init__(self, instructions, in_val=0, phase_setting=-1):
		self.instructions = instructions
		self.pointer = 0
		self.output = []
		self.in_val = in_val
		self.phase_setting = phase_setting
		self.set_phase = False
		self.halted = False
		self.relative_base = 0
		self.op_map = {
			1: self.op_add,
			2: self.op_multiply,
			3: self.op_input,
			4: self.op_output,
			5: self.op_jump_if_true,
			6: self.op_jump_if_false,
			7: self.op_less_than,
			8: self.op_equals,
			9: self.op_relative_base
		}

	def run_until_halt(self):
		exit_code = 0
		while exit_code != 99:
			exit_code = self.run()

	def run(self):
		while True:
			op = self.instructions[self.pointer]
			str_op = str(op).zfill(5)
			if op == 99:
				self.halted = True
				return 99
			elif op > 99:
				op = int(str_op[3]) * 10 + int(str_op[4])

			self.perform_operation(op, int(str_op[2]), int(str_op[1]), int(str_op[0]))
			if op == 4:
				return 4

	def perform_operation(self, op, param1_mode, param2_mode, param3_mode):
		param1_idx = self.get_param_index(param1_mode, self.pointer + 1)
		param2_idx = self.get_param_index(param2_mode, self.pointer + 2) if op in [1, 2, 5, 6, 7, 8] else 0
		param3_idx = self.get_param_index(param3_mode, self.pointer + 3) if op in [1, 2, 7, 8] else 0
		self.op_map[op]((param1_idx, param2_idx, param3_idx))

	def get_param_index(self, mode, base_idx):
		if mode == 0:
			self.resize_array_if_needed(self.instructions[base_idx])
			return self.instructions[base_idx]
		elif mode == 1:
			return base_idx
		elif mode == 2:
			self.resize_array_if_needed(max(base_idx, self.instructions[base_idx] + self.relative_base))
			return self.instructions[base_idx] + self.relative_base

	def resize_array_if_needed(self, base_idx):
		if base_idx >= len(self.instructions):
			self.instructions.extend([0] * (base_idx - len(self.instructions) + 1))

	def op_add(self, params):
		self.instructions[params[2]] = self.instructions[params[0]] + self.instructions[params[1]]
		self.pointer += 4

	def op_multiply(self, params):
		self.instructions[params[2]] = self.instructions[params[0]] * self.instructions[params[1]]
		self.pointer += 4

	def op_input(self, params):
		self.instructions[params[0]] = self.phase_setting if not self.set_phase and self.phase_setting >= 0 else self.in_val
		self.set_phase = True
		self.pointer += 2

	def op_output(self, params):
		self.output.append(self.instructions[params[0]])
		self.pointer += 2

	def op_jump_if_true(self, params):
		self.pointer = self.instructions[params[1]] if self.instructions[params[0]] else self.pointer + 3

	def op_jump_if_false(self, params):
		self.pointer = self.instructions[params[1]] if not self.instructions[params[0]] else self.pointer + 3

	def op_less_than(self, params):
		self.instructions[params[2]] = 1 if self.instructions[params[0]] < self.instructions[params[1]] else 0
		self.pointer += 4

	def op_equals(self, params):
		self.instructions[params[2]] = 1 if self.instructions[params[0]] == self.instructions[params[1]] else 0
		self.pointer += 4

	def op_relative_base(self, params):
		self.relative_base += self.instructions[params[0]]
		self.pointer += 2

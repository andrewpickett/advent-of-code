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
		if op == 1:
			self.instructions[param3_idx] = self.instructions[param1_idx] + self.instructions[param2_idx]
			self.pointer += 4
		elif op == 2:
			self.instructions[param3_idx] = self.instructions[param1_idx] * self.instructions[param2_idx]
			self.pointer += 4
		elif op == 3:
			self.instructions[param1_idx] = self.phase_setting if not self.set_phase and self.phase_setting >= 0 else self.in_val
			self.set_phase = True
			self.pointer += 2
		elif op == 4:
			self.output.append(self.instructions[param1_idx])
			self.pointer += 2
		elif op == 5:
			self.pointer = self.instructions[param2_idx] if self.instructions[param1_idx] else self.pointer + 3
		elif op == 6:
			self.pointer = self.instructions[param2_idx] if not self.instructions[param1_idx] else self.pointer + 3
		elif op == 7:
			self.instructions[param3_idx] = 1 if self.instructions[param1_idx] < self.instructions[param2_idx] else 0
			self.pointer += 4
		elif op == 8:
			self.instructions[param3_idx] = 1 if self.instructions[param1_idx] == self.instructions[param2_idx] else 0
			self.pointer += 4
		elif op == 9:
			self.relative_base += self.instructions[param1_idx]
			self.pointer += 2

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

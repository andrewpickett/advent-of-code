from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def run_until_loop_or_end(instructions):
	curr_ins = 0
	run_instructions = set()
	accumulator = 0
	while curr_ins not in run_instructions and curr_ins < len(instructions):
		run_instructions.add(curr_ins)
		parts = instructions[curr_ins].split()

		if parts[0] == 'acc':
			accumulator += int(parts[1])
			curr_ins += 1
		elif parts[0] == 'nop':
			curr_ins += 1
		elif parts[0] == 'jmp':
			curr_ins += int(parts[1])
	return accumulator, curr_ins >= len(instructions)


def part_one():
	return run_until_loop_or_end(data.copy())[0]


def part_two():
	ins_repl = 0
	swaps = {'jmp':'nop', 'nop':'jmp'}
	while ins_repl < len(data):
		insts = data.copy()
		if insts[ins_repl].split()[0] == 'acc':
			ins_repl += 1
			continue
		swap_key = insts[ins_repl].split()[0]
		insts[ins_repl] = insts[ins_repl].replace(swap_key, swaps[swap_key])
		run_result = run_until_loop_or_end(insts)
		if run_result[1]:
			return run_result[0]
		ins_repl += 1
	return None


if __name__ == '__main__':
	run_with_timer(part_one)  # 1262 -- took 0 ms
	run_with_timer(part_two)  # 1643 -- took 26 ms

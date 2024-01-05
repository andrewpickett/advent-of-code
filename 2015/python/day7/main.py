from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return [x.strip() for x in open(filename).readlines()]


def operand(op, signals):
	return int(op) if op.isnumeric() else (signals[op] if op in signals.keys() else False)


def validate_operands(lhs, signals):
	for o in lhs:
		if o not in ['NOT', 'AND', 'OR', 'LSHIFT', 'RSHIFT'] and not o.isnumeric() and o not in signals.keys():
			return False
	return True


def run_instruction_book(d, signals):
	completed_ins = []
	while len(completed_ins) < len(d):
		for x in d:
			if x not in completed_ins:
				lhs = x.split(' -> ')[0].split(' ')
				rhs = x.split(' -> ')[1]

				if rhs in signals.keys():
					completed_ins.append(x)
				elif validate_operands(lhs, signals):
					if len(lhs) == 1:
						signals[rhs] = operand(lhs[0], signals)
					if 'AND' in lhs:
						signals[rhs] = operand(lhs[0], signals) & operand(lhs[2], signals)
					elif 'OR' in lhs:
						signals[rhs] = operand(lhs[0], signals) | operand(lhs[2], signals)
					elif 'NOT' in lhs:
						signals[rhs] = ~operand(lhs[1], signals) & 0xffff
					elif 'LSHIFT' in lhs:
						signals[rhs] = operand(lhs[0], signals) << int(lhs[2])
					elif 'RSHIFT' in lhs:
						signals[rhs] = operand(lhs[0], signals) >> int(lhs[2])
					completed_ins.append(x)


def part_one(d):
	signals = {}
	run_instruction_book(d, signals)
	return signals['a']


def part_two(d):
	signals = {'b': part_one(d)}
	run_instruction_book(d, signals)
	return signals['a']


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

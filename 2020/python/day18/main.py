import math
from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def eval_stmt(stmt):
	curr_val = int(stmt[0])
	curr_op = stmt[1]
	for x in stmt[2:]:
		if x == '+' or x == '*':
			curr_op = x
		else:
			if curr_op == '+':
				curr_val += int(x)
			elif curr_op == '*':
				curr_val *= int(x)
	return curr_val


def eval_stmt_with_precedence(stmt):
	while '+' in stmt:
		idx = stmt.index('+')
		new_val = int(stmt[idx-1]) + int(stmt[idx+1])
		stmt = stmt[:idx-1] + [new_val] + stmt[idx+2:]
	return math.prod(int(x) for x in stmt if x != '*')


def lex_parse_eval(equation, precedence):
	statement_stack = [[]]
	tokens = equation.split()
	e = eval_stmt_with_precedence if precedence else eval_stmt
	for token in tokens:
		if token.count(')') > 0:
			statement_stack[-1].append(token[:-token.count(')')])
			for i in range(token.count(')')):
				statement_stack[-2].append(e(statement_stack.pop()))
		elif token.count('(') > 0:
			for i in range(token.count('(')):
				statement_stack.append([])
			statement_stack[-1].append(token[token.count('('):])
		else:
			statement_stack[-1].append(token)
	return e(statement_stack.pop())


def part_one():
	return sum(lex_parse_eval(x, False) for x in data)


def part_two():
	return sum(lex_parse_eval(x, True) for x in data)


if __name__ == '__main__':
	run_with_timer(part_one)  # 1890866893020 -- took 6 ms
	run_with_timer(part_two)  # 34646237037193 -- took 8 ms

from aoc_utils import run_with_timer
import re

data = [x.strip().split(" ") for x in open("input.txt").readlines()]


def parse_input():
	monkeys = {}
	for x in data:
		name = x[0][:-1]
		if x[1].isnumeric():
			monkeys[name] = {"value": int(x[1])}
		else:
			monkeys[name] = {"other1": x[1], "op": x[2], "other2": x[3], "value": False}
	return monkeys


def calc_value(monkeys, monkey):
	m = monkeys[monkey]
	if "other1" not in m:
		return m["value"]

	match m["op"]:
		case "+":
			m["value"] = calc_value(monkeys, m["other1"]) + calc_value(monkeys, m["other2"])
		case "-":
			m["value"] = calc_value(monkeys, m["other1"]) - calc_value(monkeys, m["other2"])
		case "*":
			m["value"] = calc_value(monkeys, m["other1"]) * calc_value(monkeys, m["other2"])
		case "/":
			m["value"] = calc_value(monkeys, m["other1"]) // calc_value(monkeys, m["other2"])

	return m["value"]


def find_node(monkeys, monkey, target):
	m = monkeys[monkey]
	if monkey == target:
		return True

	if "other1" not in m:
		return False

	return find_node(monkeys, m["other1"], target) or find_node(monkeys, m["other2"], target)


def build_equation(monkeys, monkey):
	m = monkeys[monkey]
	if monkey == "humn":
		return "x"

	if "other1" not in m:
		return str(m["value"])

	return "(" + build_equation(monkeys, m["other1"]) + m["op"] + build_equation(monkeys, m["other2"]) + ")"


def simplify_op(equation, op):
	ops = re.compile(r"\(\d+" + re.escape(op) + r"\d+\)")
	result = ops.search(equation)
	simplified = False
	while result:
		equation = equation.replace(result.group(), str(eval(result.group().replace("/", "//"))))
		result = ops.search(equation)
		simplified = True
	return equation, simplified


def simplify(equation):
	was_simplified = True
	while was_simplified:
		was_simplified = False
		equation, simplified = simplify_op(equation, "+")
		was_simplified = was_simplified or simplified
		equation, simplified = simplify_op(equation, "-")
		was_simplified = was_simplified or simplified
		equation, simplified = simplify_op(equation, "*")
		was_simplified = was_simplified or simplified
		equation, simplified = simplify_op(equation, "/")
		was_simplified = was_simplified or simplified
	return equation


def op_on_x(x, op, val, left):
	match op:
		case "+":
			return x - val
		case "-":
			return abs(x - val) if left else x + val
		case "*":
			return x // val
		case "/":
			return x * val


def solve_for_x(eq, start_val):
	eq = eq[1:-1]		# remove beginning and ending ().
	x = start_val
	while eq.find("(") >= 0:
		e = eq.rindex(")")
		s = eq.index("(")
		if eq.startswith("("):
			# get last operation from end and reverse it (y op ##)
			x = op_on_x(x, eq[e+1], int(eq[e+2:]), False)
			eq = eq[1:e]
		else:
			# get first operation from start and reverse it (## op y)
			x = op_on_x(x, eq[s-1], int(eq[:s-1]), True)
			eq = eq[s+1:-1]
	x = op_on_x(x, eq[1], int(eq[2:]), False)
	return x


def part_one():
	monkeys = parse_input()
	return calc_value(monkeys, "root")


def part_two():
	monkeys = parse_input()
	o1 = monkeys["root"]["other1"]
	o2 = monkeys["root"]["other2"]
	o2_val = calc_value(monkeys, o2)

	return solve_for_x(simplify(build_equation(monkeys, o1)), o2_val)


if __name__ == '__main__':
	run_with_timer(part_one)  # 81075092088442 -- took 1 ms
	run_with_timer(part_two)  # 3349136384441 -- took 14 ms

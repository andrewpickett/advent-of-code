from aoc_utils import run_with_timer

data = [x.strip().split(" ") for x in open("input.txt").readlines()]


def parse_input():
	monkeys = {}
	curr_monkey = None
	for x in data:
		if x[0] == "Monkey":
			curr_monkey = {"inspections": 0}
			monkeys[int(x[1][:-1])] = curr_monkey
		elif x[0] == "Starting":
			curr_monkey["items"] = [int(y.replace(",", "")) for y in x[2:]]
		elif x[0] == "Operation:":
			curr_monkey["op"] = x[4:]
		elif x[0] == "Test:":
			curr_monkey["mod"] = int(x[3])
		elif x[0] == "If" and x[1] == "true:":
			curr_monkey["true"] = int(x[5])
		elif x[0] == "If" and x[1] == "false:":
			curr_monkey["false"] = int(x[5])
	return monkeys


def monkey_inspect(monkeys, rounds, relief_limiter):
	for _ in range(rounds):
		for monkey in monkeys.values():
			for item in monkey["items"]:
				monkey["inspections"] += 1
				new_worry_level = item
				if monkey["op"][0] == "+":
					new_worry_level += int(monkey["op"][1])
				elif monkey["op"][0] == "*":
					if monkey["op"][1].isnumeric():
						new_worry_level *= int(monkey["op"][1])
					else:
						new_worry_level *= new_worry_level
				new_worry_level = relief_limiter(new_worry_level)
				t = monkey["true" if new_worry_level % monkey["mod"] == 0 else "false"]
				monkeys[t]["items"].append(new_worry_level)
			monkey["items"] = []
	inspections = sorted([m["inspections"] for m in monkeys.values()])
	return inspections[-2] * inspections[-1]


def part_one():
	return monkey_inspect(parse_input(), 20, lambda x: x // 3)


def part_two():
	monkeys = parse_input()
	big_mod = 1
	for m in monkeys.values():
		big_mod *= m["mod"]
	return monkey_inspect(monkeys, 10000, lambda x: x % big_mod)


if __name__ == '__main__':
	run_with_timer(part_one)  # 55458 -- took 2 ms
	run_with_timer(part_two)  # 14508081294 -- took 1302 ms

from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def get_input_data():
	return data[:data.index('')], data[data.index('')+1:]


def parse_rule(s):
	rule_num, rule = s.split(": ")
	return (int(rule_num), rule) if '"' in rule else (int(rule_num), [[int(y) for y in x.split()] for x in rule.split("|")])


def test(rules, s, seq):
	if s == '' or seq == []:
		return s == '' and seq == []
	rule = rules[seq[0]]
	if '"' in rule:
		return test(rules, s[1:], seq[1:]) if s[0] in rule else False
	else:
		return any(test(rules, s, x+seq[1:]) for x in rule)


def part_one():
	rule_map, tests = get_input_data()
	rules = dict(parse_rule(x) for x in rule_map)
	return sum(test(rules, m, [0]) for m in tests)


def part_two():
	rule_map, tests = get_input_data()
	rule_map[rule_map.index('8: 42')] = '8: 42 | 42 8'
	rule_map[rule_map.index('11: 42 31')] = '11: 42 31 | 42 11 31'
	rules = dict(parse_rule(x) for x in rule_map)
	return sum(test(rules, m, [0]) for m in tests)


if __name__ == '__main__':
	run_with_timer(part_one)  # 226 -- took 77 ms
	run_with_timer(part_two)  # 355 -- took 283 ms

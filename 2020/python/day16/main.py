import math
from aoc_utils import run_with_timer

data = [x.strip() for x in open("input.txt").readlines()]


def get_validators():
	data_validators = {}
	for i in range(len(data)):
		if data[i].strip() == '':
			break
		parts = data[i].split(': ')
		rng = parts[1].split(' or ')
		max_val = int(rng[1].split('-')[1]) + 1
		next_valid_rng = [0] * max_val
		for r in rng:
			for x in range(int(r.split('-')[0]), int(r.split('-')[1])+1):
				next_valid_rng[x] = 1
		data_validators[parts[0]] = next_valid_rng

	all_valid_nums = [0] * max(len(y) for y in data_validators.values())
	for y in data_validators.values():
		for i in range(len(y)):
			all_valid_nums[i] = 1 if all_valid_nums[i] or y[i] else 0

	return data_validators, all_valid_nums


def get_my_ticket():
	for i, x in enumerate(data):
		if x == 'your ticket:':
			return data[i+1].split(',')


def get_other_tickets():
	return [data[i].split(',') for i in range(data.index('nearby tickets:') + 1, len(data))]


def get_invalid_tickets_and_values(tickets, all_valid_nums):
	invalid_tickets = []
	invalid_values = []
	for x in tickets:
		is_valid = True
		for y in x:
			if int(y) >= len(all_valid_nums) or all_valid_nums[int(y)] == 0:
				is_valid = False
				invalid_values.append(int(y))
		if not is_valid:
			invalid_tickets.append(x)
	return invalid_tickets, invalid_values


def part_one():
	data_validators, all_valid_nums = get_validators()
	invalid_tickets, invalid_values = get_invalid_tickets_and_values(get_other_tickets(), all_valid_nums)
	return sum(invalid_values)


def part_two():
	data_validators, all_valid_nums = get_validators()
	my_ticket = get_my_ticket()
	other_tickets = get_other_tickets()
	all_tickets = [my_ticket] + other_tickets
	invalid_tickets, invalid_values = get_invalid_tickets_and_values(all_tickets, all_valid_nums)
	all_tickets = [x for x in all_tickets if x not in invalid_tickets]

	possible_labels = [[y for y in data_validators.keys()] for x in range(len(all_tickets[0]))]
	for ticket in all_tickets:
		for i, val in enumerate(ticket):
			for label, validator in data_validators.items():
				if not validator[int(val)]:
					possible_labels[i].remove(label)

	actual_labels = [None] * len(possible_labels)
	while actual_labels.count(None) > 0:
		for i, x in enumerate(possible_labels):
			if len(x) == 1 and not actual_labels[i]:
				actual_labels[i] = x[0]
			elif len(x) > 1:
				possible_labels[i] = [y for y in x if y not in actual_labels]

	return math.prod(int(my_ticket[i]) for i, x in enumerate(actual_labels) if 'departure' in x)


if __name__ == '__main__':
	run_with_timer(part_one)  # 24110 -- took 4 ms
	run_with_timer(part_two)  # 6766503490793 -- took 24 ms

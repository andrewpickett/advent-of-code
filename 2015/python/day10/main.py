from utils.timers import run_with_timer


def get_data(filename):
	return [x for x in open(filename).readline().strip()]


def look_and_say(input_val):
	last_num = 0
	curr_count = 0
	new_str = ''
	for x in input_val:
		if int(x) != last_num:
			if curr_count > 0:
				new_str += str(curr_count) + str(last_num)
			last_num = int(x)
			curr_count = 0
		curr_count += 1
	new_str += str(curr_count) + str(last_num)
	return new_str


def part_one(d):
	new_val = d
	for x in range(40):
		new_val = look_and_say(new_val)
	return len(new_val)


def part_two(d):
	new_val = d
	for x in range(50):
		new_val = look_and_say(new_val)
	return len(new_val)


if __name__ == '__main__':
	data = get_data("input.txt")
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)

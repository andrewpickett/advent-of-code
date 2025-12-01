from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return {"d": [(x[0], int(x[1:])) for x in open(filename).readlines()], "s": 50}


def part_one(d):
	cur_pointer = d["s"]
	count = 0
	for x in d["d"]:
		cur_pointer = ((cur_pointer - x[1]) if x[0] == "L" else (cur_pointer + x[1])) % 100
		count = count + 1 if cur_pointer == 0 else count
	return count


def part_two(d):
	cur_pointer = d["s"]
	count = 0
	for x in d["d"]:
		tmp = cur_pointer - (x[1] % 100) if x[0] == "L" else cur_pointer + (x[1] % 100)
		if (tmp <= 0 or tmp > 99) and cur_pointer != 0:
			count += 1
		cur_pointer = tmp % 100
		if x[1] >= 100:
			count += x[1] // 100
	return count


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

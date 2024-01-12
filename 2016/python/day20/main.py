from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	ret_val = []
	for line in [x.strip() for x in open(filename).readlines()]:
		parts = [int(x) for x in line.split("-")]
		ret_val.append(range(parts[0], parts[1]+1))
	ret_val.sort(key=lambda x: x.start)
	return {"ips": ret_val, "max": 4294967295}


def get_next_combined_range(ips):
	curr_ip_range = ips[0]
	for i, x in enumerate(ips):
		if curr_ip_range.stop >= x.start:
			curr_ip_range = range(curr_ip_range.start, max(curr_ip_range.stop, x.stop))
		else:
			return i, curr_ip_range
	return len(ips), curr_ip_range


def part_one(d):
	return get_next_combined_range(d["ips"])[1].stop


def part_two(d):
	i, curr_ip_range = get_next_combined_range(d["ips"])
	combined_ips = [curr_ip_range]
	while i < len(d["ips"]):
		next_i, curr_ip_range = get_next_combined_range(d["ips"][i:])
		combined_ips.append(curr_ip_range)
		i += next_i
	total = 0
	for i, x in enumerate(combined_ips[:-1]):
		total += combined_ips[i+1].start - x.stop
	total += 0 if combined_ips[-1].stop > d["max"] else d["max"] - combined_ips[-1].stop
	return total


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

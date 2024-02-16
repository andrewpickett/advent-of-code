from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return {"programs": list("abcdefghijklmnop"), "moves": open(filename).readline().strip().split(",")}


def dance(programs, moves):
	progs = programs
	for x in moves:
		if x[0] == "s":
			spin = int(x[1:])
			progs = progs[-spin:] + progs[:-spin]
		elif x[0] == "x":
			idx = [int(y) for y in x[1:].split("/")]
			progs[idx[0]], progs[idx[1]] = progs[idx[1]], progs[idx[0]]
		elif x[0] == "p":
			idx = [progs.index(y) for y in x[1:].split("/")]
			progs[idx[0]], progs[idx[1]] = progs[idx[1]], progs[idx[0]]
	return progs


def part_one(d):
	return ''.join(dance(d["programs"].copy(), d["moves"]))


def part_two(d):
	next_dance = d["programs"].copy()
	seen_dances = [''.join(next_dance)]
	idx = 0
	for i in range(1000000000):
		next_dance = dance(next_dance, d["moves"])
		if ''.join(next_dance) in seen_dances:
			idx = i+1
			break
		seen_dances.append(''.join(next_dance))
	return seen_dances[1000000000 % idx]


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

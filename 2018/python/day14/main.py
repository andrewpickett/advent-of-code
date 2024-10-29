from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
	return open(filename).readline().strip()


def part_one(d):
	int_i = int(d)
	recipes = build_recipe_list(lambda a, b: len(a) < b, int_i + 11)
	return ''.join([str(x) for x in recipes[int_i:int_i+10]])


def part_two(d):
	recipes = build_recipe_list(lambda a, b: len(a) < b, 100000000)
	s = ''.join([str(x) for x in recipes])
	if d in s:
		return str(s.find(d))
	return None


def build_recipe_list(comp, val):
	recipes = [3, 7]
	elf_recipe_idx = [0, 1]
	while comp(recipes, val):
		next_rec = recipes[elf_recipe_idx[0]] + recipes[elf_recipe_idx[1]]
		if next_rec < 10:
			recipes.append(next_rec)
		else:
			recipes.extend([next_rec // 10, next_rec % 10])
		elf_recipe_idx = [(i+(recipes[i]+1)) % len(recipes) for i in elf_recipe_idx]
	return recipes


def main(f="input.txt"):
	data = get_data_with_timer(get_data, f)
	run_with_timer(part_one, data)
	run_with_timer(part_two, data)


if __name__ == '__main__':
	main()

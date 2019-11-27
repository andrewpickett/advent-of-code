import ir


def part_one():
    twos = 0
    threes = 0

    for line in ir.lines:
        found_twos = False
        found_threes = False
        for letter in line:
            found_twos = found_twos or line.count(letter) == 2
            found_threes = found_threes or line.count(letter) == 3

        twos = twos + 1 if found_twos else twos
        threes = threes + 1 if found_threes else threes
    return twos * threes


def part_two():
    for i in range(len(ir.lines)):
        start_line = ir.lines[i]
        for j in range(i + 1, len(ir.lines)):
            end_line = ir.lines[j]

            diff_count = 0
            diff_idx = 0
            for k in range(len(start_line)):
                if start_line[k] != end_line[k]:
                    diff_count += 1
                    diff_idx = k
                if diff_count > 1:
                    break

            if diff_count == 1:
                return start_line[:diff_idx] + start_line[diff_idx + 1:]


if __name__ == '__main__':
    ir.read_lines('./input.txt')
    print(part_one())
    print(part_two())

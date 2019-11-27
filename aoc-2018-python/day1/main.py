import ir


def part_one():
    frequency = 0
    for line in ir.lines:
        frequency += int(line)

    return frequency


def part_two():
    used_frequencies = [0] * 1000000
    frequency = 0
    done = False
    while not done:
        for line in ir.lines:
            frequency += int(line)
            if used_frequencies[frequency] > 0:
                done = True
                break
            else:
                used_frequencies[frequency] = 1
    return frequency


if __name__ == '__main__':
    ir.read_lines('./input.txt')
    print(part_one())
    print(part_two())

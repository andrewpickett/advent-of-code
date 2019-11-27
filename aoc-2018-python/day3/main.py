import ir

FABRIC_SIZE = 1000
OVERLAP_SPACE = 'X'
UNUSED_SPACE = '0'

fabric = [[UNUSED_SPACE for j in range(FABRIC_SIZE)] for i in range(FABRIC_SIZE)]


def part_one():
    total_duplicate = 0
    for i in range(len(fabric)):
        for j in range(len(fabric[i])):
            if fabric[i][j] == OVERLAP_SPACE:
                total_duplicate += 1
    return total_duplicate


def part_two():
    best_claim = 0
    for line in ir.lines:
        tokens = get_tokens(line)

        good_claim = True
        for j in range(tokens[1], tokens[1] + tokens[3]):
            for k in range(tokens[2], tokens[2] + tokens[4]):
                if fabric[j][k] == OVERLAP_SPACE:
                    good_claim = False
                    break
            if not good_claim:
                break
        if good_claim:
            best_claim = tokens[0]
            break
    return best_claim


def create_fabric_from_input():
    for line in ir.lines:
        tokens = get_tokens(line)

        for j in range(tokens[1], tokens[1] + tokens[3]):
            for k in range(tokens[2], tokens[2] + tokens[4]):
                if fabric[j][k] == UNUSED_SPACE:
                    fabric[j][k] = str(tokens[0])
                else:
                    fabric[j][k] = OVERLAP_SPACE


def get_tokens(line):
    tokens = line.split(' ')
    claim = int(tokens[0][1:])
    left = int(tokens[2].split(',')[0])
    top = int(tokens[2].split(',')[1][0:-1])
    width = int(tokens[3].split('x')[0])
    height = int(tokens[3].split('x')[1])

    return claim, left, top, width, height


if __name__ == '__main__':
    ir.read_lines('./input.txt')
    create_fabric_from_input()
    print(part_one())
    print(part_two())

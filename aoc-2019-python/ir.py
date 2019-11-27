lines = []


def read_lines(f):
    with open(f, 'r') as fp:
        for i, line in enumerate(fp):
            lines.append(line.strip())

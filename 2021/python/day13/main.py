from aoc_utils import run_with_timer, Grid, Point

data = [x.strip() for x in open("input.txt").readlines()]


def parse_data():
    pts = []
    folds = []
    on_points = True
    for x in data:
        if x == '':
            on_points = False
        else:
            if on_points:
                ps = [int(y) for y in x.split(",")]
                pts.append(Point(ps[1], ps[0]))
            else:
                folds.append(x[x.find("=") - 1:].split("="))
    return pts, folds


def fold(pts, d, val):
    for pt in pts:
        pt_val = pt.get_row() if d == 'y' else pt.get_col()
        if pt_val > val:
            new_val = val - (pt_val - val)
            if d == 'y':
                pt.set_row(new_val)
            else:
                pt.set_col(new_val)


def part_one():
    pts, folds = parse_data()
    fold(pts, folds[0][0], int(folds[0][1]))
    return len(set(pts))


def part_two():
    pts, folds = parse_data()
    for f in folds:
        fold(pts, f[0], int(f[1]))

    grid = Grid(max(pt.get_row() for pt in pts)+1, max(pt.get_col() for pt in pts)+1, default_value=" ")
    for p in set(pts):
        grid.get_point(p.get_row(), p.get_col()).set_value("#")
    return "\n" + str(grid)


if __name__ == '__main__':
    run_with_timer(part_one)  # 737 -- took 3 ms
    run_with_timer(part_two)  # ZUJUAFHP -- took 5 ms

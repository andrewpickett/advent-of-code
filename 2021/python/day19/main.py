from aoc_utils import run_with_timer

data = [x.strip() for x in open("sample.txt").readlines()]

rx = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
ry = [[0, 0, 1], [0, 1, 0], [-1, 0, 0]]
rz = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]

# run through these rotations in order to hit all 24 cases.
# start, y, y, y, 	x, y, y, y, 		x, y, y, y, 		z', y, y, y			z, y, y, y			z, x, x, x
# 1t, 1r, 1b, 1l, 	4l, 4t, 4r, 4b 	5r, 5b, 5l, 5t		2l, 2t, 2r, 2b		3b, 3l, 3t, 3r		6l, 6t, 6r, 6b
rotation_sequence = ['y', 'y', 'y', 'x', 'y', 'y', 'y', 'x', 'y', 'y', 'y', '-z', 'y', 'y', 'y', 'z', 'y', 'y', 'y', 'z', 'y', 'y', 'y']

completed_matches = {}


class Point3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_list(cls, l):
        return Point3(l[0], l[1], l[2])

    def to_list(self):
        return [self.x, self.y, self.z]

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.z) + ")"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash(str(self))


def map_scanners():
    scanner_map = {}
    curr_scanner = None
    curr_key = None
    for x in data:
        if x != "":
            if x.startswith("---"):
                if curr_scanner is not None:
                    scanner_map[curr_key] = curr_scanner
                curr_key = x.split(" ")[2]
                curr_scanner = []
            else:
                coords = x.split(",")
                curr_scanner.append(Point3(int(coords[0]), int(coords[1]), int(coords[2])))
    scanner_map[curr_key] = curr_scanner
    return scanner_map


def rotate(space, axis):
    rot_mat = rx
    if axis == 'y':
        rot_mat = ry
    elif axis == 'z':
        rot_mat = rz
    new_points = []
    for p in space:
        pl = p.to_list()
        new_points.append(Point3.from_list([sum((rot_mat[i][k] * pl[k]) for k in range(len(rot_mat[0]))) for i in range(len(pl))]))
    return new_points


def check_for_match(ref_space, space, threshold):
    ref_point = ref_space[0]
    for i in space:
        movement = [i.x - ref_point.x, i.y - ref_point.y, i.z - ref_point.z]
        moved_points = []
        for j in space:
            moved_points.append(Point3(j.x - movement[0], j.y - movement[1], j.z - movement[2]))

        matched_points = 0
        for j in moved_points:
            if j in ref_space:
                matched_points += 1

        if matched_points >= threshold:
            return movement
    return False


def do_all_rotations_until_matched(ref_space, space, threshold):
    matched = check_for_match(ref_space, space, threshold)
    if not matched:
        for x in rotation_sequence:
            space = rotate(space, x)
            if x.startswith("-"):
                space = rotate(space, x)
                space = rotate(space, x)

            matched = check_for_match(ref_space, space, threshold)
            if matched:
                break
    if matched:
        print("Matched!", matched)
        # TODO: Now I need to actually do something with the match. Build the aggregate point list...
        return space


def part_one():
    scanner_map = map_scanners()
    for p in scanner_map:
        for q in scanner_map:
            if p != q:
                print("Checking", p, " to ", q)
                do_all_rotations_until_matched(scanner_map[p], scanner_map[q], 12)
    return


def part_two():
    return


if __name__ == '__main__':
    run_with_timer(part_one)  #
    run_with_timer(part_two)  #

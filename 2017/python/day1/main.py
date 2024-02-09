from utils.timers import run_with_timer, get_data_with_timer


def get_data(filename):
    return open(filename).readline().strip()


def calc_captcha(d, offset=1):
    return sum([int(d[x]) for x in range(len(d)) if d[x] == d[(x+offset) % len(d)]])


def part_one(d):
    return calc_captcha(d)


def part_two(d):
    return calc_captcha(d, len(d) // 2)


def main(f="input.txt"):
    data = get_data_with_timer(get_data, f)
    run_with_timer(part_one, data)
    run_with_timer(part_two, data)


if __name__ == '__main__':
    main()

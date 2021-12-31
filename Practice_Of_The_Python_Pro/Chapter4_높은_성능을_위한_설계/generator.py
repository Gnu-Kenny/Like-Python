def range(*args):
    if len(args) == 1:
        start = 0
        stop = args[0]
    else:
        start = args[0]
        stop = args[1]

    current = start

    while current < stop:
        yield current
        current += 1


def main():
    range(1, 3)


if __name__ == "__main__":
    main()

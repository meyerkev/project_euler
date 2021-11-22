#/usr/bin/env python3


def main():
    total = 0
    n1 = 1
    n2 = 1

    while n2 < 4000000:
        tmp = n2
        n2 = n1 + n2
        n1 = tmp
        if not n2 % 2:
            total += n2

    return total


if __name__ == "__main__":
    print(main())

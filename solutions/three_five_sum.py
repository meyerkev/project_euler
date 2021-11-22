#/usr/bin/env python3

import typing

def main():
    total = 0
    for i in range(1, 1000):
        if not i % 3 or not i % 5:
            total += i
    return total



if __name__ == "__main__":
    print(main())

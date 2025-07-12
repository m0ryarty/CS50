import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):

    s = s.lower()

    middle = re.findall(r'^um$|\Wum\W|\Aum\W|\Wum\Z', s)

    return len(middle)


if __name__ == "__main__":
    main()

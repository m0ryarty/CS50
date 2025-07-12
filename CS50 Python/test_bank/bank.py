import sys


def main():
    while True:
        try:
            answer = input("Greeting: ")
            if answer.isdecimal():
                sys.exit()
            print(f'${value(answer)}')
            sys.exit()
        except ValueError:
            sys.exit()
        except EOFError:
            print()
            sys.exit()


def value(greeting):
    if greeting.lower().strip().startswith('hello'):
        return 0
    elif greeting.lower().strip().startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

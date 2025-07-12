import random
import sys


def main():
    level = get_level()
    score = 0

    try:
        for i in range(10):
            number = generate_integer(level)
            x = number
            number = generate_integer(level)
            y = number

            z = x + y

            for j in range(3):
                response = int(input(f'{x} + {y} = '))
                if response == z:
                    score = score + 1
                    break
                else:
                    print('EEE')
                if j == 2:
                    print(f'{x} + {y} = {z}')

        print(f'Score: {score}')

    except ValueError:
        pass
    except EOFError:
        sys.exit()


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass
        except EOFError:
            sys.exit()


def generate_integer(level):
    start = 0
    stop = 10
    if level == 2:
        start = 10
        stop = 100
    elif level == 3:
        start = 100
        stop = 1000

    number = random.randrange(start, stop, 1)
    return number


if __name__ == "__main__":
    main()

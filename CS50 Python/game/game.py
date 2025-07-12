import sys
import random


def main():
    while True:
        try:
            level = int(input('Level: '))
            if level and level > 0:
                break
            else:
                pass
        except ValueError:
            pass
        except EOFError:
            sys.exit()
    guess = random.randrange(1, level, 1)

    while True:
        try:
            number = int(input('Guess: '))
            if number < 1:
                pass
            else:
                if number > guess:
                    print('Too large!')
                elif number < guess:
                    print('Too small!')
                else:
                    print('Just right!')
                    sys.exit()
        except ValueError:
            pass
        except EOFError:
            print()
            sys.exit()


main()

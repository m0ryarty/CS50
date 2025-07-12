import inflect
import sys

p = inflect.engine()


def main():
    name_list = []

    while True:
        try:
            name = input('Name: ')
            if name:
                name_list.append(name)
            else:
                break
        except EOFError:
            print(f'Adieu, adieu, to {p.join(name_list)}')
            sys.exit()


main()

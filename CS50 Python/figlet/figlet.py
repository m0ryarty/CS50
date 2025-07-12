from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


def main():
    font = random.choice(figlet.getFonts())

    if len(sys.argv) == 2:
        sys.exit('Invalid usage')
    elif len(sys.argv) == 3:
        if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in figlet.getFonts():
            font = sys.argv[2]
        else:
            sys.exit('Invalid usage')

    text = input('Input: ')
    figlet.setFont(font=font)
    print(figlet.renderText(text))


main()

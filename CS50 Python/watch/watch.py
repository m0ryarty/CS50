import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    try:
        url = re.search(r'(\bsrc=.+)(embed.{12})', s).group(2)
        videoId = re.split('/', url)

        if videoId:
            return f'https://youtu.be/{videoId[1]}'

    except AttributeError:
        return None


if __name__ == "__main__":
    main()

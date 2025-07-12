import emoji


def main():
    text = input('Input: ')

    print(f'Output: {emoji.emojize(text, language='alias')}')


main()

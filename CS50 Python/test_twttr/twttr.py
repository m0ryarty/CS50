def main():
    while True:
        try:
            tweet = input('Input: ')

            no_vowel = short(tweet)

            print(no_vowel)
        except ValueError:
            pass


def shorten(word):
    no_vowel = ''

    for char in word:

        match char.lower():
            case 'a' | 'e' | 'i' | 'o' | 'u':
                char = ''
        no_vowel = no_vowel + char
    return no_vowel


if __name__ == "__main__":
    main()

def main():
    answer = input("What's the answer to the Great Question of Life, the Universe and Everything? ")

    match answer.lower().strip():
        case '42' | 'forty-two' | 'forty two':
            print('Yes')
        case _:
            print('No')

main()

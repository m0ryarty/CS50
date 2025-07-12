def main():
    answer = input("Greeting: ")

    if answer.lower().strip().startswith('hello'):
        print('$0')
    elif answer.lower().strip().startswith('h'):
        print('$20')
    else:
        print('$100')


main()

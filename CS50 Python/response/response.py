from validator_collection import validators, checkers, errors


def main():

    print(check(input("What's your email adress? ")))


def check(e):
    email = checkers.is_email(e)

    if email:
        return 'Valid'
    else:
        return 'Invalid'


if __name__ == "__main__":
    main()

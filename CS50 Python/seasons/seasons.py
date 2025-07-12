from datetime import date
import inflect
import sys

p = inflect.engine()


def main():
    try:
        minutes_since = minutes(input('Date of Birth: '))
        minutes_since = p.number_to_words(minutes_since).capitalize().replace(' and', '')
        print(f'{minutes_since} minutes')
    except ValueError:
        sys.exit('Invalid Date')


def minutes(d):
    past = date.fromisoformat(d)
    now = date.today()
    all_minutes = (now - past).days * 24 * 60

    return (all_minutes)


if __name__ == "__main__":
    main()

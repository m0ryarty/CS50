def main():
    time = input('What time is it? ')

    mealTime = convert(time)

    if 7 <= mealTime <= 8:
        print('breakfast time')
    elif 12 <= mealTime <= 13:
        print('lunch time')
    elif 18 <= mealTime <= 19:
        print('dinner time')

def convert(time):
    x, y = time.split(':')

    x = float(x)
    y = float(y)

    return x + (y/60)
    ...


if __name__ == "__main__":
    main()

def main():
    while True:
        try:
            fraction = input('Fraction: ')
            tank = convert(fraction)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

    print(gauge(tank))


def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if x > y:
            raise ZeroDivisionError
        else:
            tank = int(round((x / y) * 100))
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError
    return tank


def gauge(percentage):

    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()

def main():


    while True:
        fraction = input('Fraction: ')

        try:
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            tank = int(round((x / y) * 100))

        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            if tank > 100:
                pass
            else:
                if tank <= 1:
                    print('E')
                elif tank >= 99:
                    print('F')

                else:
                    print(f'{tank}%')
                break

main()

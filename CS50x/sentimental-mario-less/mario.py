while True:
    try:
        height = int(input("Height: "))
        if 0 < height < 9:
            break
    except ValueError:
        True

for i in range(height):
    print(((' ' * (height - i - 1) + '#' * (i + 1))))

while True:
    try:
        change = float(input("Change: "))

        if change > 0:
            break
    except ValueError:
        True


def changed(amount, coinType):
    coins = int(amount / coinType)
    rest = round(amount % coinType, 2)
    return [coins, rest]


q = changed(change, 0.25)
d = changed(q[1], 0.1)
n = changed(d[1], 0.05)
p = changed(n[1], 0.01)


print(q[0] + d[0] + n[0] + p[0])

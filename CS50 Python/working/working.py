import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        hours = re.search(r'(.+[AP]M).to(.+[AP]M$)', s)

        g_one = hours.group(1).strip()
        g_two = hours.group(2).strip()

        g_one = re.split(' ', g_one)
        g_two = re.split(' ', g_two)

        if g_one[1] == 'PM':
            pm = g_one[0]
        else:
            am = g_one[0]

        if g_two[1] == 'PM':
            pm = g_two[0]
        else:
            am = g_two[0]

        am_with_colon = re.search(r':', am)
        pm_with_colon = re.search(r':', pm)

        if am_with_colon:
            h, m = re.split(':', am)

            if int(m) >= 60:
                raise ValueError

            if int(h) >= 13:
                raise ValueError

            if h == '12':
                h = '00'

            am = f'{h.rjust(2, '0')}:{m}'
        else:
            if am == '12':
                am = '00'
            am = f'{am.rjust(2, '0')}:00'

        if pm_with_colon:
            h, m = re.split(':', pm)

            if int(m) >= 60:
                raise ValueError

            if int(h) >= 13:
                raise ValueError

            if h != '12':
                h = int(h) + 12

            pm = f'{h}:{m}'
        else:
            if pm != '12':
                pm = int(pm) + 12
            pm = f'{pm}:00'

        if g_one[1] == 'PM':
            return f'{pm} to {am}'
        else:
            return f'{am} to {pm}'

    except (AttributeError, IndexError):
        raise ValueError


if __name__ == "__main__":
    main()

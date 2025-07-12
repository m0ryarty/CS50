def main():
    list_of_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    month  = 0
    while True:
        date = input('Date: ').title()
        try:

            for i in list_of_months:
                if date.startswith(i):
                    month = list_of_months.index(i) + 1
            month = int(month)

            if month == 0:
                m, d, y = date.split('/')

                m = int(m)
                d = int(d)
                y = int(y)

                if m > 12 or d > 31:
                    pass
                else:
                    print(f'{y}-{m:02}-{d:02}')
                    break

            else:
                if date.find(',') == -1:
                    pass
                else:
                    m, d, y = date.replace(',', '').split(' ')
                    d = int(d)
                    y = int(y)
                    if d > 31:
                        pass
                    else:
                        print(f'{y}-{int(month):02}-{d:02}')
                        break

        except ValueError:
            pass

main()

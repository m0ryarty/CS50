import re


def main():

    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        split = re.split('\\.', ip)
        if split and len(split) == 4:
            pass
        else:
            return False

        for i in split:

            if len(i) > 1 and re.search(r'^0', i):
                return False

            if len(i) > 3:
                return False

            i = i.rjust(3, '0')

            if re.search(r'^[3-9]', i):
                return False

            if int(i) > 255 or int(i) < 0:
                return False

        return True

    except ValueError:
        return False


if __name__ == "__main__":
    main()

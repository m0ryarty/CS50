def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    v = True



    if (s.isalpha()) and (len(s) > 2 and len(s) < 7):
        return True

    for char in s:
        if not (char.isdecimal()) and not (char.isalpha()):
            return False

    if len(s) < 2 or len(s) > 7:
      v = False
      return v

    if s[0].isdecimal() or s[1].isdecimal():
        v = False
        return v

    for j in range(len(s)):
        if j > 1:
            if (not s[j-1].isdecimal() and s[j] == '0') or (s[j-1].isdecimal() and s[j].isalpha()):
                return False



    for i in range(len(s)):
        if i > 1:
            v = True
            if s[i].isdecimal():
                v = True
            else:
                v = False

    return v


main()

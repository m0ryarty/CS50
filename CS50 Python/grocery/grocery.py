def main():
    list = {}
    while True:

        try:
            item = input().upper()
            if item in list.keys():
                list[item] = list[item] + 1
            else:
                list.update({item: 1})
        except EOFError:
            for i in sorted(list):
                print(list[i], i)
            break

main()

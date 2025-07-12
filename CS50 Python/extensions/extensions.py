def main():
    name = input('File name: ').strip().lower()

    if name.endswith('.gif'):
        print('image/gif')
    elif name.endswith('.jpg'):
        print('image/jpeg')
    elif name.endswith('.jpeg'):
        print('image/jpeg')
    elif name.endswith('.png'):
        print('image/png')
    elif name.endswith('.pdf'):
        print('application/pdf')
    elif name.endswith('.txt'):
        print('text/plain')
    elif name.endswith('.zip'):
        print('application/zip')
    elif name.count('.') == 0:
        print('application/octet-stream')
    else:
        print('application/octet-stream')


main()

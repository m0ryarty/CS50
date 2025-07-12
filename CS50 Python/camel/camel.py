camel = input('camelCase:   ')

snake = ''


for char in camel:
    if char.isupper():
        char = '_' + char.lower()
    snake = snake + char

print('snake_case: ', snake)

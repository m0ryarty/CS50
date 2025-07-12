from cs50 import get_string

text = get_string('Text: ')

word = 1
letter = 0
sentence = 0
for i in text:
    letter = letter + 1
    if i == '.' or i == '!' or i == '?':
        letter = letter - 1
        sentence = sentence + 1
    if i == ' ':
        letter = letter - 1
        word = word + 1
    if i == ',' or i == ':' or i == ';' or i == "'":
        letter = letter - 1

L = (letter / word) * 100
S = (sentence / word) * 100


index = round(0.0588 * L - 0.296 * S - 15.8)


if index < 1:
    index = 'Before Grade 1'
elif index >= 16:
    index = 'Grade 16+'
else:
    index = f'Grade {index}'


print(index)

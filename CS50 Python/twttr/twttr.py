tweet = input('Input: ')

no_vowel = ''

for char in tweet:
    match char.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u':
            char = ''
    no_vowel = no_vowel + char

print(no_vowel)

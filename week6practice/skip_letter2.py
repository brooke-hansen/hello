def skip_letter2(word):
    letter_lyst = []
    found_letter = ''
    for letter in range(len(word)):
        if letter % 2 == 1:
            found_letter = word[letter]
            letter_lyst.append(found_letter)
            found_letter = ''
    return letter_lyst

print(skip_letter2("counterattack"))
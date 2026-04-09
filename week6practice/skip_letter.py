#Q1 write a function that loops thru word and returns list with every other letter of word
#starting with first letter
def skip_letter(word):
    letter_lyst = []
    found_letter = ""
    for letter in range(len(word)):
        if letter % 2 == 0:
            found_letter = word[letter]
            letter_lyst.append(found_letter)
            found_letter = ''
    return letter_lyst

word = "counterattack"
print(skip_letter("counterattack"))
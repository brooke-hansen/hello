#Q6 function that takes string 
#and returns T/F depending on if isogram

def is_isogram(word):
    seen_letters = {} #create empty dictionary
   
    for letter in word:
        if letter in seen_letters:
            return False
        else:
            seen_letters[letter] = 1
    return True

print(is_isogram("Password"))
print(is_isogram("Praline"))
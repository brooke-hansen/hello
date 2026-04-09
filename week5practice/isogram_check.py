#Q5 create a function that takes a string and returns T/F depending if an isogram 
#only lowercase
def is_isogram(word): 
    seen = set()  
    for char in word:
        if char in seen:
            return False #duplicate found
        else:
            seen.add(char)
    return True

print(is_isogram("annagram"))

word_ = "algorithm"
print(is_isogram(word_))
#Q2 function that takes string
#and returns dict containing count of each letter

def letter_count(word):
    letter_counts = {} #create empty dictionary
    for letter in word: #for each letter in word
        if letter in letter_counts: #if the letter's in the dictionary
            letter_counts[letter] += 1 #add one to value
        else: #if letter isn't already in dictionary
            letter_counts[letter] = 1 #set value to one
    return letter_counts #return final dictionary

print(letter_count("Mississippi"))
#Q13 
# one function returns boolean value determining if letter = vowel (is_vowel)
# other takes string and returns list containing the vowels from OG string

def is_vowel(word):
    vowels = ["a","e","i","o","u"]
    for letter in word:
        if letter in vowels:
            return True

def report_vowels():
         
            

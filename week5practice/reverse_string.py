#Q1 create a function reverse_string that takes variable word and returns word in reverse order
#use a loop, no slicing

def reverse_string(user_word):
    
    reversed_word = ""
    
    for char in user_word:
        reversed_word = char + reversed_word
    
    return reversed_word

word_ = "stressed"
print(reverse_string("loop"))
print(reverse_string(word_))
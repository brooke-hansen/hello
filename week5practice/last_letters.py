#Q8 create a function that takes variable sentences and returns string of last letters of each word
def last_letters(sentence):
    last_lett = ''
    sentence += " "
    #how can we iterate through each char in the sentence?
    for i in range(len(sentence) - 1):
        #check our current char with next
        if sentence[i + 1] == " ":
            last_lett += sentence[i]
    
    return last_lett
sample = "the magic is within you"
print(last_letters(sample))
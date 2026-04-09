
'''
answers = "A C A A CA D B A"

for letter in answers:
    print(letter)
'''
'''
#to initialize a list in code, we use []

lyst = ['a','apple', 7, 12.1, True, 456]
print(x[1][3]) #apple is in index position 1, and the letter 'l' is in position 3 (of apple)
print(x[1],x[2],x[3],x[4])
print(x[1:4+1]) #behaves like splicing and range functions
for index in range(len(lyst)): #starts at 0 and goes up to (but not including length)
    print(lyst[index])

lyst.append() #adds to a list 
'''

#write a function that takes a sentance as a parameter and returns all of the words in that sentance
sentence = "the quick brown fox jumped over the lazy log."

def sentence_to_words(sentence):
    word_lyst = []
    #find the words
    found_word = ' '
    for letter in sentence:
        if letter == " " or letter == "": #indicates a word, so add word to list
            word_lyst.append(found_word)
        else:
            found_word += letter
    return word_lyst

sample_sentence = "cats and dogs are fun"
words = sentence_to_words(sample_sentence)
for word in words:
    print(word)
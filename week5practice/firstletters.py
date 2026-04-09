#Q7 create function that returns string of first letters of words in a sentence
def first_letters(sentence):
    start_lett = ''
    letters = ''
    for letter in sentence:
        if letter == " " or letter == '.':
           if start_lett:
               letters += start_lett[0]
               start_lett = ''
        else:
            start_lett += letter
    if start_lett:
        letters += start_lett[0]
    return letters
sample_sentence = "the magic is within you"
print(first_letters(sample_sentence))

#Q9 create a function flip_flop that takes string as argument
# and returns a new word made of (2/2) + (1/2) of original input
def flip_flop(word):
    length = len(word)
    middle = length // 2
    if length % 2 == 0: #even
        first_half = word[:middle]
        second_half = word[middle:]
        return second_half + first_half
    else: #odd
        first_half = word[:middle]
        middle_letter = word[middle]
        second_half = word[middle+1:]
        return second_half + middle_letter + first_half

print(flip_flop("cranberries"))

word_ = "abcde"
print(flip_flop(word_))
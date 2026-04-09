#Q2 ask for word, print every other letter in word, starting w/ 2nd letter
userword = input('Enter a word: ') #ask for word
for letter in range(len(userword)): #for letters in the range of the length of the word
     if letter % 2 == 1: #if the letter is in an odd index position
         print(userword[letter], end = '') #print the list(letter), same line
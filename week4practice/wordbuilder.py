#Q7 ask user for letters until type done, then print complete word
word = "" #set word to fill-in-blank
while True: #while True loop
    letter = input("Enter a letter (or type 'done' to finish): ") #ask for letter input
    if letter == "done": #if user types done
        break #done
    word += letter #add letters to fill in blank-space word
print("Your new word is:", word) #print accumulated letters
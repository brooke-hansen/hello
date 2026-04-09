'''
#write a function that takes two bounds and return a list containing
#each of the even numbers btwn those bounds (inclusively)

def even_btwn(lower, upper):
    number_list = [] #start as an empty list
    for number in range(lower, upper+1):
        if number % 2 == 0:
            number_list.append(number) #add number to list
    return number_list

print(even_btwn(10,20))
'''
'''
#write a function that takes 2 lists as arguments and returns list w/ greater sum (of elements)
def greater_list(list1,list2):
    total1 = 0
    total2 = 0
    #OPTION A: TWO FOR INDEX LOOPS
    #have to do both index/range(len) separately in case list sizes are diff
    #for index in range(len(list1)):
        #total1 += list1[index]
    #for index in range(len(list2)):
        #total2 += list2[index]

    #OPTION B: INDEX AND ELEMENT
    for index in range(len(list1)):
        total1 += list1[index]
    for element in list2:
        total2 += element
    
    #print check statement
    print(f'{total1 = }, {total2 = }')
    
    #find the totals and compare
    if total1 > total2:
        return list1
    elif total2 > total1:
        return list2
    else:
        print('both lists have the same total')
        return list1

#if lists have different lengths, breaks
list_one = [3, 7, 12, 19, 24, 31, 42, 56, 68, 95]
list_two = [5, 9, 14, 18, 27, 33, 45, 52, 64, 80]

print(greater_list(list_one, list_two))
'''

#continue from last class
#write a function that takes a sentance as a parameter and returns all of the words in that sentance
sentence = "the quick brown fox jumped over the lazy log."

def sentence_2_words_alt(sentence):
    word_lyst = [] 
    found_word = ''
    for index in range(len(sentence)):
        if sentence[index] == " " or index == len(sentence): #if letter == space
            word_lyst.append(found_word) #add word to list
            found_word = '' #reset word
        #elif index == len(sentence)-1:
            #found_word += sentence[index]
            #word_lyst.append(found_word) #add word to list
            #found_word = '' #reset word
        else:
            found_word += sentence[index]
    word_lyst.append(found_word) #alt solution to #elif
    return word_lyst

sample_sentence = "cats and dogs are fun"
words = sentence_2_words_alt(sample_sentence)
for word in words:
    print(word)

#as problem progresses, solution will change and so will code
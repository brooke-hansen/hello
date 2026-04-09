'''
#Q19
def is_acronym(s, words) :
    first_letters = ""
    for word in words:
        first_letter += word[0]
    if s == first_letters:
        return True
    else:
        return False

words_ = ["alice", "bob", "charlie"]
s = "abc"

print(is_acronym(s,words_))
'''
'''
#Q18 function that takes in list of miles run every Sat + returns total # of lag days
def lag_days(runs):
    log_days = 0
    #1. iterate through the list of runs
    for i in range(len(runs) - 1):
        #2. check that the next run is more, else it is a lag day
        if runs[i] > runs [i+1]:
            #3. add up all the lag days 
            log_days += 1
    return log_days

run_record = [10, 11, 12, 9, 10]
run2 = [6, 5, 4, 3, 2, 9]
print(lag_days(run_record))
print(lag_days(run2))
'''

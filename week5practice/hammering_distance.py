#Q4 create function hammering_distance that takes 2 strings as arguments
# and returns the hammering distance btwn the 2 strings
def hammering_distance(string1, string2):
    if len(string1) != len(string2):
        return "words must be of equal length"
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1
    return distance

str1 = "balloring"
str2 = "hectic"
print(hammering_distance(str1,str2))
print(hammering_distance("abcde","ebcda"))
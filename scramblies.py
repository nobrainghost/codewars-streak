''' Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
'''
def scramble(s1, s2):
    count_each_s1={}
    count_each_s2={}
    for letter in s2:
        if letter not in s1:
            return False
    for letter in s1:
        if letter in count_each_s1:
            count_each_s1[letter]+=1
        else:
             count_each_s1[letter]=1
    for letter in s2:
            if letter in count_each_s2:
                count_each_s2[letter]+=1
            else:
                 count_each_s2[letter]=1
    
    for letter in count_each_s2:
        if letter not in count_each_s1:
            print("happened here")
            return False
        elif count_each_s1[letter]<count_each_s2[letter]:
            return False
    return True
                    

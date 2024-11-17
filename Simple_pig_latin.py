'''Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.'''


def pig_it(text):
    text=text.split(" ")
    new_array=[]
    for i in text:
        print(i)
        if i.isalpha():
            i=i+i[0]
            i=i+"ay"
            i=i[1:]
            new_array.append(i)
        else:
            new_array.append(i)
    new_string=" ".join(new_array)
    return new_string

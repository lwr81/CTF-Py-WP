str1 = '1122334455667788'

def Add_Space(text):
    i = 0
    str2 = ''
    for a in text:
        i += 1
        if i % 3 == 1:
            str2 = str2 + a
        elif i % 3 == 2:
            str2 = str2 + a
        elif i % 3 == 0:
            str2 = str2 + ' ' + a
            i = i + 1
    print(str2)


Add_Space(str1)

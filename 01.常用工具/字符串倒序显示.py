a = 'abcdefghijklmnopq'
b = list(a)[::-1]
# b.reverse()
print(type(b))
c = ''
for i in b:
    c += i
print(c)

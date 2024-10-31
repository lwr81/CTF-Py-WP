import execjs
with open("1.js", 'r') as f:
    a = execjs.compile(f.read())
result1 = a.call('a', "1234")
print(result1)

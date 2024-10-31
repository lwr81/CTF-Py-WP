#  方法一
import subprocess
import json
import re
import binascii

# command = 'tshark.exe -r capture.pcapng -T json -e dns.qry.name > 1.json'
# proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# proc.communicate()

with open('1.json', 'r') as f:
    data = json.load(f)
a1 = []
for i in data:
    try:
        a1.append(i['_source']['layers']['dns.qry.name'][0])
    except:
        continue
# print(a1)

a2 = []

for i in a1:
    # print(i)
    a2.append(i.replace('.secret.base', ''))
a3 = []
c = 0
while c < len(a2):
    a3.append(a2[c])
    c = c + 2
print(a2)
print(len(a2))
print(a3)
print(len(a3))
flag=''
for i in a3:
    flag += i
open("flag.zip", "wb").write(binascii.unhexlify(flag))

# # 方法二
# import binascii
# import subprocess
#
# command = 'tshark.exe -r capture.pcapng -T fields -e dns.qry.name > hex.txt'
# proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# proc.communicate()
# lines = open("hex.txt", 'r', encoding='utf-8').readlines( )
# print(lines)
# byte = ""
# i = True
# for l in lines:
#     if i:
#         byte += l.replace(".secret.base", "").replace("\n", "")
#     i = not i
# print(byte)
#
# # open("data", "wb").write(binascii.unhexlify(byte))

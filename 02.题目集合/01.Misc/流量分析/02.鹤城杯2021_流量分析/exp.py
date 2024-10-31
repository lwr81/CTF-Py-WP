import re
import subprocess
import json
from urllib.parse import unquote

# command = 'tshark -r icmp.pcapng -Y "icmp.type ==8" -T json >1.json'
# command = 'tshark.exe -r timu.pcapng -Y "http" -T json -e "http.request.uri" > 1.json'
# proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# proc.communicate()

with open('1.json', 'r') as f:
    data = json.load(f)
a1 = []
for i in data:
    try:
        a1.append(i['_source']['layers']['http.request.uri'][0])
    except:
        continue

print(a1)
a2 = {}
re1 = re.compile(r",(\d+),1\)\)=(\d+)")
for i in a1:
    re2 = re1.search(i)
    b1 = re2[1]
    b2 = re2[2]
    a2[b1] = b2
print(a2)

flag = ""
for i in a2:
    flag += chr(int(a2[i]))
print(flag)

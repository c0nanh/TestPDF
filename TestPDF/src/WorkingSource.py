import re
data = "Myanmar burma ESG Sustainable "
patterns = [ 'Myanmar', 'Burma', 'CSR', 'Social Responsibility', 'ESG', 'sustainable', 'sustainability' ]

regex = re.compile("\w+")
print regex
flag = [False] * len(patterns)
print flag

#print [m for p in patterns for m in [regex.search(p)]]



for i in range(len(patterns)):
    if re.search(patterns[i], data, flags=re.IGNORECASE):
        flag[i] = True

print str(flag)
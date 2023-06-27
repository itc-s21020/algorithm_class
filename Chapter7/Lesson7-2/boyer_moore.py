test = "I'm learning Python3. It's interesting!"
pattern = "Python3"
tn = len(test)
pn = len(pattern)
skip = [pn]*256
for i in range(pn-1):
    o = ord(pattern[i])
    skip[o] = pn-i-1

flg = False
p = pn-1
while p < tn:
    flg = True
    for i in range(pn):
        if test[p-i] != pattern[pn-1-i]:
            f
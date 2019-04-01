n = int(input())
a = []
b = []
for i in range(n):
    a.append(input())
    b.append(float(input()))
c = sorted(b)
l = 1
while l < len(c) and c[0]==c[l]:
    l+=1
s = l+1
while s < len(c) and c[l]==c[s]:
    s+=1
sortedList = []
for x in range (s-l):
    if b.__contains__(c[l+x]):
        sortedList.append(a[b.index(c[l+x])])
        a.pop(b.index(c[l + x]))
        b.pop(b.index(c[l+x]))
sortedList = sorted(sortedList)
for a in sortedList:
    print(a)
n = int(input())
b = []
for x in range(n):
    a = input().split()
    if a[0] == "insert":
        b.insert(int(a[1]), int(a[2]))
    if a[0] == "print":
        print(b)
    if a[0] == "remove":
        b.remove(int(a[1]))
    if a[0] == "append":
        b.append(int(a[1]))
    if a[0] == "sort":
        b.sort()
    if a[0] == "pop":
        b.pop()
    if a[0] == "reverse":
        b.reverse()


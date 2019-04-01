n = int(input())
a = []
for x in range(n):
    a.append(input().split())
requested = input()
for x in a:
    if x[0] == requested:
        avg = (float(x[1]) + float(x[2]) + float(x[3]))/3
        print("%.2f" % avg)
        break
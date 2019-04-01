def mutate_string(s, p, c):
    l = ""
    for i in range(len(s)):
        if i == p:
            l += c
        else:
            l += s[i]
    return l

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
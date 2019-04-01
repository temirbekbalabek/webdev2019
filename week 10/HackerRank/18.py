import textwrap

def wrap(string, n):
    result = ""
    for i in range(0, len(string), n):
        if i + n <= len(string):
            res1 = ""
            for j in range(i, i + n):
                res1 += string[j]
            result += res1
            result += "\n"
        else:
            res2 = ""
            for l in range(i, len(string)):
                res2 += string[l]
            result += res2
            result += "\n"
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
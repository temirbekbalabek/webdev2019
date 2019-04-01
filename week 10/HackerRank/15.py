def count_substring(string, sub_string):
    i = 0
    cnt = 0
    while i + len(sub_string) <= len(string):

        if string.find(sub_string, i, i + len(sub_string)) != -1:
            cnt += 1
        i += 1
    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
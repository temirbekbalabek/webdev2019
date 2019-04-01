if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    for x in range(n):
        arr[x] = int(arr[x])
    arr = sorted(arr, reverse=True)
    i = 1
    while arr[0]==arr[i]:
        i+=1

    print(arr[i])

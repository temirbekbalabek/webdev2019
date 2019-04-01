#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    cnt = 0
    b = []
    for j in range(len(s)):
        if s[j] == " ":
            cnt += 1
        else:
            if cnt != 0:
                b.append(cnt)
                cnt = 0

    a = s.split()
    l = ""
    for i in range(len(a)):
        a[i] = a[i].capitalize()
        l += a[i]
        length = i
        if length < len(a) - 1:
            for u in range(0, b[length]):
                l += " "
    return l
if __name__ == '__main__':


    s = input()

    result = solve(s)
    print(result)

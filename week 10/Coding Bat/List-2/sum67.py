def sum67(nums):
    sum = 0
    bad = False
    for i in nums:
        if i == 6:
            bad = True
        if not bad:
            sum += i
        if i == 7:
            bad = False
    return sum
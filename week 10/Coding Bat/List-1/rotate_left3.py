def rotate_left3(nums):
    a = [0] * len(nums)
    a[-1] = nums[0]
    for i in range(len(nums) - 1):
        a[i] = nums[i + 1]
    return a
# -*- coding = utf-8 -*-
# @Time: 2021/2/26 下午 2:11
'''
找到合适的下标,如果没有这个值，返回比这个是数字略大的下标
'''
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
nums2 = [0, 1]
traget = 6.5
traget2 = 0.5


def binaryser1(nums, target):
    low = 0
    high = len(nums) - 1
    now = 0
    while (low <= high):
        now = int(low + (high - low) / 2)
        num = nums[now]
        if (num < traget):
            low = now + 1
        elif (num > traget):
            high = now - 1
        else:
            break
    if (nums[now] < target):
        return now + 1
    return now


def binaryser2(nums, target, high, low):
    if (high >= low):
        mid = int(low + (high - low) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binaryser2(nums, target, high, mid + 1)
        else:
            return binaryser2(nums, target, mid - 1, low)
    else:
        return -1


now = binaryser1(nums, traget)
print(now)
print(binaryser1(nums2, traget2))
now = binaryser2(nums, traget, len(nums) - 1, 0)
print(now)

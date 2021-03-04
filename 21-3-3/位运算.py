# -*- coding = utf-8 -*-
# @Time: 2021/3/3 下午 7:25
# &（按位与，全1为1,常与1相&判断最后一位是0还是1）
# | （按位或，全0为0，常和0相并）
# ~（按位非）
# ^（按位异或，相同为0，有交换律，a^0=a,a^1=~a），
# << (有符号左移位)
# >>（有符号右移位） //2
a = 1
b = 1
c = 1


# 奇偶判断
def isodd(x):
    return True if (x & 1) else False


# 左移一位相当于乘以2，右移一位相当于除以2
'''
midpoint = (low + high) >> 1
等价于 midpoint = (low + high) // 2
'''


# 交换数值
def swap(a, b):
    a ^= b
    b ^= a
    a ^= b


# 找独一无二的数字
def find(nums):
    x = 0
    for i in nums:
        x ^= i
    return x


# 找2进制中1个数
def number1Bit(x):
    count = 0
    while x:
        count = count + (x & 1)
        x = x >> 1
    return count


print(number1Bit(5))

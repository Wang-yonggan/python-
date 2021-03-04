# -*- coding = utf-8 -*-
# @Time: 2021/3/3 下午 8:14
'''
a和b的二进制中不同位的个数
思想：a和b相异或得c，c中1的个数
'''


def get(a, b):
    c = a ^ b
    count = 0
    while (c > 0):
        count += c & 1
        c >>= 1
    return count


print(get(10, 26))

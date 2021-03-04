# -*- coding = utf-8 -*-
# @Time: 2021/3/3 下午 7:13
'''
a的n次幂 对b取余
'''


def fast(a, b, n):
    ans = 1
    while n > 0:
        if n % 2 == 1:
            ans = ans * a % b
        a = a * a % b
        n /= 2
    return ans % b


print(fast(2, 3, 31))

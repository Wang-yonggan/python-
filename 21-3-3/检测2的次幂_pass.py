# -*- coding = utf-8 -*-
# @Time: 2021/3/3 下午 5:06
num = 100
flag = False


def is2(num):
    # while num > 1:
    #     if (num % 2 == 0):
    #         num /= 2
    #         continue
    #     else:
    #         break
    # return not (num - 1)
    ans = 1
    while (ans <= num):
        if ans == num:
            return True
        ans <<= 1
    return False


x = pow(2, 40)
print(is2(x))

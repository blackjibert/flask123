"""
偏函数(functools.partial)
"""

import functools

def func(a1, a2, a3):
    return a1 + a2 + a3

v1 = func(1, 2, 3)

new_func = functools.partial(func, 111, 2)  # 前两个参数固定为111,2

print(new_func(3))
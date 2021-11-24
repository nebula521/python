# 结果 = (lambda 形参 : 返回值)(实参1`)
print((lambda x, y=3: x * y)(1,2))

print(list(filter(lambda x: x if x % 2 else None, range(1, 10))))  # filter过滤器，过滤出1-9中符合f1的数

print(list(map(lambda x, y: [x, y], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))  # map可以接收多个序列作为参数

"""
递归函数的要求:
1.要出现自身调用自身的现象
2.要具有明确的结束标志
"""

"""
递归函数是自身调用自身: 
调用层数问题:
1000 > 1000次的函数的调用了 超出了范围...
本身就有两次 2 + 999 = 1001 > 1000
             2 + 998 = 1000 

1000层以内的调用是被允许的....python解释器规定...了解即可,,,,,,,,,,,

"""

def demo(a):
    if a == 1:
        return 1
    return demo(a - 1) + a


# return  100 + 99 + 98 + 97 ......1
# 函数的调用
print('程序开始了...')
res_ = demo(998)
print(res_)
print('程序结束了...')
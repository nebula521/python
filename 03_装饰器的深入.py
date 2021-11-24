"""
装饰器的深入
"""
"""
闭包的介绍
1.两个函数的嵌套
2.内部函数本身作为外部函数的返回值
3.内部函数用到了外部函数的数据
"""

"""
1.装饰器的原理: 就是把要被装饰的函数当做一个实参,传进一个闭包,在调用他的前后,去添加代码增加功能,
2.装饰器的一个机制: 装饰器只能对函数起作用(重点)
"""


def a(c):
    def b(*args, **kwargs):
        print('中华人民共和国的:', end='')
        return c(*args, **kwargs)  # '今天天气不错'

    return b


@a  # demo = a(demo)
def demo1(name):
    print(f'湖南省的{name}')
    return '今天天气不错'


res_ = demo1('瑶瑶老师')  # res代表b()的返回值，b()返回的是c(),即res_代表c()的返回值
print(res_)


# 第一个闭包
def a(c):  # c是形参,接收的是要被装饰的函数
    print('这是第一个装饰器......')  # (2)只要调用a函数就会被执行

    def a_in(*args, **kwargs):
        print('添加了第一种功能......')  # (3)
        return c(*args, **kwargs)  # 如果有返回值,就需要先加()

    return a_in


# 第二个闭包
def b(c):  # c是形参,接收的是要被装饰的函数
    print('这是第二个装饰器******')  # (1)只要调用b函数就会被执行

    def b_in(*args, **kwargs):
        print('添加了第二种功能******')  # (4)
        return c(*args, **kwargs)  # 如果有返回值,就需要先加()

    return b_in


@a  # b_in = a(b_in)
@b  # demo = b(demo)
def demo():
    print('长清老师真帅气......')  # (5)


demo()
# 这是第二个装饰器******
# 这是第一个装饰器......
# 添加了第一种功能......
# 添加了第二种功能******
# 长清老师真帅气......


"""
装饰器携带参数的情况
"""


def a(name):  # c是形参,接收的是要被装饰的函数
    print('这是第一个装饰器......')  # (1)只要调用a函数就会被执行

    def a1(c):
        print(name)  # (2) 我是一个参数....

        def b(*args, **kwargs):
            print('添加了第一种功能......')  # (3)
            return c(*args, **kwargs)  # 如果有返回值,就需要先加()

        return b

    return a1


@a(name='我是一个参数....')  # @a  >  demo = a(name = '我是一个参数....')(demo)
def demo():
    print('长清老师真帅气......')  # (4)


# 调用函数
demo()


"""
@a  >  demo = a(name = '我是一个参数....')(demo)
1.a(name = '我是一个参数....') > print('这是第一个装饰器......') 返回值是a1
2.demo = a1(demo)  >>> 最基础的装饰器
3.a1(demo) >> print(name)  # (2) 我是一个参数.... 返回值 b
4.demo = b
5demo()  >>> b()
"""
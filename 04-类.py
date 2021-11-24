class Father():
    def __str__(self):  # 函数的文档注释
        return "注释信息"

    def __init__(self,name):
        self.name = name
        self.__idcard = '4306262000'  # 将其私有化 将其封装起来之后,是拿不到的,,

    def get_idcard(self):
        """获得私有属性"""
        return self.__idcard

    def set_idcard(self, id):
        self.__idcard = id

    def myself(self):
        print(f'我是:{self.name}')

    @classmethod
    def country(cls):  # 调用：Man.country()
        print("中国")

    @staticmethod  # 静态方法。调用：Man.demo()
    def demo():
        print('我是一个demo函数')


class Son(Father):
    # 类变量
    __instance = None  # 私有化保护类变量,不能被外界干预

    # 重写object用来创建对象的new方法
    def __new__(cls, *args, **kwargs):
        print('new方法被调用')
        # 调用object的new方法,让对象成功的创建
        if cls.__instance is None:  # 就对象成功的创建 类变量的值 None > 非None
            cls.__instance = object.__new__(Son)  # 创建对象,一般默认名称instance
        return cls.__instance  # 把创建出来的对象return出去,让创建对象时候的对象名进行接收

    def myself(self):
        print('我就是我,颜色不一样的烟火......')
        # 调用格式一:父类名.方法名(对象)  >>> 想要跨越第一级父类取资源
        # Father.myself(self)

        # 调用格式二:super(子类名, 对象).方法名()
        # super(Son, self).myself()

        # 调用格式三:super().方法名()  >>> 最方便,推荐大家使用
        # super().myself()

    def run(self):
        super().myself()
        self.myself()

son1 = Son('wxy')  # son1和son2的id相同
print(son1)  # 注释信息

son1.set_idcard(430626)
print(f'修改之后的,{son1.get_idcard()}')  # 修改之后的,430626

print(Son.__mro__)  # 查看继承关系

son1.run()

"""
==   判断的是两边的数据是否相等
is   判断的是两边的内存地址是否相等
"""







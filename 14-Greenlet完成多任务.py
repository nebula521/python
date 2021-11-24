"""
greenlet是对yield进行了封装,了解即可,
"""

from greenlet import greenlet
import time


def sing():
    while True:
        print('瑶瑶老师在唱歌......')
        time.sleep(0.3)
        g2.switch()  # 指向的是dance部分


def dance():
    while True:
        print('瑶瑶老师在跳舞******')
        time.sleep(0.3)
        g1.switch()  # 指向的是什么sing部分


def main():
    g1.switch()  # 进行切换,切换到创建对象的时候指向的部分


if __name__ == '__main__':
    g1 = greenlet(sing)  # 创建了一个对象,指向了sing函数
    g2 = greenlet(dance)  # 不能放在main里，放在函数里不是全局的
    main()
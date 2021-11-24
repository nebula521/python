"""
协程完成多任务: yield
"""
import time


def sing():  # 生成器模板
    while True:
        print('瑶瑶老师在唱歌......')
        time.sleep(0.3)
        yield  # 没有返回值的情况下,起到暂停挂起的效果


def dance():
    while True:
        print('瑶瑶老师在跳舞******')
        time.sleep(0.3)
        yield


def main():
    g1 = sing()  # 创建生成器对象, next()就可以调用一次生成器模板
    g2 = dance()
    while True:
        next(g1)  # 变成了非阻塞状态
        next(g2)


if __name__ == '__main__':
    main()
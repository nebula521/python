"""
gevent机制是遇到延迟操作 就 自动切换 任务....
打补丁: 就是可以让一些正常的延迟, 来触发gevent任务的切换
"""

import gevent
import time
from gevent import monkey

# 打补丁
monkey.patch_all()  # 只需要这句代码执行, 程序中的延迟操作,就会骗过gevent,,让他看成是自己的延迟操作进行切换


def sing():
    for i in range(1, 6):
        print(f'瑶瑶老师唱第{i}首歌......')
        # 延时,为了让gevent进行任务的切换
        time.sleep(0.5)  # 通过打补丁的方式,,骗过gevent去进行任务的切换,,实现多任务
        # gevent.sleep(0.5)  # gevent自带的延迟方法 自动切换任务 让程序变成非阻塞状态..


def dance():
    for i in range(1, 6):
        print(f'瑶瑶老师跳第{i}支舞......')
        time.sleep(0.5)
        # gevent.sleep(0.5)


def main():
    g1.join()  # start
    g2.join()  # start


if __name__ == '__main__':
    # 使用gevent进行任务
    g1 = gevent.spawn(sing)   # 协程对象 > sing
    g2 = gevent.spawn(dance)  # 协程对象 > dance
    main()


"""
网络延迟
文件的读写
"""

"""
死锁是一个概念,,状况,,了解即可
互斥锁,,,得开锁之后,,才能够进行任务的切换....

如果有两把锁, 你在我等我释放锁,,我在等你释放锁....死锁的现象....
"""

import threading
import time

class MyThread1(threading.Thread):
    def run(self):
        """子线程A运行"""
        # 对mutexA上锁
        mutexA.acquire()

        # mutexA上锁后，延时1秒，等待另外那个线程 把mutexB上锁
        print(self.name+'----do1---up----')
        time.sleep(1)

        # 此时会堵塞，因为这个mutexB已经被另外的线程抢先上锁了
        mutexB.acquire()  # 需要用到锁B
        print(self.name+'----do1---down----')
        mutexB.release()

        # 对mutexA解锁
        mutexA.release()

class MyThread2(threading.Thread):
    def run(self):
        """子线程B运行"""
        # 对mutexB上锁
        mutexB.acquire()

        # mutexB上锁后，延时1秒，等待另外那个线程 把mutexA上锁
        print(self.name+'----do2---up----')
        time.sleep(1)

        # 此时会堵塞，因为这个mutexA已经被另外的线程抢先上锁了
        mutexA.acquire()  # 想使用锁A
        print(self.name+'----do2---down----')
        mutexA.release()

        # 对mutexB解锁
        mutexB.release()

mutexA = threading.Lock()  # 锁A
mutexB = threading.Lock()  # 锁B

if __name__ == '__main__':
    t1 = MyThread1()  # 子线程A
    t2 = MyThread2()  # 子线程B
    t1.start()
    t2.start()


"""
在子线程B里面,,想要获取锁A的使用...
在子线程A里面,,想要获取锁B的使用...
等待对方释放锁
"""
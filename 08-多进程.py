import multiprocessing
import time
import os


def sing():
    for i in range(3):
        print(f"唱歌{os.getpid()},父进程{os.getppid()}")
        time.sleep(0.5)


def dance():
    for i in range(3):
        print(f"跳舞{os.getpid()},父进程{os.getppid()}")
        time.sleep(0.5)


def run():
    p1 = multiprocessing.Process(target=sing)
    p2 = multiprocessing.Process(target=dance)
    p1.start()
    # p1.join(5)  # 确保子进程A执行完毕/设置最大等候时间
    p2.start()
    time.sleep(4)
    print(f"进程号{os.getpid()},父进程{os.getppid()}")


if __name__ == '__main__':
    run()

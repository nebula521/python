import threading
import time

"""互斥锁"""
num = 0


def demo1(a):
    global num
    for i in range(a):
        lock.acquire()
        num += 1  # 1.获取num的值  2.num += 1  3.的值赋值给num
        lock.release()
    print(f"demo1中，num的值为{num}")


def demo2(a):
    global num
    for i in range(a):
        lock.acquire()
        num += 1
        lock.release()
    print(f"demo2中，num的值为{num}")


lock = threading.Lock()  # 互斥锁


def run():
    i = 1000000
    t1 = threading.Thread(target=demo1, args=(i,))
    t2 = threading.Thread(target=demo2, args=(i,))
    t1.start()
    t2.start()
    time.sleep(3)


if __name__ == '__main__':
    run()
    print(f"最终num的值为{num}")

"""查看线程数目"""
# def sing():
#     for i in range(3):
#         print("唱歌")
#         time.sleep(1)
#
#
# def dance():
#     for i in range(3):
#         print("跳舞")
#         time.sleep(1)
#
#
# def main():
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)
#     t1.start()
#     t2.start()
#     while True:
#         data = len(threading.enumerate())  # 查看线程数目
#         print(data)
#         time.sleep(1)
#         if data <= 1:
#             break
#
#
# main()

"""类"""
# class DiyThread(threading.Thread):
#     def run(self):
#         for i in range(3):
#             time.sleep(1)
#             print(len(threading.enumerate()))
#
#
# t1 = DiyThread()
# t1.start()
# time.sleep(4)
# print("类外", len(threading.enumerate()))
import threading
import time

def task(name):
    time.sleep(5)
    print(f"子线程{name}运行完毕！")

def sum(name):
    i=0
    while i <= 9999*9999:
        i=i+1
    print(f"子线程{name}计算结果为：{i}")

def main():
    start_time = time.time()
    # 创建线程
    thread1 = threading.Thread(target=sum, args=("A"))
    thread2 = threading.Thread(target=sum, args=("B"))
    # 启动线程
    thread1.start()
    thread2.start()
    # 等待子线程运行完毕
    thread1.join()
    thread2.join()
    end_time = time.time()
    print(f"主线程运行完毕！耗时：{end_time-start_time}")


if __name__ == "__main__":
    main()
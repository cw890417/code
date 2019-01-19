from concurrent.futures import ThreadPoolExecutor
import threading
import time


def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))
        my_sum += i
    return my_sum


# 创建大小为2的线程池
with ThreadPoolExecutor(max_workers=2) as pool:
    future1 = pool.submit(action, 50)
    future2 = pool.submit(action, 100)


    def get_result(future):
        print(future.result())


    # 添加线程完成的回调函数
    future1.add_done_callback(get_result)
    future2.add_done_callback(get_result)
    print("-------------------")

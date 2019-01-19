import threading
from concurrent.futures import ThreadPoolExecutor


def action(max):
    """
    创建线程执行方法
    :param max:
    :return:
    """
    for i in range(max):
        print(threading.current_thread().getName() + " " + str(i))


for x in range(100):
    print(threading.current_thread().getName() + " " + str(x))
    if x == 20:
        """
        #创建线程
        t1 = threading.Thread(target=action, args=(100,))
        #启动线程
        t1.start()
        t2 = threading.Thread(target=action, args=(100,))
        t2.start()
        """
        with ThreadPoolExecutor(max_workers=4) as pool:
            pool.map(action, (80, 80))

print('主线程执行完毕！')

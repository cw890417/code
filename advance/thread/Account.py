from concurrent.futures import ThreadPoolExecutor
import threading
import time

"""
模拟银行取钱
使用锁
"""


class Account:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self._balance = balance
        # 初始化锁对象
        self.lock = threading.RLock()

    def getBalance(self):
        return self._balance

    def draw(self, draw_amount):

        # 启用锁
        self.lock.acquire()
        try:
            if self._balance >= draw_amount:
                print(threading.current_thread().name + "成功取钱：" + str(draw_amount))
                time.sleep(0.001)
                self._balance -= draw_amount
                print("余额：" + str(self._balance))
            else:
                print(threading.current_thread().name + "取钱失败!")
        finally:
            # 释放锁，放在finally
            self.lock.release()


def draw(account, draw_amount):
    account.draw(draw_amount)


acct = Account("123456", 1000)
# threading.Thread(target=draw, args=(acct, 800), name='甲').start()
# threading.Thread(target=draw, args=(acct, 800), name='乙').start()

with ThreadPoolExecutor(max_workers=4) as pool:
    pool.submit(draw(acct, 80))
    pool.submit(draw(acct, 800))
    pool.submit(draw(acct, 900))

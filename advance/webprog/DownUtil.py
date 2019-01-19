from urllib.request import *
import threading


class DownUtil:
    def __init__(self, path, target_file, thread_num):
        self.path = path
        self.thread_num = thread_num
        self.target_file = target_file
        self.threads = []

    def download(self):
        req = Request(url=self.path, method='GET')

        req.add_header('Accept', '*/*')
        req.add_header('Charset', 'UTF-8')
        req.add_header('Connection', 'Keep-Alive')

        f = urlopen(req)
        self.file_size = int(dict(f.headers).get('Content-Length', 0))
        f.close()

        current_part_size = self.file_size // self.thread_num
        for i in range(self.thread_num):
            start_pos = i * current_part_size
            t = open(self.target_file, 'wb')
            t.seek(start_pos, 0)

            td = DownThread(self.path, start_pos, current_part_size, t)
            self.threads.append(td)
            td.start()

    def get_complete_rate(self):
        sum_size = 0
        for i in range(self.thread_num):
            sum_size += self.threads[i].length
        return sum_size / self.file_size


class DownThread(threading.Thread):
    def __init__(self, path, start_pos, current_part_size, current_part):
        super().__init__()
        self.path = path
        self.start_pos = start_pos
        self.current_part_size = current_part_size
        self.current_part = current_part
        self.length = 0

    def run(self):
        req = Request(url=self.path, method='GET')

        req.add_header('Accept', '*/*')
        req.add_header('Charset', 'UTF-8')
        req.add_header('Connection', 'Keep-Alive')

        f = urlopen(req)
        print(threading.current_thread().getName() + " 11111")
        for i in range(self.start_pos):
            f.read(1)
        print(threading.current_thread().getName() + " 22222")
        while self.length < self.current_part_size:
            data = f.read(1024)
            if data is None or len(data) <= 0:
                break
            self.current_part.write(data)
            self.length += len(data)
        self.current_part.close()
        f.close()


du = DownUtil("http://www.crazyit.org/data/attachment/forum/201801/19/121212ituj1s9gj8g880jr.png", "a.png", 3)
du.download()


def show_process():
    print("已完成：%.2f" % du.get_complete_rate())
    global t
    if du.get_complete_rate() < 1:
        t = threading.Timer(1, show_process)
        t.start()


t = threading.Timer(1, show_process)
t.start()

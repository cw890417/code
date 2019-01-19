class Fibs(object):
    """实现迭代器"""

    def __init__(self, len):
        super(Fibs, self).__init__()
        self.len = len
        self.first = 0
        self.sec = 1

    def __next__(self):
        if self.len == 0:
            raise StopIteration

        self.first, self.sec = self.sec, self.first + self.sec
        self.len -= 1
        return self.first

    def __iter__(self):
        return self


fibs = Fibs(10)
# print(next(fibs))
for x in fibs:
    print(x, end=' ')

print("\n")
my_iter = iter([2, 3, 4, 5, 'a'])
# print(my_iter.__next__())
for myiter in my_iter:
    print(myiter, end=' ')

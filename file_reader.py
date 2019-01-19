# 读取文件内容
file_path = '/Users/chenwei/code/data/pi.txt'

with open(file_path) as file_object:
    # 读取文件的全部内容
    contents = file_object.read()
    print(contents)

# 文件末尾有换行符
with open(file_path) as file_object1:
    for line in file_object1:
        print(line)

# with外使用内容
with open(file_path) as file_object2:
    lines = file_object2.readlines()

for line in lines:
    print(line.rstrip())

# 文件操作的三种方式open('',<w,r,a>)
# r：读 w：写 a：附加
with open(file_path, 'a') as file_object3:
    file_object3.write('asdf')

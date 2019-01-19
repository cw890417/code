import sqlite3

def creat_table():
    #创建连接
    conn = sqlite3.connect('first.db')
    #打开游标
    c = conn.cursor()
    #执行语句
    c.execute('''create table user_tb(_id integer primary key autoincrement,name text,pass text,gender text)''')
    #关闭游标
    c.close()
    #关闭连接
    conn.close()

def inst_data():
    conn = sqlite3.connect('first.db')
    c = conn.cursor()
    c.execute('insert into user_tb values(null,?,?,?)',('sunwukong','123456','male'))
    conn.commit()
    c.close()
    conn.close()

def select_data():
    conn = sqlite3.connect('first.db')
    c = conn.cursor()
    c.execute('select * from user_tb where 1 = ?',(1,))
    print('rowcount:',c.rowcount)
    for col in c.description:
        print(col[0],end = '\t')
    while True:
        row = c.fetchone()
        if not row:
            break
        print(row)
        print(row[1] + '->' + row[2])

    c.close()
    conn.close()

if __name__ == '__main__':
    select_data()